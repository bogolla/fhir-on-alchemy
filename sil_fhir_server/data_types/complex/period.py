#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Period)
#  Date: 2016-03-18.


from sqlalchemy import Column

from sil_fhir_server.data_types import primitives
from . import complex_dt


class Period(complex_dt.ComplexElement):
    """ Time range defined by start and end date/time.

    A time period defined by a start and end date and optionally time.
    """

    __tablename__ = "Period"
    
    end = Column(primitives.DateTimeField)
    """ End time with inclusive boundary, if not ongoing.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    start = Column(primitives.DateTimeField)
    """ Starting time with inclusive boundary.
        Type `FHIRDate` (represented as `str` in JSON). """

    def __init__(self, end, start):
        """ Initialize all valid properties.
        """
        self.end = end
        self.start = start

    def __repr__(self):
        return '<Period %r-%r>' % (self.start, self.end)
