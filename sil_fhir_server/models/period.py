#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Period)
#  Date: 2016-03-18.


from . import element

class Period(element.Element):
    """ Time range defined by start and end date/time.

    A time period defined by a start and end date and optionally time.
    """

    __tablename__ = "Period"

    end = Column()
    """ End time with inclusive boundary, if not ongoing.
        Type `FHIRDate` (represented as `str` in JSON). """

    start = Column()
    """ Starting time with inclusive boundary.
        Type `FHIRDate` (represented as `str` in JSON). """

    def __init__(self, end, start,):
        """ Initialize all valid properties.
        """
        self.end = end
        self.start = start

    def __repr__(self):
        return '<Period %r>' % 'self.property'  # replace self.property


from . import fhirdate