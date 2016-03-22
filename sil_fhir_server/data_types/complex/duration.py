#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Duration)
#  Date: 2016-03-18.


from . import quantity


class Duration(quantity.QuantityBase):
    """ A length of time.

    There SHALL be a code if there is a value and it SHALL be an expression of
    time.  If system is present, it SHALL be UCUM.
    """

    __tablename__ = "Duration"
