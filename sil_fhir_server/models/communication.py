#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Communication)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class CommunicationPayload(backboneelement.BackboneElement):
    """ Message payload.

    Text, attachment(s), or resource(s) that was communicated to the recipient.
    """

    __tablename__ = "CommunicationPayload"

    contentAttachment = Column(primitives.StringField, ForeignKey('Attachment.id'))
    """ Message part content.
        Type `Attachment` (represented as `dict` in JSON). """

    # todo contentReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    contentReference = Column(primitives.StringField)
    """ Message part content.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    contentString = Column(primitives.StringField)
    """ Message part content.
        Type `str`. """

    def __init__(self, contentAttachment, contentReference, contentString,):
        """ Initialize all valid properties.
        """
        self.contentAttachment = contentAttachment
        self.contentReference = contentReference
        self.contentString = contentString

    def __repr__(self):
        return '<CommunicationPayload %r>' % 'self.property'  # replace self.property


class Communication(domainresource.DomainResource):
    """ A record of information transmitted from a sender to a receiver.

    An occurrence of information being transmitted; e.g. an alert that was sent
    to a responsible provider, a public health agency was notified about a
    reportable condition.
    """

    __tablename__ = "Communication"
    
    category = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Message category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo encounter = Column(primitives.StringField,
    #                    ForeignKey('FHIRReference.id'))
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
                     ForeignKey('CommunicationPayload.id'))
    """ Message payload.
        List of `CommunicationPayload` items
        (represented as `dict` in JSON). """
    
    reason = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ Indication for message.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    received = Column(primitives.DateTimeField)
    """ When received.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    # todo recipient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    recipient = Column(primitives.StringField)
    """ Message recipient.
        List of `FHIRReference` items referencing `Device,
        Organization, Patient, Practitioner, RelatedPerson,
        Group` (represented as `dict` in JSON). """
    
    # todo requestDetail = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    requestDetail = Column(primitives.StringField)
    """ CommunicationRequest producing this message.
        Type `FHIRReference` referencing `CommunicationRequest`
        (represented as `dict` in JSON). """
    
    # todo sender = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    sender = Column(primitives.StringField)
    """ Message sender.
        Type `FHIRReference` referencing `Device, Organization,
        Patient, Practitioner, RelatedPerson`
        (represented as `dict` in JSON). """
    
    sent = Column(primitives.DateTimeField)
    """ When sent.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    status = Column(primitives.StringField)
    """ in-progress | completed | suspended | rejected | failed.
        Type `str`. """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Focus of message.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    def __init__(self, category, encounter, identifier,
                 medium, payload, reason, received, recipient,
                 requestDetail, sender, sent, status, subject,):
        """ Initialize all valid properties.
        """
        self.category = category
        self.encounter = encounter
        self.identifier = identifier
        self.medium = medium
        self.payload = payload
        self.reason = reason
        self.received = received
        self.recipient = recipient
        self.requestDetail = requestDetail
        self.sender = sender
        self.sent = sent
        self.status = status
        self.subject = subject

    def __repr__(self):
        return '<Communication %r>' % 'self.property'  # replace self.property
