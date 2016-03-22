#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/AuditEvent)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer
from sil_fhir_server.data_types import primitives
from . import domainresource

class AuditEvent(domainresource.DomainResource):
    """ Event record kept for security purposes.

    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """

    __tablename__ = "AuditEvent"

    event = Column(AuditEventEvent)
    """ What was done.
        Type `AuditEventEvent` (represented as `dict` in JSON). """

    object = Column(AuditEventObject)
    """ Specific instances of data or objects that have been accessed.
        List of `AuditEventObject` items (represented as `dict` in JSON). """

    participant = Column(AuditEventParticipant)
    """ A person, a hardware device or software process.
        List of `AuditEventParticipant` items (represented as `dict` in JSON). """

    source = Column(AuditEventSource)
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


from sqlalchemy import Column, Integer, String
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

    dateTime = Column(FHIRDate)
    """ Time when the event occurred on source.
        Type `FHIRDate` (represented as `str` in JSON). """

    outcome = Column(primitives.StringField)
    """ Whether the event succeeded or failed.
        Type `str`. """

    outcomeDesc = Column(primitives.StringField)
    """ Description of the event outcome.
        Type `str`. """

    purposeOfEvent = Column(Coding)
    """ The purposeOfUse of the event.
        List of `Coding` items (represented as `dict` in JSON). """

    subtype = Column(Coding)
    """ More specific type/id for the event.
        List of `Coding` items (represented as `dict` in JSON). """

    type = Column(Coding)
    """ Type/identifier of event.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, action, dateTime, outcome, outcomeDesc, purposeOfEvent, subtype, type,):
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


from sqlalchemy import Column, Integer, String
class AuditEventObject(backboneelement.BackboneElement):
    """ Specific instances of data or objects that have been accessed.
    """

    __tablename__ = "AuditEventObject"

    description = Column(primitives.StringField)
    """ Descriptive text.
        Type `str`. """

    detail = Column(AuditEventObjectDetail)
    """ Additional Information about the Object.
        List of `AuditEventObjectDetail` items (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Specific instance of object (e.g. versioned).
        Type `Identifier` (represented as `dict` in JSON). """

    lifecycle = Column(Coding)
    """ Life-cycle stage for the object.
        Type `Coding` (represented as `dict` in JSON). """

    name = Column(primitives.StringField)
    """ Instance-specific descriptor for Object.
        Type `str`. """

    query = Column(primitives.StringField)
    """ Actual query for object.
        Type `str`. """

    reference = Column(FHIRReference)
    """ Specific instance of resource (e.g. versioned).
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    role = Column(Coding)
    """ What role the Object played.
        Type `Coding` (represented as `dict` in JSON). """

    securityLabel = Column(Coding)
    """ Security labels applied to the object.
        List of `Coding` items (represented as `dict` in JSON). """

    type = Column(Coding)
    """ Type of object involved.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, description, detail, identifier, lifecycle, name, query, reference, role, securityLabel, type,):
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


from sqlalchemy import Column, Integer, String
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


from sqlalchemy import Column, Integer, String
class AuditEventParticipant(backboneelement.BackboneElement):
    """ A person, a hardware device or software process.
    """

    __tablename__ = "AuditEventParticipant"

    altId = Column(primitives.StringField)
    """ Alternative User id e.g. authentication.
        Type `str`. """

    location = Column(FHIRReference)
    """ Where.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """

    media = Column(Coding)
    """ Type of media.
        Type `Coding` (represented as `dict` in JSON). """

    name = Column(primitives.StringField)
    """ Human-meaningful name for the user.
        Type `str`. """

    network = Column(AuditEventParticipantNetwork)
    """ Logical network location for application activity.
        Type `AuditEventParticipantNetwork` (represented as `dict` in JSON). """

    policy = Column(primitives.StringField)
    """ Policy that authorized event.
        List of `str` items. """

    purposeOfUse = Column(Coding)
    """ Reason given for this user.
        List of `Coding` items (represented as `dict` in JSON). """

    reference = Column(FHIRReference)
    """ Direct reference to resource.
        Type `FHIRReference` referencing `Practitioner, Organization, Device, Patient, RelatedPerson` (represented as `dict` in JSON). """

    requestor = Column(bool)
    """ Whether user is initiator.
        Type `bool`. """

    role = Column(CodeableConcept)
    """ User roles (e.g. local RBAC codes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    userId = Column(Identifier)
    """ Unique identifier for the user.
        Type `Identifier` (represented as `dict` in JSON). """

    def __init__(self, altId, location, media, name, network, policy, purposeOfUse, reference, requestor, role, userId,):
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


from sqlalchemy import Column, Integer, String
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


from sqlalchemy import Column, Integer, String
class AuditEventSource(backboneelement.BackboneElement):
    """ Application systems and processes.
    """

    __tablename__ = "AuditEventSource"

    identifier = Column(Identifier)
    """ The identity of source detecting the event.
        Type `Identifier` (represented as `dict` in JSON). """

    site = Column(primitives.StringField)
    """ Logical source location within the enterprise.
        Type `str`. """

    type = Column(Coding)
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


from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier