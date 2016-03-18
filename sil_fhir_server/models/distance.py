#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Distance)
#  Date: 2016-03-18.


from . import quantity

class Distance(quantity.Quantity):
    """ A measure of distance.

    There SHALL be a code if there is a value and it SHALL be an expression of
    length.  If system is present, it SHALL be UCUM.
    """

    __tablename__ = "Distance"

    def __init__(self,):
        """ Initialize all valid properties.
        """

    def __repr__(self):
        return '<Distance %r>' % 'self.property'  # replace self.property

