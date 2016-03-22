#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Conformance)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer
from sil_fhir_server.data_types import primitives
from . import domainresource

class Conformance(domainresource.DomainResource):
    """ A conformance statement.

    A conformance statement is a set of capabilities of a FHIR Server that may
    be used as a statement of actual server functionality or a statement of
    required or desired server implementation.
    """

    __tablename__ = "Conformance"

    acceptUnknown = Column(primitives.StringField)
    """ no | extensions | elements | both.
        Type `str`. """

    contact = Column(ConformanceContact)
    """ Contact details of the publisher.
        List of `ConformanceContact` items (represented as `dict` in JSON). """

    copyright = Column(primitives.StringField)
    """ Use and/or publishing restrictions.
        Type `str`. """

    date = Column(FHIRDate)
    """ Publication Date(/time).
        Type `FHIRDate` (represented as `str` in JSON). """

    description = Column(primitives.StringField)
    """ Human description of the conformance statement.
        Type `str`. """

    document = Column(ConformanceDocument)
    """ Document definition.
        List of `ConformanceDocument` items (represented as `dict` in JSON). """

    experimental = Column(bool)
    """ If for testing purposes, not real usage.
        Type `bool`. """

    fhirVersion = Column(primitives.StringField)
    """ FHIR Version the system uses.
        Type `str`. """

    format = Column(primitives.StringField)
    """ formats supported (xml | json | mime type).
        List of `str` items. """

    implementation = Column(ConformanceImplementation)
    """ If this describes a specific instance.
        Type `ConformanceImplementation` (represented as `dict` in JSON). """

    kind = Column(primitives.StringField)
    """ instance | capability | requirements.
        Type `str`. """

    messaging = Column(ConformanceMessaging)
    """ If messaging is supported.
        List of `ConformanceMessaging` items (represented as `dict` in JSON). """

    name = Column(primitives.StringField)
    """ Informal name for this conformance statement.
        Type `str`. """

    profile = Column(FHIRReference)
    """ Profiles for use cases supported.
        List of `FHIRReference` items referencing `StructureDefinition` (represented as `dict` in JSON). """

    publisher = Column(primitives.StringField)
    """ Name of the publisher (Organization or individual).
        Type `str`. """

    requirements = Column(primitives.StringField)
    """ Why is this needed?.
        Type `str`. """

    rest = Column(ConformanceRest)
    """ If the endpoint is a RESTful one.
        List of `ConformanceRest` items (represented as `dict` in JSON). """

    software = Column(ConformanceSoftware)
    """ Software that is covered by this conformance statement.
        Type `ConformanceSoftware` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ draft | active | retired.
        Type `str`. """

    url = Column(primitives.StringField)
    """ Logical uri to reference this statement.
        Type `str`. """

    version = Column(primitives.StringField)
    """ Logical id for this version of the statement.
        Type `str`. """

    def __init__(self, acceptUnknown, contact, copyright, date, description, document, experimental, fhirVersion, format, implementation, kind, messaging, name, profile, publisher, requirements, rest, software, status, url, version,):
        """ Initialize all valid properties.
        """
        self.acceptUnknown = acceptUnknown
        self.contact = contact
        self.copyright = copyright
        self.date = date
        self.description = description
        self.document = document
        self.experimental = experimental
        self.fhirVersion = fhirVersion
        self.format = format
        self.implementation = implementation
        self.kind = kind
        self.messaging = messaging
        self.name = name
        self.profile = profile
        self.publisher = publisher
        self.requirements = requirements
        self.rest = rest
        self.software = software
        self.status = status
        self.url = url
        self.version = version

    def __repr__(self):
        return '<Conformance %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class ConformanceContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    __tablename__ = "ConformanceContact"

    name = Column(primitives.StringField)
    """ Name of a individual to contact.
        Type `str`. """

    telecom = Column(ContactPoint)
    """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, name, telecom,):
        """ Initialize all valid properties.
        """
        self.name = name
        self.telecom = telecom

    def __repr__(self):
        return '<ConformanceContact %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConformanceDocument(backboneelement.BackboneElement):
    """ Document definition.

    A document definition.
    """

    __tablename__ = "ConformanceDocument"

    documentation = Column(primitives.StringField)
    """ Description of document support.
        Type `str`. """

    mode = Column(primitives.StringField)
    """ producer | consumer.
        Type `str`. """

    profile = Column(FHIRReference)
    """ Constraint on a resource used in the document.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """

    def __init__(self, documentation, mode, profile,):
        """ Initialize all valid properties.
        """
        self.documentation = documentation
        self.mode = mode
        self.profile = profile

    def __repr__(self):
        return '<ConformanceDocument %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConformanceImplementation(backboneelement.BackboneElement):
    """ If this describes a specific instance.

    Identifies a specific implementation instance that is described by the
    conformance statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """

    __tablename__ = "ConformanceImplementation"

    description = Column(primitives.StringField)
    """ Describes this specific instance.
        Type `str`. """

    url = Column(primitives.StringField)
    """ Base URL for the installation.
        Type `str`. """

    def __init__(self, description, url,):
        """ Initialize all valid properties.
        """
        self.description = description
        self.url = url

    def __repr__(self):
        return '<ConformanceImplementation %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConformanceMessaging(backboneelement.BackboneElement):
    """ If messaging is supported.

    A description of the messaging capabilities of the solution.
    """

    __tablename__ = "ConformanceMessaging"

    documentation = Column(primitives.StringField)
    """ Messaging interface behavior details.
        Type `str`. """

    endpoint = Column(ConformanceMessagingEndpoint)
    """ A messaging service end-point.
        List of `ConformanceMessagingEndpoint` items (represented as `dict` in JSON). """

    event = Column(ConformanceMessagingEvent)
    """ Declare support for this event.
        List of `ConformanceMessagingEvent` items (represented as `dict` in JSON). """

    reliableCache = Column(Integer)
    """ Reliable Message Cache Length (min).
        Type `int`. """

    def __init__(self, documentation, endpoint, event, reliableCache,):
        """ Initialize all valid properties.
        """
        self.documentation = documentation
        self.endpoint = endpoint
        self.event = event
        self.reliableCache = reliableCache

    def __repr__(self):
        return '<ConformanceMessaging %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConformanceMessagingEndpoint(backboneelement.BackboneElement):
    """ A messaging service end-point.

    An endpoint (network accessible address) to which messages and/or replies
    are to be sent.
    """

    __tablename__ = "ConformanceMessagingEndpoint"

    address = Column(primitives.StringField)
    """ Address of end-point.
        Type `str`. """

    protocol = Column(Coding)
    """ http | ftp | mllp +.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, address, protocol,):
        """ Initialize all valid properties.
        """
        self.address = address
        self.protocol = protocol

    def __repr__(self):
        return '<ConformanceMessagingEndpoint %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConformanceMessagingEvent(backboneelement.BackboneElement):
    """ Declare support for this event.

    A description of the solution's support for an event at this end-point.
    """

    __tablename__ = "ConformanceMessagingEvent"

    category = Column(primitives.StringField)
    """ Consequence | Currency | Notification.
        Type `str`. """

    code = Column(Coding)
    """ Event type.
        Type `Coding` (represented as `dict` in JSON). """

    documentation = Column(primitives.StringField)
    """ Endpoint-specific event documentation.
        Type `str`. """

    focus = Column(primitives.StringField)
    """ Resource that's focus of message.
        Type `str`. """

    mode = Column(primitives.StringField)
    """ sender | receiver.
        Type `str`. """

    request = Column(FHIRReference)
    """ Profile that describes the request.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """

    response = Column(FHIRReference)
    """ Profile that describes the response.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """

    def __init__(self, category, code, documentation, focus, mode, request, response,):
        """ Initialize all valid properties.
        """
        self.category = category
        self.code = code
        self.documentation = documentation
        self.focus = focus
        self.mode = mode
        self.request = request
        self.response = response

    def __repr__(self):
        return '<ConformanceMessagingEvent %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConformanceRest(backboneelement.BackboneElement):
    """ If the endpoint is a RESTful one.

    A definition of the restful capabilities of the solution, if any.
    """

    __tablename__ = "ConformanceRest"

    compartment = Column(primitives.StringField)
    """ Compartments served/used by system.
        List of `str` items. """

    documentation = Column(primitives.StringField)
    """ General description of implementation.
        Type `str`. """

    interaction = Column(ConformanceRestInteraction)
    """ What operations are supported?.
        List of `ConformanceRestInteraction` items (represented as `dict` in JSON). """

    mode = Column(primitives.StringField)
    """ client | server.
        Type `str`. """

    operation = Column(ConformanceRestOperation)
    """ Definition of an operation or a custom query.
        List of `ConformanceRestOperation` items (represented as `dict` in JSON). """

    resource = Column(ConformanceRestResource)
    """ Resource served on the REST interface.
        List of `ConformanceRestResource` items (represented as `dict` in JSON). """

    searchParam = Column(ConformanceRestResourceSearchParam)
    """ Search params for searching all resources.
        List of `ConformanceRestResourceSearchParam` items (represented as `dict` in JSON). """

    security = Column(ConformanceRestSecurity)
    """ Information about security of implementation.
        Type `ConformanceRestSecurity` (represented as `dict` in JSON). """

    transactionMode = Column(primitives.StringField)
    """ not-supported | batch | transaction | both.
        Type `str`. """

    def __init__(self, compartment, documentation, interaction, mode, operation, resource, searchParam, security, transactionMode,):
        """ Initialize all valid properties.
        """
        self.compartment = compartment
        self.documentation = documentation
        self.interaction = interaction
        self.mode = mode
        self.operation = operation
        self.resource = resource
        self.searchParam = searchParam
        self.security = security
        self.transactionMode = transactionMode

    def __repr__(self):
        return '<ConformanceRest %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConformanceRestInteraction(backboneelement.BackboneElement):
    """ What operations are supported?.

    A specification of restful operations supported by the system.
    """

    __tablename__ = "ConformanceRestInteraction"

    code = Column(primitives.StringField)
    """ transaction | search-system | history-system.
        Type `str`. """

    documentation = Column(primitives.StringField)
    """ Anything special about operation behavior.
        Type `str`. """

    def __init__(self, code, documentation,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.documentation = documentation

    def __repr__(self):
        return '<ConformanceRestInteraction %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConformanceRestOperation(backboneelement.BackboneElement):
    """ Definition of an operation or a custom query.

    Definition of an operation or a named query and with its parameters and
    their meaning and type.
    """

    __tablename__ = "ConformanceRestOperation"

    definition = Column(FHIRReference)
    """ The defined operation/query.
        Type `FHIRReference` referencing `OperationDefinition` (represented as `dict` in JSON). """

    name = Column(primitives.StringField)
    """ Name by which the operation/query is invoked.
        Type `str`. """

    def __init__(self, definition, name,):
        """ Initialize all valid properties.
        """
        self.definition = definition
        self.name = name

    def __repr__(self):
        return '<ConformanceRestOperation %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConformanceRestResource(backboneelement.BackboneElement):
    """ Resource served on the REST interface.

    A specification of the restful capabilities of the solution for a specific
    resource type.
    """

    __tablename__ = "ConformanceRestResource"

    conditionalCreate = Column(bool)
    """ If allows/uses conditional create.
        Type `bool`. """

    conditionalDelete = Column(primitives.StringField)
    """ not-supported | single | multiple - how conditional delete is
        supported.
        Type `str`. """

    conditionalUpdate = Column(bool)
    """ If allows/uses conditional update.
        Type `bool`. """

    interaction = Column(ConformanceRestResourceInteraction)
    """ What operations are supported?.
        List of `ConformanceRestResourceInteraction` items (represented as `dict` in JSON). """

    profile = Column(FHIRReference)
    """ Base System profile for all uses of resource.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """

    readHistory = Column(bool)
    """ Whether vRead can return past versions.
        Type `bool`. """

    searchInclude = Column(primitives.StringField)
    """ _include values supported by the server.
        List of `str` items. """

    searchParam = Column(ConformanceRestResourceSearchParam)
    """ Search params supported by implementation.
        List of `ConformanceRestResourceSearchParam` items (represented as `dict` in JSON). """

    searchRevInclude = Column(primitives.StringField)
    """ _revinclude values supported by the server.
        List of `str` items. """

    type = Column(primitives.StringField)
    """ A resource type that is supported.
        Type `str`. """

    updateCreate = Column(bool)
    """ If update can commit to a new identity.
        Type `bool`. """

    versioning = Column(primitives.StringField)
    """ no-version | versioned | versioned-update.
        Type `str`. """

    def __init__(self, conditionalCreate, conditionalDelete, conditionalUpdate, interaction, profile, readHistory, searchInclude, searchParam, searchRevInclude, type, updateCreate, versioning,):
        """ Initialize all valid properties.
        """
        self.conditionalCreate = conditionalCreate
        self.conditionalDelete = conditionalDelete
        self.conditionalUpdate = conditionalUpdate
        self.interaction = interaction
        self.profile = profile
        self.readHistory = readHistory
        self.searchInclude = searchInclude
        self.searchParam = searchParam
        self.searchRevInclude = searchRevInclude
        self.type = type
        self.updateCreate = updateCreate
        self.versioning = versioning

    def __repr__(self):
        return '<ConformanceRestResource %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConformanceRestResourceInteraction(backboneelement.BackboneElement):
    """ What operations are supported?.

    Identifies a restful operation supported by the solution.
    """

    __tablename__ = "ConformanceRestResourceInteraction"

    code = Column(primitives.StringField)
    """ read | vread | update | delete | history-instance | validate |
        history-type | create | search-type.
        Type `str`. """

    documentation = Column(primitives.StringField)
    """ Anything special about operation behavior.
        Type `str`. """

    def __init__(self, code, documentation,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.documentation = documentation

    def __repr__(self):
        return '<ConformanceRestResourceInteraction %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConformanceRestResourceSearchParam(backboneelement.BackboneElement):
    """ Search params supported by implementation.

    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """

    __tablename__ = "ConformanceRestResourceSearchParam"

    chain = Column(primitives.StringField)
    """ Chained names supported.
        List of `str` items. """

    definition = Column(primitives.StringField)
    """ Source of definition for parameter.
        Type `str`. """

    documentation = Column(primitives.StringField)
    """ Server-specific usage.
        Type `str`. """

    modifier = Column(primitives.StringField)
    """ missing | exact | contains | not | text | in | not-in | below |
        above | type.
        List of `str` items. """

    name = Column(primitives.StringField)
    """ Name of search parameter.
        Type `str`. """

    target = Column(primitives.StringField)
    """ Types of resource (if a resource reference).
        List of `str` items. """

    type = Column(primitives.StringField)
    """ number | date | string | token | reference | composite | quantity |
        uri.
        Type `str`. """

    def __init__(self, chain, definition, documentation, modifier, name, target, type,):
        """ Initialize all valid properties.
        """
        self.chain = chain
        self.definition = definition
        self.documentation = documentation
        self.modifier = modifier
        self.name = name
        self.target = target
        self.type = type

    def __repr__(self):
        return '<ConformanceRestResourceSearchParam %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConformanceRestSecurity(backboneelement.BackboneElement):
    """ Information about security of implementation.

    Information about security implementation from an interface perspective -
    what a client needs to know.
    """

    __tablename__ = "ConformanceRestSecurity"

    certificate = Column(ConformanceRestSecurityCertificate)
    """ Certificates associated with security profiles.
        List of `ConformanceRestSecurityCertificate` items (represented as `dict` in JSON). """

    cors = Column(bool)
    """ Adds CORS Headers (http://enable-cors.org/).
        Type `bool`. """

    description = Column(primitives.StringField)
    """ General description of how security works.
        Type `str`. """

    service = Column(CodeableConcept)
    """ OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, certificate, cors, description, service,):
        """ Initialize all valid properties.
        """
        self.certificate = certificate
        self.cors = cors
        self.description = description
        self.service = service

    def __repr__(self):
        return '<ConformanceRestSecurity %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConformanceRestSecurityCertificate(backboneelement.BackboneElement):
    """ Certificates associated with security profiles.
    """

    __tablename__ = "ConformanceRestSecurityCertificate"

    blob = Column(primitives.StringField)
    """ Actual certificate.
        Type `str`. """

    type = Column(primitives.StringField)
    """ Mime type for certificate.
        Type `str`. """

    def __init__(self, blob, type,):
        """ Initialize all valid properties.
        """
        self.blob = blob
        self.type = type

    def __repr__(self):
        return '<ConformanceRestSecurityCertificate %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConformanceSoftware(backboneelement.BackboneElement):
    """ Software that is covered by this conformance statement.

    Software that is covered by this conformance statement.  It is used when
    the conformance statement describes the capabilities of a particular
    software version, independent of an installation.
    """

    __tablename__ = "ConformanceSoftware"

    name = Column(primitives.StringField)
    """ A name the software is known by.
        Type `str`. """

    releaseDate = Column(FHIRDate)
    """ Date this version released.
        Type `FHIRDate` (represented as `str` in JSON). """

    version = Column(primitives.StringField)
    """ Version covered by this statement.
        Type `str`. """

    def __init__(self, name, releaseDate, version,):
        """ Initialize all valid properties.
        """
        self.name = name
        self.releaseDate = releaseDate
        self.version = version

    def __repr__(self):
        return '<ConformanceSoftware %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirreference