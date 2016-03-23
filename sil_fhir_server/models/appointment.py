#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Appointment)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class AppointmentParticipant(backboneelement.BackboneElement):
    """ Participants involved in appointment.

    List of participants involved in the appointment.
    """

    __tablename__ = "AppointmentParticipant"

    # todo
    # actor = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Person, Location/HealthcareService or Device.
        Type `FHIRReference` referencing `Patient, Practitioner,
        RelatedPerson, Device, HealthcareService, Location`
        (represented as `dict` in JSON). """

    required = Column(primitives.StringField)
    """ required | optional | information-only.
        Type `str`. """

    status = Column(primitives.StringField)
    """ accepted | declined | tentative | needs-action.
        Type `str`. """

    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
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


class Appointment(domainresource.DomainResource):
    """ A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one
    or more Encounter(s).
    """

    __tablename__ = "Appointment"
    
    comment = Column(primitives.StringField)
    """ Additional comments.
        Type `str`. """
    
    description = Column(primitives.StringField)
    """ Shown on a subject line in a meeting request, or appointment list.
        Type `str`. """
    
    end = Column(primitives.DateTimeField)
    """ When appointment is to conclude.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    minutesDuration = Column(primitives.IntegerField)
    """ Can be less than start/end (e.g. estimate).
        Type `int`. """
    
    participant = Column(primitives.StringField,
                         ForeignKey('AppointmentParticipant.id'))
    """ Participants involved in appointment.
        List of `AppointmentParticipant` items (represented as `dict` in JSON). """
    
    priority = Column(primitives.IntegerField)
    """ Used to make informed decisions if needing to re-prioritize.
        Type `int`. """
    
    reason = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ Reason this appointment is scheduled.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    # todo
    # slot = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ If provided, then no schedule and start/end values MUST match slot.
        List of `FHIRReference` items referencing `Slot` (represented as `dict` in JSON). """
    
    start = Column(primitives.DateTimeField)
    """ When appointment is to take place.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    status = Column(primitives.StringField)
    """ proposed | pending | booked | arrived | fulfilled | cancelled |
        noshow.
        Type `str`. """
    
    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ The type of appointment that is being booked.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, comment, description, end, identifier,
                 minutesDuration, participant, priority, reason,
                 slot, start, status, type,):
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
