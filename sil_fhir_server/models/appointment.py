#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Appointment)
#  Date: 2016-03-18.


from . import domainresource

class Appointment(domainresource.DomainResource):
    """ A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one
    or more Encounter(s).
    """

    __tablename__ = "Appointment"

    comment = Column()
    """ Additional comments.
        Type `str`. """

    description = Column()
    """ Shown on a subject line in a meeting request, or appointment list.
        Type `str`. """

    end = Column()
    """ When appointment is to conclude.
        Type `FHIRDate` (represented as `str` in JSON). """

    identifier = Column(Identifier)
    """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """

    minutesDuration = Column()
    """ Can be less than start/end (e.g. estimate).
        Type `int`. """

    participant = Column(AppointmentParticipant)
    """ Participants involved in appointment.
        List of `AppointmentParticipant` items (represented as `dict` in JSON). """

    priority = Column()
    """ Used to make informed decisions if needing to re-prioritize.
        Type `int`. """

    reason = Column()
    """ Reason this appointment is scheduled.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    slot = Column(FHIRReference)
    """ If provided, then no schedule and start/end values MUST match slot.
        List of `FHIRReference` items referencing `Slot` (represented as `dict` in JSON). """

    start = Column()
    """ When appointment is to take place.
        Type `FHIRDate` (represented as `str` in JSON). """

    status = Column()
    """ proposed | pending | booked | arrived | fulfilled | cancelled |
        noshow.
        Type `str`. """

    type = Column()
    """ The type of appointment that is being booked.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, comment, description, end, identifier, minutesDuration, participant, priority, reason, slot, start, status, type,):
        """ Initialize all valid properties.
        """
        self.comment = comment
        self.description = description
        self.end = end
        self.identifier = identifier
        self.minutesDuration = minutesDuration
        self.participant = participant
        self.priority = priority
        self.reason = reason
        self.slot = slot
        self.start = start
        self.status = status
        self.type = type

    def __repr__(self):
        return '<Appointment %r>' % 'self.property'  # replace self.property


from . import backboneelement

class AppointmentParticipant(backboneelement.BackboneElement):
    """ Participants involved in appointment.

    List of participants involved in the appointment.
    """

    __tablename__ = "AppointmentParticipant"

    actor = Column()
    """ Person, Location/HealthcareService or Device.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson, Device, HealthcareService, Location` (represented as `dict` in JSON). """

    required = Column()
    """ required | optional | information-only.
        Type `str`. """

    status = Column()
    """ accepted | declined | tentative | needs-action.
        Type `str`. """

    type = Column(CodeableConcept)
    """ Role of participant in the appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, actor, required, status, type,):
        """ Initialize all valid properties.
        """
        self.actor = actor
        self.required = required
        self.status = status
        self.type = type

    def __repr__(self):
        return '<AppointmentParticipant %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier