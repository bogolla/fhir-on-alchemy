#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Money)
#  Date: 2016-03-18.


from . import quantity

class Money(quantity.Quantity):
    """ An amount of money. With regard to precision, see [Decimal
    Precision](datatypes.html#precision).

    There SHALL be a code if there is a value and it SHALL be an expression of
    currency.  If system is present, it SHALL be ISO 4217 (system =
    "urn:iso:std:iso:4217" - currency).
    """

    __tablename__ = "Money"

    def __init__(self,):
        """ Initialize all valid properties.
        """

    def __repr__(self):
        return '<Money %r>' % 'self.property'  # replace self.property

