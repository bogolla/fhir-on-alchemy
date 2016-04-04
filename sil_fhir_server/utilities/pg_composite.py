"""
CompositeType provides means to interact with
`PostgreSQL composite types`_.

.. _PostgreSQL composite types:
    http://www.postgresql.org/docs/devel/static/rowtypes.html
"""
from collections import namedtuple

import six
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql.psycopg2 import PGDialect_psycopg2
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.schema import _CreateDropBase
from sqlalchemy.sql.expression import FunctionElement
from sqlalchemy.types import (
    SchemaType,
    to_instance,
    TypeDecorator,
    UserDefinedType
)


class ImproperlyConfigured(Exception):
    """
    Global Custom data types exception class.

    SQLAlchemy-Utils is improperly configured; normally due to usage of
    a utility that depends on a missing library.
    """


psycopg2 = None
CompositeCaster = None
adapt = None
AsIs = None
register_adapter = None
try:
    import psycopg2
    from psycopg2.extras import CompositeCaster
    from psycopg2.extensions import adapt, AsIs, register_adapter
except ImportError:
    pass


class CompositeElement(FunctionElement):
    """
    Instances of this class wrap a Postgres composite type.
    """
    def __init__(self, base, field, type_):
        self.name = field
        self.type = to_instance(type_)

        super(CompositeElement, self).__init__(base)


@compiles(CompositeElement)
def _compile_pgelem(expr, compiler, **kw):
    return '(%s).%s' % (compiler.process(expr.clauses, **kw), expr.name)


registered_composites = {}


class CompositeType(UserDefinedType, SchemaType):
    """ Represents a PostgreSQL composite type.

    Extends:
        UserDefinedType
        SchemaType

    :param name:
        Name of the composite type.
    :param columns:
        List of columns that this composite type consists of
    """

    python_type = tuple

    class comparator_factory(UserDefinedType.Comparator):
        def __getattr__(self, key):
            try:
                type_ = self.type.typemap[key]
            except KeyError:
                raise KeyError(
                    "Type '%s' doesn't have an attribute: '%s'" % (
                        self.name, key
                    )
                )

            return CompositeElement(self.expr, key, type_)

    def __init__(self, name, columns):
        if psycopg2 is None:
            raise ImproperlyConfigured(
                "'psycopg2' package is required in order to use CompositeType."
            )
        SchemaType.__init__(self)
        self.name = name
        self.columns = columns
        if name in registered_composites:
            self.type_cls = registered_composites[name].type_cls
        else:
            self.type_cls = namedtuple(
                self.name, [c.name for c in columns]
            )
        registered_composites[name] = self

        class Caster(CompositeCaster):
            def make(obj, values):
                return self.type_cls(*values)

        self.caster = Caster
        attach_composite_listeners()

    def get_col_spec(self, **kw):
        return self.name

    def bind_processor(self, dialect):
        def process(value):
            if value is None:
                return None
            processed_value = []
            for i, column in enumerate(self.columns):
                if isinstance(column.type, TypeDecorator):
                    processed_value.append(
                        column.type.process_bind_param(
                            value[i], dialect
                        )
                    )
                else:
                    processed_value.append(value[i])
            return self.type_cls(*processed_value)
        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            if value is None:
                return None
            cls = value.__class__
            kwargs = {}
            for column in self.columns:
                if isinstance(column.type, TypeDecorator):
                    kwargs[column.name] = column.type.process_result_value(
                        getattr(value, column.name), dialect
                    )
                else:
                    kwargs[column.name] = getattr(value, column.name)
            return cls(**kwargs)
        return process

    def create(self, bind=None, checkfirst=None):
        if (
            not checkfirst or
            not bind.dialect.has_type(bind, self.name, schema=self.schema)
        ):
            bind.execute(CreateCompositeType(self))

    def drop(self, bind=None, checkfirst=True):
        if (
            checkfirst and
            bind.dialect.has_type(bind, self.name, schema=self.schema)
        ):
            bind.execute(DropCompositeType(self))


def register_psycopg2_composite(dbapi_connection, composite):
    psycopg2.extras.register_composite(
        composite.name,
        dbapi_connection,
        globally=True,
        factory=composite.caster
    )

    def adapt_composite(value):
        adapted = [
            adapt(
                getattr(value, column.name)
                if not isinstance(column.type, TypeDecorator)
                else column.type.process_bind_param(
                    getattr(value, column.name),
                    PGDialect_psycopg2()
                )
            )
            for column in
            composite.columns
        ]
        for value in adapted:
            if hasattr(value, 'prepare'):
                value.prepare(dbapi_connection)
        values = [
            value.getquoted().decode(dbapi_connection.encoding)
            if six.PY3
            else value.getquoted()
            for value in adapted
        ]
        return AsIs("(%s)::%s" % (', '.join(values), composite.name))

    register_adapter(composite.type_cls, adapt_composite)


def before_create(target, connection, **kw):
    for name, composite in registered_composites.items():
        composite.create(connection, checkfirst=True)
        register_psycopg2_composite(
            connection.connection.connection,
            composite
        )


def after_drop(target, connection, **kw):
    for name, composite in registered_composites.items():
        composite.drop(connection, checkfirst=True)


def register_composites(connection):
    for name, composite in registered_composites.items():
        register_psycopg2_composite(
            connection.connection.connection,
            composite
        )


def attach_composite_listeners():
    listeners = [
        (sa.MetaData, 'before_create', before_create),
        (sa.MetaData, 'after_drop', after_drop),
    ]
    for listener in listeners:
        if not sa.event.contains(*listener):
            sa.event.listen(*listener)


def remove_composite_listeners():
    listeners = [
        (sa.MetaData, 'before_create', before_create),
        (sa.MetaData, 'after_drop', after_drop),
    ]
    for listener in listeners:
        if sa.event.contains(*listener):
            sa.event.remove(*listener)


class CreateCompositeType(_CreateDropBase):
    pass


@compiles(CreateCompositeType)
def _visit_create_composite_type(create, compiler, **kw):
    type_ = create.element
    fields = ', '.join(
        '{name} {type}'.format(
            name=column.name,
            type=compiler.dialect.type_compiler.process(
                to_instance(column.type)
            )
        )
        for column in type_.columns
    )

    return 'CREATE TYPE {name} AS ({fields})'.format(
        name=compiler.preparer.format_type(type_),
        fields=fields
    )


class DropCompositeType(_CreateDropBase):
    pass


@compiles(DropCompositeType)
def _visit_drop_composite_type(drop, compiler, **kw):
    type_ = drop.element

    return 'DROP TYPE {name}'.format(name=compiler.preparer.format_type(type_))
