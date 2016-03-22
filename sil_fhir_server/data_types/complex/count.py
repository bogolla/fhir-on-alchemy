#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Count)
#  Date: 2016-03-18.


from . import quantity


class Count(quantity.QuantityBase):
    """ A count of a discrete element (no unit).

    There SHALL be a code with a value of "1" if there is a value and it SHALL
    be an expression of length.  If system is present, it SHALL be UCUM.  If
    present, the value SHALL a whole number.
    """

    __tablename__ = "Count"
