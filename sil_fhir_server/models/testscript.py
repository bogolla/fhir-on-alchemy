#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/TestScript)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class TestScript(domainresource.DomainResource):
    """ Describes a set of tests.

    TestScript is a resource that specifies a suite of tests against a FHIR
    server implementation to determine compliance against the FHIR
    specification.
    """

    __tablename__ = "TestScript"

    contact = Column(TestScriptContact)
    """ Contact details of the publisher.
        List of `TestScriptContact` items (represented as `dict` in JSON). """

    copyright = Column(primitives.StringField)
    """ Use and/or publishing restrictions.
        Type `str`. """

    date = Column(FHIRDate)
    """ Date for this version of the TestScript.
        Type `FHIRDate` (represented as `str` in JSON). """

    description = Column(primitives.StringField)
    """ Natural language description of the TestScript.
        Type `str`. """

    experimental = Column(bool)
    """ If for testing purposes, not real usage.
        Type `bool`. """

    fixture = Column(TestScriptFixture)
    """ Fixture in the test script - by reference (uri).
        List of `TestScriptFixture` items (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ External identifier.
        Type `Identifier` (represented as `dict` in JSON). """

    metadata = Column(TestScriptMetadata)
    """ Required capability that is assumed to function correctly on the
        FHIR server being tested.
        Type `TestScriptMetadata` (represented as `dict` in JSON). """

    multiserver = Column(bool)
    """ Whether or not the tests apply to more than one FHIR server.
        Type `bool`. """

    name = Column(primitives.StringField)
    """ Informal name for this TestScript.
        Type `str`. """

    profile = Column(FHIRReference)
    """ Reference of the validation profile.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """

    publisher = Column(primitives.StringField)
    """ Name of the publisher (Organization or individual).
        Type `str`. """

    requirements = Column(primitives.StringField)
    """ Scope and Usage this Test Script is for.
        Type `str`. """

    setup = Column(TestScriptSetup)
    """ A series of required setup operations before tests are executed.
        Type `TestScriptSetup` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ draft | active | retired.
        Type `str`. """

    teardown = Column(TestScriptTeardown)
    """ A series of required clean up steps.
        Type `TestScriptTeardown` (represented as `dict` in JSON). """

    test = Column(TestScriptTest)
    """ A test in this script.
        List of `TestScriptTest` items (represented as `dict` in JSON). """

    url = Column(primitives.StringField)
    """ Absolute URL used to reference this TestScript.
        Type `str`. """

    useContext = Column(CodeableConcept)
    """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    variable = Column(TestScriptVariable)
    """ Placeholder for evaluated elements.
        List of `TestScriptVariable` items (represented as `dict` in JSON). """

    version = Column(primitives.StringField)
    """ Logical id for this version of the TestScript.
        Type `str`. """

    def __init__(self, contact, copyright, date, description, experimental, fixture, identifier, metadata, multiserver, name, profile, publisher, requirements, setup, status, teardown, test, url, useContext, variable, version,):
        """ Initialize all valid properties.
        """
        self.contact = contact
        self.copyright = copyright
        self.date = date
        self.description = description
        self.experimental = experimental
        self.fixture = fixture
        self.identifier = identifier
        self.metadata = metadata
        self.multiserver = multiserver
        self.name = name
        self.profile = profile
        self.publisher = publisher
        self.requirements = requirements
        self.setup = setup
        self.status = status
        self.teardown = teardown
        self.test = test
        self.url = url
        self.useContext = useContext
        self.variable = variable
        self.version = version

    def __repr__(self):
        return '<TestScript %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class TestScriptContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    __tablename__ = "TestScriptContact"

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
        return '<TestScriptContact %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class TestScriptFixture(backboneelement.BackboneElement):
    """ Fixture in the test script - by reference (uri).

    Fixture in the test script - by reference (uri). All fixtures are required
    for the test script to execute.
    """

    __tablename__ = "TestScriptFixture"

    autocreate = Column(bool)
    """ Whether or not to implicitly create the fixture during setup.
        Type `bool`. """

    autodelete = Column(bool)
    """ Whether or not to implicitly delete the fixture during teardown.
        Type `bool`. """

    resource = Column(FHIRReference)
    """ Reference of the resource.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    def __init__(self, autocreate, autodelete, resource,):
        """ Initialize all valid properties.
        """
        self.autocreate = autocreate
        self.autodelete = autodelete
        self.resource = resource

    def __repr__(self):
        return '<TestScriptFixture %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class TestScriptMetadata(backboneelement.BackboneElement):
    """ Required capability that is assumed to function correctly on the FHIR
    server being tested.

    The required capability must exist and are assumed to function correctly on
    the FHIR server being tested.
    """

    __tablename__ = "TestScriptMetadata"

    capability = Column(TestScriptMetadataCapability)
    """ Capabilities  that are assumed to function correctly on the FHIR
        server being tested.
        List of `TestScriptMetadataCapability` items (represented as `dict` in JSON). """

    link = Column(TestScriptMetadataLink)
    """ Links to the FHIR specification.
        List of `TestScriptMetadataLink` items (represented as `dict` in JSON). """

    def __init__(self, capability, link,):
        """ Initialize all valid properties.
        """
        self.capability = capability
        self.link = link

    def __repr__(self):
        return '<TestScriptMetadata %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class TestScriptMetadataCapability(backboneelement.BackboneElement):
    """ Capabilities  that are assumed to function correctly on the FHIR server
    being tested.

    Capabilities that must exist and are assumed to function correctly on the
    FHIR server being tested.
    """

    __tablename__ = "TestScriptMetadataCapability"

    conformance = Column(FHIRReference)
    """ Required Conformance.
        Type `FHIRReference` referencing `Conformance` (represented as `dict` in JSON). """

    description = Column(primitives.StringField)
    """ The expected capabilities of the server.
        Type `str`. """

    destination = Column(Integer)
    """ Which server these requirements apply to.
        Type `int`. """

    link = Column(primitives.StringField)
    """ Links to the FHIR specification.
        List of `str` items. """

    required = Column(bool)
    """ Are the capabilities required?.
        Type `bool`. """

    validated = Column(bool)
    """ Are the capabilities validated?.
        Type `bool`. """

    def __init__(self, conformance, description, destination, link, required, validated,):
        """ Initialize all valid properties.
        """
        self.conformance = conformance
        self.description = description
        self.destination = destination
        self.link = link
        self.required = required
        self.validated = validated

    def __repr__(self):
        return '<TestScriptMetadataCapability %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class TestScriptMetadataLink(backboneelement.BackboneElement):
    """ Links to the FHIR specification.

    A link to the FHIR specification that this test is covering.
    """

    __tablename__ = "TestScriptMetadataLink"

    description = Column(primitives.StringField)
    """ Short description.
        Type `str`. """

    url = Column(primitives.StringField)
    """ URL to the specification.
        Type `str`. """

    def __init__(self, description, url,):
        """ Initialize all valid properties.
        """
        self.description = description
        self.url = url

    def __repr__(self):
        return '<TestScriptMetadataLink %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class TestScriptSetup(backboneelement.BackboneElement):
    """ A series of required setup operations before tests are executed.
    """

    __tablename__ = "TestScriptSetup"

    action = Column(TestScriptSetupAction)
    """ A setup operation or assert to perform.
        List of `TestScriptSetupAction` items (represented as `dict` in JSON). """

    metadata = Column(TestScriptMetadata)
    """ Capabilities  that are assumed to function correctly on the FHIR
        server being tested.
        Type `TestScriptMetadata` (represented as `dict` in JSON). """

    def __init__(self, action, metadata,):
        """ Initialize all valid properties.
        """
        self.action = action
        self.metadata = metadata

    def __repr__(self):
        return '<TestScriptSetup %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class TestScriptSetupAction(backboneelement.BackboneElement):
    """ A setup operation or assert to perform.

    Action would contain either an operation or an assertion.
    """

    __tablename__ = "TestScriptSetupAction"

    assert_fhir = Column(TestScriptSetupActionAssert)
    """ The assertion to perform.
        Type `TestScriptSetupActionAssert` (represented as `dict` in JSON). """

    operation = Column(TestScriptSetupActionOperation)
    """ The setup operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """

    def __init__(self, assert_fhir, operation,):
        """ Initialize all valid properties.
        """
        self.assert_fhir = assert_fhir
        self.operation = operation

    def __repr__(self):
        return '<TestScriptSetupAction %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class TestScriptSetupActionAssert(backboneelement.BackboneElement):
    """ The assertion to perform.

    Evaluates the results of previous operations to determine if the server
    under test behaves appropriately.
    """

    __tablename__ = "TestScriptSetupActionAssert"

    compareToSourceId = Column(primitives.StringField)
    """ Id of fixture used to compare the "sourceId/path" evaluations to.
        Type `str`. """

    compareToSourcePath = Column(primitives.StringField)
    """ XPath or JSONPath expression against fixture used to compare the
        "sourceId/path" evaluations to.
        Type `str`. """

    contentType = Column(primitives.StringField)
    """ xml | json.
        Type `str`. """

    description = Column(primitives.StringField)
    """ Tracking/reporting assertion description.
        Type `str`. """

    direction = Column(primitives.StringField)
    """ response | request.
        Type `str`. """

    headerField = Column(primitives.StringField)
    """ HTTP header field name.
        Type `str`. """

    label = Column(primitives.StringField)
    """ Tracking/logging assertion label.
        Type `str`. """

    minimumId = Column(primitives.StringField)
    """ Fixture Id of minimum content resource.
        Type `str`. """

    navigationLinks = Column(bool)
    """ Perform validation on navigation links?.
        Type `bool`. """

    operator = Column(primitives.StringField)
    """ equals | notEquals | in | notIn | greaterThan | lessThan | empty |
        notEmpty | contains | notContains.
        Type `str`. """

    path = Column(primitives.StringField)
    """ XPath or JSONPath expression.
        Type `str`. """

    resource = Column(primitives.StringField)
    """ Resource type.
        Type `str`. """

    response = Column(primitives.StringField)
    """ okay | created | noContent | notModified | bad | forbidden |
        notFound | methodNotAllowed | conflict | gone | preconditionFailed
        | unprocessable.
        Type `str`. """

    responseCode = Column(primitives.StringField)
    """ HTTP response code to test.
        Type `str`. """

    sourceId = Column(primitives.StringField)
    """ Fixture Id of source expression or headerField.
        Type `str`. """

    validateProfileId = Column(primitives.StringField)
    """ Profile Id of validation profile reference.
        Type `str`. """

    value = Column(primitives.StringField)
    """ The value to compare to.
        Type `str`. """

    warningOnly = Column(bool)
    """ Will this assert produce a warning only on error?.
        Type `bool`. """

    def __init__(self, compareToSourceId, compareToSourcePath, contentType, description, direction, headerField, label, minimumId, navigationLinks, operator, path, resource, response, responseCode, sourceId, validateProfileId, value, warningOnly,):
        """ Initialize all valid properties.
        """
        self.compareToSourceId = compareToSourceId
        self.compareToSourcePath = compareToSourcePath
        self.contentType = contentType
        self.description = description
        self.direction = direction
        self.headerField = headerField
        self.label = label
        self.minimumId = minimumId
        self.navigationLinks = navigationLinks
        self.operator = operator
        self.path = path
        self.resource = resource
        self.response = response
        self.responseCode = responseCode
        self.sourceId = sourceId
        self.validateProfileId = validateProfileId
        self.value = value
        self.warningOnly = warningOnly

    def __repr__(self):
        return '<TestScriptSetupActionAssert %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class TestScriptSetupActionOperation(backboneelement.BackboneElement):
    """ The setup operation to perform.

    The operation to perform.
    """

    __tablename__ = "TestScriptSetupActionOperation"

    accept = Column(primitives.StringField)
    """ xml | json.
        Type `str`. """

    contentType = Column(primitives.StringField)
    """ xml | json.
        Type `str`. """

    description = Column(primitives.StringField)
    """ Tracking/reporting operation description.
        Type `str`. """

    destination = Column(Integer)
    """ Which server to perform the operation on.
        Type `int`. """

    encodeRequestUrl = Column(bool)
    """ Whether or not to send the request url in encoded format.
        Type `bool`. """

    label = Column(primitives.StringField)
    """ Tracking/logging operation label.
        Type `str`. """

    params = Column(primitives.StringField)
    """ Explicitly defined path parameters.
        Type `str`. """

    requestHeader = Column(TestScriptSetupActionOperationRequestHeader)
    """ Each operation can have one ore more header elements.
        List of `TestScriptSetupActionOperationRequestHeader` items (represented as `dict` in JSON). """

    resource = Column(primitives.StringField)
    """ Resource type.
        Type `str`. """

    responseId = Column(primitives.StringField)
    """ Fixture Id of mapped response.
        Type `str`. """

    sourceId = Column(primitives.StringField)
    """ Fixture Id of body for PUT and POST requests.
        Type `str`. """

    targetId = Column(primitives.StringField)
    """ Id of fixture used for extracting the [id],  [type], and [vid] for
        GET requests.
        Type `str`. """

    type = Column(Coding)
    """ The setup operation type that will be executed.
        Type `Coding` (represented as `dict` in JSON). """

    url = Column(primitives.StringField)
    """ Request URL.
        Type `str`. """

    def __init__(self, accept, contentType, description, destination, encodeRequestUrl, label, params, requestHeader, resource, responseId, sourceId, targetId, type, url,):
        """ Initialize all valid properties.
        """
        self.accept = accept
        self.contentType = contentType
        self.description = description
        self.destination = destination
        self.encodeRequestUrl = encodeRequestUrl
        self.label = label
        self.params = params
        self.requestHeader = requestHeader
        self.resource = resource
        self.responseId = responseId
        self.sourceId = sourceId
        self.targetId = targetId
        self.type = type
        self.url = url

    def __repr__(self):
        return '<TestScriptSetupActionOperation %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class TestScriptSetupActionOperationRequestHeader(backboneelement.BackboneElement):
    """ Each operation can have one ore more header elements.

    Header elements would be used to set HTTP headers.
    """

    __tablename__ = "TestScriptSetupActionOperationRequestHeader"

    field = Column(primitives.StringField)
    """ HTTP header field name.
        Type `str`. """

    value = Column(primitives.StringField)
    """ HTTP headerfield value.
        Type `str`. """

    def __init__(self, field, value,):
        """ Initialize all valid properties.
        """
        self.field = field
        self.value = value

    def __repr__(self):
        return '<TestScriptSetupActionOperationRequestHeader %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class TestScriptTeardown(backboneelement.BackboneElement):
    """ A series of required clean up steps.

    A series of operations required to clean up after the all the tests are
    executed (successfully or otherwise).
    """

    __tablename__ = "TestScriptTeardown"

    action = Column(TestScriptTeardownAction)
    """ One or more teardown operations to perform.
        List of `TestScriptTeardownAction` items (represented as `dict` in JSON). """

    def __init__(self, action,):
        """ Initialize all valid properties.
        """
        self.action = action

    def __repr__(self):
        return '<TestScriptTeardown %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class TestScriptTeardownAction(backboneelement.BackboneElement):
    """ One or more teardown operations to perform.

    The teardown action will only contain an operation.
    """

    __tablename__ = "TestScriptTeardownAction"

    operation = Column(TestScriptSetupActionOperation)
    """ The teardown operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """

    def __init__(self, operation,):
        """ Initialize all valid properties.
        """
        self.operation = operation

    def __repr__(self):
        return '<TestScriptTeardownAction %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class TestScriptTest(backboneelement.BackboneElement):
    """ A test in this script.
    """

    __tablename__ = "TestScriptTest"

    action = Column(TestScriptTestAction)
    """ A test operation or assert to perform.
        List of `TestScriptTestAction` items (represented as `dict` in JSON). """

    description = Column(primitives.StringField)
    """ Tracking/reporting short description of the test.
        Type `str`. """

    metadata = Column(TestScriptMetadata)
    """ Capabilities  that are expected to function correctly on the FHIR
        server being tested.
        Type `TestScriptMetadata` (represented as `dict` in JSON). """

    name = Column(primitives.StringField)
    """ Tracking/logging name of this test.
        Type `str`. """

    def __init__(self, action, description, metadata, name,):
        """ Initialize all valid properties.
        """
        self.action = action
        self.description = description
        self.metadata = metadata
        self.name = name

    def __repr__(self):
        return '<TestScriptTest %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class TestScriptTestAction(backboneelement.BackboneElement):
    """ A test operation or assert to perform.

    Action would contain either an operation or an assertion.
    """

    __tablename__ = "TestScriptTestAction"

    assert_fhir = Column(TestScriptSetupActionAssert)
    """ The setup assertion to perform.
        Type `TestScriptSetupActionAssert` (represented as `dict` in JSON). """

    operation = Column(TestScriptSetupActionOperation)
    """ The setup operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """

    def __init__(self, assert_fhir, operation,):
        """ Initialize all valid properties.
        """
        self.assert_fhir = assert_fhir
        self.operation = operation

    def __repr__(self):
        return '<TestScriptTestAction %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class TestScriptVariable(backboneelement.BackboneElement):
    """ Placeholder for evaluated elements.

    Variable is set based either on element value in response body or on header
    field value in the response headers.
    """

    __tablename__ = "TestScriptVariable"

    headerField = Column(primitives.StringField)
    """ HTTP header field name for source.
        Type `str`. """

    name = Column(primitives.StringField)
    """ Descriptive name for this variable.
        Type `str`. """

    path = Column(primitives.StringField)
    """ XPath or JSONPath against the fixture body.
        Type `str`. """

    sourceId = Column(primitives.StringField)
    """ Fixture Id of source expression or headerField within this variable.
        Type `str`. """

    def __init__(self, headerField, name, path, sourceId,):
        """ Initialize all valid properties.
        """
        self.headerField = headerField
        self.name = name
        self.path = path
        self.sourceId = sourceId

    def __repr__(self):
        return '<TestScriptVariable %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier