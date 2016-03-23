#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/MessageHeader)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource

class MessageHeader(domainresource.DomainResource):
    """ A resource that describes a message that is exchanged between systems.

    The header for a message exchange that is either requesting or responding
    to an action.  The reference(s) that are the subject of the action as well
    as other information related to the action are typically transmitted in a
    bundle in which the MessageHeader resource instance is the first resource
    in the bundle.
    """

    __tablename__ = "MessageHeader"
    
    author = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ The source of the decision.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    data = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ The actual content of the message.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
    
    destination = Column(primitives.StringField, ForeignKey('MessageHeaderDestination.id'))
    """ Message Destination Application(s).
        List of `MessageHeaderDestination` items (represented as `dict` in JSON). """
    
    enterer = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ The source of the data entry.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    event = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Code for the event this message represents.
        Type `Coding` (represented as `dict` in JSON). """
    
    reason = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ Cause of event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    receiver = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Intended "real-world" recipient for the data.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """
    
    response = Column(primitives.StringField, ForeignKey('MessageHeaderResponse.id'))
    """ If this is a reply to prior message.
        Type `MessageHeaderResponse` (represented as `dict` in JSON). """
    
    responsible = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Final responsibility for event.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """
    
    source = Column(primitives.StringField, ForeignKey('MessageHeaderSource.id'))
    """ Message Source Application.
        Type `MessageHeaderSource` (represented as `dict` in JSON). """
    
    timestamp = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ Time that the message was sent.
        Type `FHIRDate` (represented as `str` in JSON). """

    def __init__(self, author, data, destination, enterer, event, reason, receiver, response, responsible, source, timestamp,):
        """ Initialize all valid properties.
        """
        self.author = author
        self.data = data
        self.destination = destination
        self.enterer = enterer
        self.event = event
        self.reason = reason
        self.receiver = receiver
        self.response = response
        self.responsible = responsible
        self.source = source
        self.timestamp = timestamp

    def __repr__(self):
        return '<MessageHeader %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import backboneelement

class MessageHeaderDestination(backboneelement.BackboneElement):
    """ Message Destination Application(s).

    The destination application which the message is intended for.
    """

    __tablename__ = "MessageHeaderDestination"
    
    endpoint = Column(primitives.StringField)
    """ Actual destination address or id.
        Type `str`. """
    
    name = Column(primitives.StringField)
    """ Name of system.
        Type `str`. """
    
    target = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Particular delivery destination within the destination.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """

    def __init__(self, endpoint, name, target,):
        """ Initialize all valid properties.
        """
        self.endpoint = endpoint
        self.name = name
        self.target = target

    def __repr__(self):
        return '<MessageHeaderDestination %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
class MessageHeaderResponse(backboneelement.BackboneElement):
    """ If this is a reply to prior message.

    Information about the message that this message is a response to.  Only
    present if this message is a response.
    """

    __tablename__ = "MessageHeaderResponse"
    
    code = Column(primitives.StringField)
    """ ok | transient-error | fatal-error.
        Type `str`. """
    
    details = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Specific list of hints/warnings/errors.
        Type `FHIRReference` referencing `OperationOutcome` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField)
    """ Id of original message.
        Type `str`. """

    def __init__(self, code, details, identifier,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.details = details
        self.identifier = identifier

    def __repr__(self):
        return '<MessageHeaderResponse %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
class MessageHeaderSource(backboneelement.BackboneElement):
    """ Message Source Application.

    The source application from which this message originated.
    """

    __tablename__ = "MessageHeaderSource"
    
    contact = Column(primitives.StringField, ForeignKey('ContactPoint.id'))
    """ Human contact for problems.
        Type `ContactPoint` (represented as `dict` in JSON). """
    
    endpoint = Column(primitives.StringField)
    """ Actual message source address or id.
        Type `str`. """
    
    name = Column(primitives.StringField)
    """ Name of system.
        Type `str`. """
    
    software = Column(primitives.StringField)
    """ Name of software running the system.
        Type `str`. """
    
    version = Column(primitives.StringField)
    """ Version of software running.
        Type `str`. """

    def __init__(self, contact, endpoint, name, software, version,):
        """ Initialize all valid properties.
        """
        self.contact = contact
        self.endpoint = endpoint
        self.name = name
        self.software = software
        self.version = version

    def __repr__(self):
        return '<MessageHeaderSource %r>' % 'self.property'  # replace self.property