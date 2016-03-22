#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/StructureDefinition)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class StructureDefinition(domainresource.DomainResource):
    """ Structural Definition.

    A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions, and constraints on resources and data types.
    """

    __tablename__ = "StructureDefinition"

    abstract = Column(bool)
    """ Whether the structure is abstract.
        Type `bool`. """

    base = Column(primitives.StringField)
    """ Structure that this set of constraints applies to.
        Type `str`. """

    code = Column(Coding)
    """ Assist with indexing and finding.
        List of `Coding` items (represented as `dict` in JSON). """

    constrainedType = Column(primitives.StringField)
    """ Any datatype or resource, including abstract ones.
        Type `str`. """

    contact = Column(StructureDefinitionContact)
    """ Contact details of the publisher.
        List of `StructureDefinitionContact` items (represented as `dict` in JSON). """

    context = Column(primitives.StringField)
    """ Where the extension can be used in instances.
        List of `str` items. """

    contextType = Column(primitives.StringField)
    """ resource | datatype | mapping | extension.
        Type `str`. """

    copyright = Column(primitives.StringField)
    """ Use and/or publishing restrictions.
        Type `str`. """

    date = Column(FHIRDate)
    """ Date for this version of the StructureDefinition.
        Type `FHIRDate` (represented as `str` in JSON). """

    description = Column(primitives.StringField)
    """ Natural language description of the StructureDefinition.
        Type `str`. """

    differential = Column(StructureDefinitionDifferential)
    """ Differential view of the structure.
        Type `StructureDefinitionDifferential` (represented as `dict` in JSON). """

    display = Column(primitives.StringField)
    """ Use this name when displaying the value.
        Type `str`. """

    experimental = Column(bool)
    """ If for testing purposes, not real usage.
        Type `bool`. """

    fhirVersion = Column(primitives.StringField)
    """ FHIR Version this StructureDefinition targets.
        Type `str`. """

    identifier = Column(Identifier)
    """ Other identifiers for the StructureDefinition.
        List of `Identifier` items (represented as `dict` in JSON). """

    kind = Column(primitives.StringField)
    """ datatype | resource | logical.
        Type `str`. """

    mapping = Column(StructureDefinitionMapping)
    """ External specification that the content is mapped to.
        List of `StructureDefinitionMapping` items (represented as `dict` in JSON). """

    name = Column(primitives.StringField)
    """ Informal name for this StructureDefinition.
        Type `str`. """

    publisher = Column(primitives.StringField)
    """ Name of the publisher (Organization or individual).
        Type `str`. """

    requirements = Column(primitives.StringField)
    """ Scope and Usage this structure definition is for.
        Type `str`. """

    snapshot = Column(StructureDefinitionSnapshot)
    """ Snapshot view of the structure.
        Type `StructureDefinitionSnapshot` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ draft | active | retired.
        Type `str`. """

    url = Column(primitives.StringField)
    """ Absolute URL used to reference this StructureDefinition.
        Type `str`. """

    useContext = Column(CodeableConcept)
    """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    version = Column(primitives.StringField)
    """ Logical id for this version of the StructureDefinition.
        Type `str`. """

    def __init__(self, abstract, base, code, constrainedType, contact, context, contextType, copyright, date, description, differential, display, experimental, fhirVersion, identifier, kind, mapping, name, publisher, requirements, snapshot, status, url, useContext, version,):
        """ Initialize all valid properties.
        """
        self.abstract = abstract
        self.base = base
        self.code = code
        self.constrainedType = constrainedType
        self.contact = contact
        self.context = context
        self.contextType = contextType
        self.copyright = copyright
        self.date = date
        self.description = description
        self.differential = differential
        self.display = display
        self.experimental = experimental
        self.fhirVersion = fhirVersion
        self.identifier = identifier
        self.kind = kind
        self.mapping = mapping
        self.name = name
        self.publisher = publisher
        self.requirements = requirements
        self.snapshot = snapshot
        self.status = status
        self.url = url
        self.useContext = useContext
        self.version = version

    def __repr__(self):
        return '<StructureDefinition %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class StructureDefinitionContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    __tablename__ = "StructureDefinitionContact"

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
        return '<StructureDefinitionContact %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class StructureDefinitionDifferential(backboneelement.BackboneElement):
    """ Differential view of the structure.

    A differential view is expressed relative to the base StructureDefinition -
    a statement of differences that it applies.
    """

    __tablename__ = "StructureDefinitionDifferential"

    element = Column(ElementDefinition)
    """ Definition of elements in the resource (if no StructureDefinition).
        List of `ElementDefinition` items (represented as `dict` in JSON). """

    def __init__(self, element,):
        """ Initialize all valid properties.
        """
        self.element = element

    def __repr__(self):
        return '<StructureDefinitionDifferential %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class StructureDefinitionMapping(backboneelement.BackboneElement):
    """ External specification that the content is mapped to.

    An external specification that the content is mapped to.
    """

    __tablename__ = "StructureDefinitionMapping"

    comments = Column(primitives.StringField)
    """ Versions, Issues, Scope limitations etc..
        Type `str`. """

    identity = Column(primitives.StringField)
    """ Internal id when this mapping is used.
        Type `str`. """

    name = Column(primitives.StringField)
    """ Names what this mapping refers to.
        Type `str`. """

    uri = Column(primitives.StringField)
    """ Identifies what this mapping refers to.
        Type `str`. """

    def __init__(self, comments, identity, name, uri,):
        """ Initialize all valid properties.
        """
        self.comments = comments
        self.identity = identity
        self.name = name
        self.uri = uri

    def __repr__(self):
        return '<StructureDefinitionMapping %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class StructureDefinitionSnapshot(backboneelement.BackboneElement):
    """ Snapshot view of the structure.

    A snapshot view is expressed in a stand alone form that can be used and
    interpreted without considering the base StructureDefinition.
    """

    __tablename__ = "StructureDefinitionSnapshot"

    element = Column(ElementDefinition)
    """ Definition of elements in the resource (if no StructureDefinition).
        List of `ElementDefinition` items (represented as `dict` in JSON). """

    def __init__(self, element,):
        """ Initialize all valid properties.
        """
        self.element = element

    def __repr__(self):
        return '<StructureDefinitionSnapshot %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import coding
from . import contactpoint
from . import elementdefinition
from . import fhirdate
from . import identifier