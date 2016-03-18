#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ConceptMap)
#  Date: 2016-03-18.


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

    copyright = Column()
    """ Use and/or publishing restrictions.
        Type `str`. """

    date = Column()
    """ Date for given status.
        Type `FHIRDate` (represented as `str` in JSON). """

    description = Column()
    """ Human language description of the concept map.
        Type `str`. """

    element = Column(ConceptMapElement)
    """ Mappings for a concept from the source set.
        List of `ConceptMapElement` items (represented as `dict` in JSON). """

    experimental = Column()
    """ If for testing purposes, not real usage.
        Type `bool`. """

    identifier = Column()
    """ Additional identifier for the concept map.
        Type `Identifier` (represented as `dict` in JSON). """

    name = Column()
    """ Informal name for this concept map.
        Type `str`. """

    publisher = Column()
    """ Name of the publisher (organization or individual).
        Type `str`. """

    requirements = Column()
    """ Why needed.
        Type `str`. """

    sourceReference = Column()
    """ Identifies the source of the concepts which are being mapped.
        Type `FHIRReference` referencing `ValueSet, StructureDefinition` (represented as `dict` in JSON). """

    sourceUri = Column()
    """ Identifies the source of the concepts which are being mapped.
        Type `str`. """

    status = Column()
    """ draft | active | retired.
        Type `str`. """

    targetReference = Column()
    """ Provides context to the mappings.
        Type `FHIRReference` referencing `ValueSet, StructureDefinition` (represented as `dict` in JSON). """

    targetUri = Column()
    """ Provides context to the mappings.
        Type `str`. """

    url = Column()
    """ Globally unique logical id for concept map.
        Type `str`. """

    useContext = Column(CodeableConcept)
    """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    version = Column()
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


from . import backboneelement

class ConceptMapContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    __tablename__ = "ConceptMapContact"

    name = Column()
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


class ConceptMapElement(backboneelement.BackboneElement):
    """ Mappings for a concept from the source set.

    Mappings for an individual concept in the source to one or more concepts in
    the target.
    """

    __tablename__ = "ConceptMapElement"

    code = Column()
    """ Identifies element being mapped.
        Type `str`. """

    codeSystem = Column()
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


class ConceptMapElementTarget(backboneelement.BackboneElement):
    """ Concept in target system for element.

    A concept from the target value set that this concept maps to.
    """

    __tablename__ = "ConceptMapElementTarget"

    code = Column()
    """ Code that identifies the target element.
        Type `str`. """

    codeSystem = Column()
    """ System of the target (if necessary).
        Type `str`. """

    comments = Column()
    """ Description of status/issues in mapping.
        Type `str`. """

    dependsOn = Column(ConceptMapElementTargetDependsOn)
    """ Other elements required for this mapping (from context).
        List of `ConceptMapElementTargetDependsOn` items (represented as `dict` in JSON). """

    equivalence = Column()
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


class ConceptMapElementTargetDependsOn(backboneelement.BackboneElement):
    """ Other elements required for this mapping (from context).

    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified element can be resolved, and it has the
    specified value.
    """

    __tablename__ = "ConceptMapElementTargetDependsOn"

    code = Column()
    """ Value of the referenced element.
        Type `str`. """

    codeSystem = Column()
    """ Code System (if necessary).
        Type `str`. """

    element = Column()
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