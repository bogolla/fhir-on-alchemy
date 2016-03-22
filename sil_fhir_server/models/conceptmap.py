#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ConceptMap)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer
from sil_fhir_server.data_types import primitives
from . import domainresource

class ConceptMap(domainresource.DomainResource):
    """ A map from one set of concepts to one or more other concepts.

    A statement of relationships from one set of concepts to one or more other
    concepts - either code systems or data elements, or classes in class
    models.
    """

    __tablename__ = "ConceptMap"

    contact = Column(ConceptMapContact)
    """ Contact details of the publisher.
        List of `ConceptMapContact` items (represented as `dict` in JSON). """

    copyright = Column(primitives.StringField)
    """ Use and/or publishing restrictions.
        Type `str`. """

    date = Column(FHIRDate)
    """ Date for given status.
        Type `FHIRDate` (represented as `str` in JSON). """

    description = Column(primitives.StringField)
    """ Human language description of the concept map.
        Type `str`. """

    element = Column(ConceptMapElement)
    """ Mappings for a concept from the source set.
        List of `ConceptMapElement` items (represented as `dict` in JSON). """

    experimental = Column(bool)
    """ If for testing purposes, not real usage.
        Type `bool`. """

    identifier = Column(Identifier)
    """ Additional identifier for the concept map.
        Type `Identifier` (represented as `dict` in JSON). """

    name = Column(primitives.StringField)
    """ Informal name for this concept map.
        Type `str`. """

    publisher = Column(primitives.StringField)
    """ Name of the publisher (organization or individual).
        Type `str`. """

    requirements = Column(primitives.StringField)
    """ Why needed.
        Type `str`. """

    sourceReference = Column(FHIRReference)
    """ Identifies the source of the concepts which are being mapped.
        Type `FHIRReference` referencing `ValueSet, StructureDefinition` (represented as `dict` in JSON). """

    sourceUri = Column(primitives.StringField)
    """ Identifies the source of the concepts which are being mapped.
        Type `str`. """

    status = Column(primitives.StringField)
    """ draft | active | retired.
        Type `str`. """

    targetReference = Column(FHIRReference)
    """ Provides context to the mappings.
        Type `FHIRReference` referencing `ValueSet, StructureDefinition` (represented as `dict` in JSON). """

    targetUri = Column(primitives.StringField)
    """ Provides context to the mappings.
        Type `str`. """

    url = Column(primitives.StringField)
    """ Globally unique logical id for concept map.
        Type `str`. """

    useContext = Column(CodeableConcept)
    """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    version = Column(primitives.StringField)
    """ Logical id for this version of the concept map.
        Type `str`. """

    def __init__(self, contact, copyright, date, description, element, experimental, identifier, name, publisher, requirements, sourceReference, sourceUri, status, targetReference, targetUri, url, useContext, version,):
        """ Initialize all valid properties.
        """
        self.contact = contact
        self.copyright = copyright
        self.date = date
        self.description = description
        self.element = element
        self.experimental = experimental
        self.identifier = identifier
        self.name = name
        self.publisher = publisher
        self.requirements = requirements
        self.sourceReference = sourceReference
        self.sourceUri = sourceUri
        self.status = status
        self.targetReference = targetReference
        self.targetUri = targetUri
        self.url = url
        self.useContext = useContext
        self.version = version

    def __repr__(self):
        return '<ConceptMap %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class ConceptMapContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    __tablename__ = "ConceptMapContact"

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
        return '<ConceptMapContact %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConceptMapElement(backboneelement.BackboneElement):
    """ Mappings for a concept from the source set.

    Mappings for an individual concept in the source to one or more concepts in
    the target.
    """

    __tablename__ = "ConceptMapElement"

    code = Column(primitives.StringField)
    """ Identifies element being mapped.
        Type `str`. """

    codeSystem = Column(primitives.StringField)
    """ Code System (if value set crosses code systems).
        Type `str`. """

    target = Column(ConceptMapElementTarget)
    """ Concept in target system for element.
        List of `ConceptMapElementTarget` items (represented as `dict` in JSON). """

    def __init__(self, code, codeSystem, target,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.codeSystem = codeSystem
        self.target = target

    def __repr__(self):
        return '<ConceptMapElement %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConceptMapElementTarget(backboneelement.BackboneElement):
    """ Concept in target system for element.

    A concept from the target value set that this concept maps to.
    """

    __tablename__ = "ConceptMapElementTarget"

    code = Column(primitives.StringField)
    """ Code that identifies the target element.
        Type `str`. """

    codeSystem = Column(primitives.StringField)
    """ System of the target (if necessary).
        Type `str`. """

    comments = Column(primitives.StringField)
    """ Description of status/issues in mapping.
        Type `str`. """

    dependsOn = Column(ConceptMapElementTargetDependsOn)
    """ Other elements required for this mapping (from context).
        List of `ConceptMapElementTargetDependsOn` items (represented as `dict` in JSON). """

    equivalence = Column(primitives.StringField)
    """ equivalent | equal | wider | subsumes | narrower | specializes |
        inexact | unmatched | disjoint.
        Type `str`. """

    product = Column(ConceptMapElementTargetDependsOn)
    """ Other concepts that this mapping also produces.
        List of `ConceptMapElementTargetDependsOn` items (represented as `dict` in JSON). """

    def __init__(self, code, codeSystem, comments, dependsOn, equivalence, product,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.codeSystem = codeSystem
        self.comments = comments
        self.dependsOn = dependsOn
        self.equivalence = equivalence
        self.product = product

    def __repr__(self):
        return '<ConceptMapElementTarget %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ConceptMapElementTargetDependsOn(backboneelement.BackboneElement):
    """ Other elements required for this mapping (from context).

    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified element can be resolved, and it has the
    specified value.
    """

    __tablename__ = "ConceptMapElementTargetDependsOn"

    code = Column(primitives.StringField)
    """ Value of the referenced element.
        Type `str`. """

    codeSystem = Column(primitives.StringField)
    """ Code System (if necessary).
        Type `str`. """

    element = Column(primitives.StringField)
    """ Reference to element/field/ValueSet mapping depends on.
        Type `str`. """

    def __init__(self, code, codeSystem, element,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.codeSystem = codeSystem
        self.element = element

    def __repr__(self):
        return '<ConceptMapElementTargetDependsOn %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier