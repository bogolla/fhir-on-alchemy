#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/CommunicationRequest)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class CommunicationRequestPayload(backboneelement.BackboneElement):
    """ Message payload.

    Text, attachment(s), or resource(s) to be communicated to the recipient.
    """

    __tablename__ = "CommunicationRequestPayload"

    contentAttachment = Column(primitives.StringField,
                               ForeignKey('Attachment.id'))
    """ Message part content.
        Type `Attachment` (represented as `dict` in JSON). """

    # todo contentReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    contentReference = Column(primitives.StringField)
    """ Message part content.
        Type `FHIRReference` referencing `Resource`
        (represented as `dict` in JSON). """

    contentString = Column(primitives.StringField)
    """ Message part content.
        Type `str`. """

    def __init__(self, contentAttachment, contentReference,
                 contentString,):
        """ Initialize all valid properties.
        """
        self.contentAttachment = contentAttachment
        self.contentReference = contentReference
        self.contentString = contentString

    def __repr__(self):
        return '<CommunicationRequestPayload %r>' % 'self.property'  # replace self.property


class CommunicationRequest(domainresource.DomainResource):
    """ A request for information to be sent to a receiver.

    A request to convey information; e.g. the CDS system proposes that an alert
    be sent to a responsible provider, the CDS system proposes that the public
    health agency be notified about a reportable condition.
    """

    __tablename__ = "CommunicationRequest"
    
    category = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Message category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ Encounter leading to message.
        Type `FHIRReference` referencing `Encounter`
        (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    medium = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ A channel of communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    payload = Column(primitives.StringField,
                     ForeignKey('CommunicationRequestPayload.id'))
    """ Message payload.
        List of `CommunicationRequestPayload` items
        (represented as `dict` in JSON). """
    
    priority = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Message urgency.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    reason = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ Indication for message.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    # todo recipient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    recipient = Column(primitives.StringField)
    """ Message recipient.
        List of `FHIRReference` items referencing `Device,
        Organization, Patient, Practitioner, RelatedPerson`
        (represented as `dict` in JSON). """
    
    requestedOn = Column(primitives.DateTimeField)
    """ When ordered or proposed.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    # todo requester = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    requester = Column(primitives.StringField)
    """ An individual who requested a communication.
        Type `FHIRReference` referencing `Practitioner,
        Patient, RelatedPerson` (represented as `dict` in JSON). """
    
    scheduledDateTime = Column(primitives.DateTimeField)
    """ When scheduled.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    scheduledPeriod = Column(primitives.StringField,
                             ForeignKey('Period.id'))
    """ When scheduled.
        Type `Period` (represented as `dict` in JSON). """
    
    # todo sender = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    sender = Column(primitives.StringField)
    """ Message sender.
        Type `FHIRReference` referencing `Device, Organization,
        Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ proposed | planned | requested | received | accepted | in-progress
        | completed | suspended | rejected | failed.
        Type `str`. """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Focus of message.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    def __init__(self, category, encounter, identifier, medium,
                 payload, priority, reason, recipient, requestedOn,
                 requester, scheduledDateTime, scheduledPeriod,
                 sender, status, subject,):
        """ Initialize all valid properties.
        """
        self.category = category
        self.encounter = encounter
        self.identifier = identifier
        self.medium = medium
        self.payload = payload
        self.priority = priority
        self.reason = reason
        self.recipient = recipient
        self.requestedOn = requestedOn
        self.requester = requester
        self.scheduledDateTime = scheduledDateTime
        self.scheduledPeriod = scheduledPeriod
        self.sender = sender
        self.status = status
        self.subject = subject

    def __repr__(self):
        return '<CommunicationRequest %r>' % 'self.property'  # replace self.property
