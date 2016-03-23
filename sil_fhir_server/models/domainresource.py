#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DomainResource)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declared_attr

from sil_fhir_server.data_types import primitives
from . import resource


class DomainResource(resource.Resource):
    """ A resource with narrative, extensions, and contained resources.

    A resource that includes narrative, extensions, and contained resources.
    """

    __tablename__ = "DomainResource"
    __abstract__ = True

    # contained = Column(primitives.StringField,
    #                    ForeignKey('Resource.id'))
    """ Contained, inline Resources.
        List of `Resource` items (represented as `dict` in JSON). """

    @declared_attr
    def extension(cls):
        return Column(primitives.StringField, ForeignKey('Extension.id'))
    # extension = Column(primitives.StringField, ForeignKey('Extension.id'))
    """ Additional Content defined by implementations.
        List of `Extension` items (represented as `dict` in JSON). """

    @declared_attr
    def modifierExtension(cls):
        return Column(primitives.StringField, ForeignKey('Extension.id'))
    # modifierExtension = Column(primitives.StringField,
    #                            ForeignKey('Extension.id'))
    """ Extensions that cannot be ignored.
        List of `Extension` items (represented as `dict` in JSON). """

    @declared_attr
    def text(cls):
        return Column(primitives.StringField, ForeignKey('Narrative.id'))
    # text = Column(primitives.StringField,
    #               ForeignKey('Narrative.id'))
    """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """

    def __init__(self, contained, extension, modifierExtension,
                 text):
        """ Initialize all valid properties.
        """
        self.contained = contained
        self.extension = extension
        self.modifierExtension = modifierExtension
        self.text = text

    def __repr__(self):
        return '<DomainResource %r>' % 'self.property'  # replace self.property