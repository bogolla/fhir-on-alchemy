#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Slot)
#  Date: 2016-03-18.


from . import domainresource

class Slot(domainresource.DomainResource):
    """ A slot of time on a schedule that may be available for booking appointments.
    """

    __tablename__ = "Slot"

    comment = Column()
    """ Comments on the slot to describe any extended information. Such as
        custom constraints on the slot.
        Type `str`. """

    end = Column()
    """ Date/Time that the slot is to conclude.
        Type `FHIRDate` (represented as `str` in JSON). """

    freeBusyType = Column()
    """ busy | free | busy-unavailable | busy-tentative.
        Type `str`. """

    identifier = Column(Identifier)
    """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """

    overbooked = Column()
    """ This slot has already been overbooked, appointments are unlikely to
        be accepted for this time.
        Type `bool`. """

    schedule = Column()
    """ The schedule resource that this slot defines an interval of status
        information.
        Type `FHIRReference` referencing `Schedule` (represented as `dict` in JSON). """

    start = Column()
    """ Date/Time that the slot is to begin.
        Type `FHIRDate` (represented as `str` in JSON). """

    type = Column()
    """ The type of appointments that can be booked into this slot (ideally
        this would be an identifiable service - which is at a location,
        rather than the location itself). If provided then this overrides
        the value provided on the availability resource.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, comment, end, freeBusyType, identifier, overbooked, schedule, start, type,):
        """ Initialize all valid properties.
        """
        self.comment = comment
        self.end = end
        self.freeBusyType = freeBusyType
        self.identifier = identifier
        self.overbooked = overbooked
        self.schedule = schedule
        self.start = start
        self.type = type

    def __repr__(self):
        return '<Slot %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier