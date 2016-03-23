#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Quantity)
#  Date: 2016-03-18.


from sqlalchemy import Column

from sil_fhir_server.data_types import primitives
from sil_fhir_server.data_types.complex import complex_dt


class SimpleQuantityBase(complex_dt.ComplexElement):
    """ A fixed quantity (no comparator). """

    __abstract__ = True

    code = Column(primitives.StringField)
    """ Coded form of the unit.
        Type `str`. """

    system = Column(primitives.StringField)
    """ System that defines coded unit form.
        Type `str`. """

    unit = Column(primitives.StringField)
    """ Unit representation.
        Type `str`. """

    value = Column(primitives.DecimalField)
    """ Numerical value (with implicit precision).
        Type `float`. """

    def __init__(self, code, comparator, system, unit, value):
        """ Initialize all valid properties.
        """
        self.code = code
        self.comparator = comparator
        self.system = system
        self.unit = unit
        self.value = value

    def __repr__(self):
        return '<%s %r>' % (self.__class__.__name__, self.value)


class QuantityBase(SimpleQuantityBase):
    """ A measured or measurable amount.

    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """
    __abstract__ = True

    comparator = Column(primitives.StringField)
    """ < | <= | >= | > - how to understand the value.
        Type `str`. """

    def __init__(self, code, comparator, system, unit, value):
        """ Initialize all valid properties.
        """
        self.code = code
        self.comparator = comparator
        self.system = system
        self.unit = unit
        self.value = value

    def __repr__(self):
        return '<%s %r>' % (self.__class__.__name__, self.value)


class Quantity(QuantityBase):
    """ A measured or measurable amount.

    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """
    __tablename__ = 'Quantity'


class SimpleQuantity(SimpleQuantityBase):
    __tablename__ = 'SimpleQuantity'
