#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Quantity)
#  Date: 2016-03-18.


from . import element

class Quantity(element.Element):
    """ A measured or measurable amount.

    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """

    __tablename__ = "Quantity"

    code = Column()
    """ Coded form of the unit.
        Type `str`. """

    comparator = Column()
    """ < | <= | >= | > - how to understand the value.
        Type `str`. """

    system = Column()
    """ System that defines coded unit form.
        Type `str`. """

    unit = Column()
    """ Unit representation.
        Type `str`. """

    value = Column()
    """ Numerical value (with implicit precision).
        Type `float`. """

    def __init__(self, code, comparator, system, unit, value,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.comparator = comparator
        self.system = system
        self.unit = unit
        self.value = value

    def __repr__(self):
        return '<Quantity %r>' % 'self.property'  # replace self.property

