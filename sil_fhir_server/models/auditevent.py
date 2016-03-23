#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/AuditEvent)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class AuditEventEvent(backboneelement.BackboneElement):
    """ What was done.

    Identifies the name, action type, time, and disposition of the audited
    event.
    """

    __tablename__ = "AuditEventEvent"

    action = Column(primitives.StringField)
    """ Type of action performed during the event.
        Type `str`. """

    dateTime = Column(primitives.DateTimeField)
    """ Time when the event occurred on source.
        Type `FHIRDate` (represented as `str` in JSON). """

    outcome = Column(primitives.StringField)
    """ Whether the event succeeded or failed.
        Type `str`. """

    outcomeDesc = Column(primitives.StringField)
    """ Description of the event outcome.
        Type `str`. """

    purposeOfEvent = Column(primitives.StringField,
                            ForeignKey('Coding.id'))
    """ The purposeOfUse of the event.
        List of `Coding` items (represented as `dict` in JSON). """

    subtype = Column(primitives.StringField,
                     ForeignKey('Coding.id'))
    """ More specific type/id for the event.
        List of `Coding` items (represented as `dict` in JSON). """

    type = Column(primitives.StringField,
                  ForeignKey('Coding.id'))
    """ Type/identifier of event.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, action, dateTime, outcome, outcomeDesc,
                 purposeOfEvent, subtype, type):
        """ Initialize all valid properties.
        """
        self.action = action
        self.dateTime = dateTime
        self.outcome = outcome
        self.outcomeDesc = outcomeDesc
        self.purposeOfEvent = purposeOfEvent
        self.subtype = subtype
        self.type = type

    def __repr__(self):
        return '<AuditEventEvent %r>' % 'self.property'  # replace self.property


class AuditEventObjectDetail(backboneelement.BackboneElement):
    """ Additional Information about the Object.
    """

    __tablename__ = "AuditEventObjectDetail"

    type = Column(primitives.StringField)
    """ Name of the property.
        Type `str`. """

    value = Column(primitives.StringField)
    """ Property value.
        Type `str`. """

    def __init__(self, type, value,):
        """ Initialize all valid properties.
        """
        self.type = type
        self.value = value

    def __repr__(self):
        return '<AuditEventObjectDetail %r>' % 'self.property'  # replace self.property


class AuditEventObject(backboneelement.BackboneElement):
    """ Specific instances of data or objects that have been accessed.
    """

    __tablename__ = "AuditEventObject"

    description = Column(primitives.StringField)
    """ Descriptive text.
        Type `str`. """

    detail = Column(primitives.StringField,
                    ForeignKey('AuditEventObjectDetail.id'))
    """ Additional Information about the Object.
        List of `AuditEventObjectDetail` items (represented as `dict` in JSON). """

    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Specific instance of object (e.g. versioned).
        Type `Identifier` (represented as `dict` in JSON). """

    lifecycle = Column(primitives.StringField,
                       ForeignKey('Coding.id'))
    """ Life-cycle stage for the object.
        Type `Coding` (represented as `dict` in JSON). """

    name = Column(primitives.StringField)
    """ Instance-specific descriptor for Object.
        Type `str`. """

    query = Column(primitives.StringField)
    """ Actual query for object.
        Type `str`. """

    # todo
    # reference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Specific instance of resource (e.g. versioned).
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    role = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ What role the Object played.
        Type `Coding` (represented as `dict` in JSON). """

    securityLabel = Column(primitives.StringField,
                           ForeignKey('Coding.id'))
    """ Security labels applied to the object.
        List of `Coding` items (represented as `dict` in JSON). """

    type = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Type of object involved.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, description, detail, identifier, lifecycle,
                 name, query, reference, role, securityLabel, type,):
        """ Initialize all valid properties.
        """
        self.description = description
        self.detail = detail
        self.identifier = identifier
        self.lifecycle = lifecycle
        self.name = name
        self.query = query
        self.reference = reference
        self.role = role
        self.securityLabel = securityLabel
        self.type = type

    def __repr__(self):
        return '<AuditEventObject %r>' % 'self.property'  # replace self.property


class AuditEventParticipantNetwork(backboneelement.BackboneElement):
    """ Logical network location for application activity.

    Logical network location for application activity, if the activity has a
    network location.
    """

    __tablename__ = "AuditEventParticipantNetwork"

    address = Column(primitives.StringField)
    """ Identifier for the network access point of the user device.
        Type `str`. """

    type = Column(primitives.StringField)
    """ The type of network access point.
        Type `str`. """

    def __init__(self, address, type,):
        """ Initialize all valid properties.
        """
        self.address = address
        self.type = type

    def __repr__(self):
        return '<AuditEventParticipantNetwork %r>' % 'self.property'  # replace self.property


class AuditEventParticipant(backboneelement.BackboneElement):
    """ A person, a hardware device or software process.
    """

    __tablename__ = "AuditEventParticipant"

    altId = Column(primitives.StringField)
    """ Alternative User id e.g. authentication.
        Type `str`. """

    # todo
    # location = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Where.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """

    media = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Type of media.
        Type `Coding` (represented as `dict` in JSON). """

    name = Column(primitives.StringField)
    """ Human-meaningful name for the user.
        Type `str`. """

    network = Column(primitives.StringField,
                     ForeignKey('AuditEventParticipantNetwork.id'))
    """ Logical network location for application activity.
        Type `AuditEventParticipantNetwork` (represented as `dict` in JSON). """

    policy = Column(primitives.StringField)
    """ Policy that authorized event.
        List of `str` items. """

    purposeOfUse = Column(primitives.StringField,
                          ForeignKey('Coding.id'))
    """ Reason given for this user.
        List of `Coding` items (represented as `dict` in JSON). """

    # todo
    # reference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Direct reference to resource.
        Type `FHIRReference` referencing `Practitioner, Organization,
        Device, Patient, RelatedPerson` (represented as `dict` in JSON). """

    requestor = Column(primitives.BooleanField)
    """ Whether user is initiator.
        Type `bool`. """

    role = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ User roles (e.g. local RBAC codes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    userId = Column(primitives.StringField,
                    ForeignKey('Identifier.id'))
    """ Unique identifier for the user.
        Type `Identifier` (represented as `dict` in JSON). """

    def __init__(self, altId, location, media, name, network, policy,
                 purposeOfUse, reference, requestor, role, userId,):
        """ Initialize all valid properties.
        """
        self.altId = altId
        self.location = location
        self.media = media
        self.name = name
        self.network = network
        self.policy = policy
        self.purposeOfUse = purposeOfUse
        self.reference = reference
        self.requestor = requestor
        self.role = role
        self.userId = userId

    def __repr__(self):
        return '<AuditEventParticipant %r>' % 'self.property'  # replace self.property


class AuditEventSource(backboneelement.BackboneElement):
    """ Application systems and processes.
    """

    __tablename__ = "AuditEventSource"

    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ The identity of source detecting the event.
        Type `Identifier` (represented as `dict` in JSON). """

    site = Column(primitives.StringField)
    """ Logical source location within the enterprise.
        Type `str`. """

    type = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ The type of source where event originated.
        List of `Coding` items (represented as `dict` in JSON). """

    def __init__(self, identifier, site, type,):
        """ Initialize all valid properties.
        """
        self.identifier = identifier
        self.site = site
        self.type = type

    def __repr__(self):
        return '<AuditEventSource %r>' % 'self.property'  # replace self.property


class AuditEvent(domainresource.DomainResource):
    """ Event record kept for security purposes.

    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """

    __tablename__ = "AuditEvent"
    
    event = Column(primitives.StringField,
                   ForeignKey('AuditEventEvent.id'))
    """ What was done.
        Type `AuditEventEvent` (represented as `dict` in JSON). """
    
    object = Column(primitives.StringField,
                    ForeignKey('AuditEventObject.id'))
    """ Specific instances of data or objects that have been accessed.
        List of `AuditEventObject` items (represented as `dict` in JSON). """
    
    participant = Column(primitives.StringField,
                         ForeignKey('AuditEventParticipant.id'))
    """ A person, a hardware device or software process.
        List of `AuditEventParticipant` items (represented as `dict` in JSON). """
    
    source = Column(primitives.StringField,
                    ForeignKey('AuditEventSource.id'))
    """ Application systems and processes.
        Type `AuditEventSource` (represented as `dict` in JSON). """

    def __init__(self, event, object, participant, source,):
        """ Initialize all valid properties.
        """
        self.event = event
        self.object = object
        self.participant = participant
        self.source = source

    def __repr__(self):
        return '<AuditEvent %r>' % 'self.property'  # replace self.property
