#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/AppointmentResponse)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource


class AppointmentResponse(domainresource.DomainResource):
    """ A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """

    __tablename__ = "AppointmentResponse"

    # todo
    # actor = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Person, Location/HealthcareService or Device.
        Type `FHIRReference` referencing `Patient, Practitioner,
        RelatedPerson, Device, HealthcareService, Location`
        (represented as `dict` in JSON). """

    # todo
    # appointment = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Appointment this response relates to.
        Type `FHIRReference` referencing `Appointment` (represented as `dict` in JSON). """
    
    comment = Column(primitives.StringField)
    """ Additional comments.
        Type `str`. """
    
    end = Column(primitives.DateTimeField)
    """ Time from appointment, or requested new end time.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    participantStatus = Column(primitives.StringField)
    """ accepted | declined | tentative | in-process | completed | needs-
        action.
        Type `str`. """
    
    participantType = Column(primitives.StringField,
                             ForeignKey('CodeableConcept.id'))
    """ Role of participant in the appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    start = Column(primitives.DateTimeField)
    """ Time from appointment, or requested new start time.
        Type `FHIRDate` (represented as `str` in JSON). """

    def __init__(self, actor, appointment, comment, end, identifier,
                 participantStatus, participantType, start,):
        """ Initialize all valid properties.
        """
        self.actor = actor
        self.appointment = appointment
        self.comment = comment
        self.end = end
        self.identifier = identifier
        self.participantStatus = participantStatus
        self.participantType = participantType
        self.start = start

    def __repr__(self):
        return '<AppointmentResponse %r>' % 'self.property'  # replace self.property