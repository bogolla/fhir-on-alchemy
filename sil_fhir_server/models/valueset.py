#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ValueSet)
#  Date: 2016-03-18.


from . import domainresource

class ValueSet(domainresource.DomainResource):
    """ A set of codes drawn from one or more code systems.

    A value set specifies a set of codes drawn from one or more code systems.
    """

    __tablename__ = "ValueSet"

    codeSystem = Column()
    """ An inline code system, which is part of this value set.
        Type `ValueSetCodeSystem` (represented as `dict` in JSON). """

    compose = Column()
    """ When value set includes codes from elsewhere.
        Type `ValueSetCompose` (represented as `dict` in JSON). """

    contact = Column(ValueSetContact)
    """ Contact details of the publisher.
        List of `ValueSetContact` items (represented as `dict` in JSON). """

    copyright = Column()
    """ Use and/or publishing restrictions.
        Type `str`. """

    date = Column()
    """ Date for given status.
        Type `FHIRDate` (represented as `str` in JSON). """

    description = Column()
    """ Human language description of the value set.
        Type `str`. """

    expansion = Column()
    """ Used when the value set is "expanded".
        Type `ValueSetExpansion` (represented as `dict` in JSON). """

    experimental = Column()
    """ If for testing purposes, not real usage.
        Type `bool`. """

    extensible = Column()
    """ Whether this is intended to be used with an extensible binding.
        Type `bool`. """

    identifier = Column()
    """ Additional identifier for the value set (e.g. HL7 v2 / CDA).
        Type `Identifier` (represented as `dict` in JSON). """

    immutable = Column()
    """ Indicates whether or not any change to the content logical
        definition may occur.
        Type `bool`. """

    lockedDate = Column()
    """ Fixed date for all referenced code systems and value sets.
        Type `FHIRDate` (represented as `str` in JSON). """

    name = Column()
    """ Informal name for this value set.
        Type `str`. """

    publisher = Column()
    """ Name of the publisher (organization or individual).
        Type `str`. """

    requirements = Column()
    """ Why needed.
        Type `str`. """

    status = Column()
    """ draft | active | retired.
        Type `str`. """

    url = Column()
    """ Globally unique logical identifier for  value set.
        Type `str`. """

    useContext = Column(CodeableConcept)
    """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    version = Column()
    """ Logical identifier for this version of the value set.
        Type `str`. """

    def __init__(self, codeSystem, compose, contact, copyright, date, description, expansion, experimental, extensible, identifier, immutable, lockedDate, name, publisher, requirements, status, url, useContext, version,):
        """ Initialize all valid properties.
        """
        self.codeSystem = codeSystem
        self.compose = compose
        self.contact = contact
        self.copyright = copyright
        self.date = date
        self.description = description
        self.expansion = expansion
        self.experimental = experimental
        self.extensible = extensible
        self.identifier = identifier
        self.immutable = immutable
        self.lockedDate = lockedDate
        self.name = name
        self.publisher = publisher
        self.requirements = requirements
        self.status = status
        self.url = url
        self.useContext = useContext
        self.version = version

    def __repr__(self):
        return '<ValueSet %r>' % 'self.property'  # replace self.property


from . import backboneelement

class ValueSetCodeSystem(backboneelement.BackboneElement):
    """ An inline code system, which is part of this value set.

    A definition of a code system, inlined into the value set (as a packaging
    convenience). Note that the inline code system may be used from other value
    sets by referring to its (codeSystem.system) directly.
    """

    __tablename__ = "ValueSetCodeSystem"

    caseSensitive = Column()
    """ If code comparison is case sensitive.
        Type `bool`. """

    concept = Column(ValueSetCodeSystemConcept)
    """ Concepts in the code system.
        List of `ValueSetCodeSystemConcept` items (represented as `dict` in JSON). """

    system = Column()
    """ URI to identify the code system (e.g. in Coding.system).
        Type `str`. """

    version = Column()
    """ Version (for use in Coding.version).
        Type `str`. """

    def __init__(self, caseSensitive, concept, system, version,):
        """ Initialize all valid properties.
        """
        self.caseSensitive = caseSensitive
        self.concept = concept
        self.system = system
        self.version = version

    def __repr__(self):
        return '<ValueSetCodeSystem %r>' % 'self.property'  # replace self.property


class ValueSetCodeSystemConcept(backboneelement.BackboneElement):
    """ Concepts in the code system.

    Concepts that are in the code system. The concept definitions are
    inherently hierarchical, but the definitions must be consulted to determine
    what the meaning of the hierarchical relationships are.
    """

    __tablename__ = "ValueSetCodeSystemConcept"

    abstract = Column()
    """ If this code is not for use as a real concept.
        Type `bool`. """

    code = Column()
    """ Code that identifies concept.
        Type `str`. """

    concept = Column(ValueSetCodeSystemConcept)
    """ Child Concepts (is-a/contains/categorizes).
        List of `ValueSetCodeSystemConcept` items (represented as `dict` in JSON). """

    definition = Column()
    """ Formal definition.
        Type `str`. """

    designation = Column(ValueSetCodeSystemConceptDesignation)
    """ Additional representations for the concept.
        List of `ValueSetCodeSystemConceptDesignation` items (represented as `dict` in JSON). """

    display = Column()
    """ Text to display to the user.
        Type `str`. """

    def __init__(self, abstract, code, concept, definition, designation, display,):
        """ Initialize all valid properties.
        """
        self.abstract = abstract
        self.code = code
        self.concept = concept
        self.definition = definition
        self.designation = designation
        self.display = display

    def __repr__(self):
        return '<ValueSetCodeSystemConcept %r>' % 'self.property'  # replace self.property


class ValueSetCodeSystemConceptDesignation(backboneelement.BackboneElement):
    """ Additional representations for the concept.

    Additional representations for the concept - other languages, aliases,
    specialized purposes, used for particular purposes, etc.
    """

    __tablename__ = "ValueSetCodeSystemConceptDesignation"

    language = Column()
    """ Human language of the designation.
        Type `str`. """

    use = Column()
    """ Details how this designation would be used.
        Type `Coding` (represented as `dict` in JSON). """

    value = Column()
    """ The text value for this designation.
        Type `str`. """

    def __init__(self, language, use, value,):
        """ Initialize all valid properties.
        """
        self.language = language
        self.use = use
        self.value = value

    def __repr__(self):
        return '<ValueSetCodeSystemConceptDesignation %r>' % 'self.property'  # replace self.property


class ValueSetCompose(backboneelement.BackboneElement):
    """ When value set includes codes from elsewhere.

    A set of criteria that provide the content logical definition of the value
    set by including or excluding codes from outside this value set.
    """

    __tablename__ = "ValueSetCompose"

    exclude = Column(ValueSetComposeInclude)
    """ Explicitly exclude codes.
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """

    import_fhir = Column(str)
    """ Import the contents of another value set.
        List of `str` items. """

    include = Column(ValueSetComposeInclude)
    """ Include one or more codes from a code system.
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """

    def __init__(self, exclude, import_fhir, include,):
        """ Initialize all valid properties.
        """
        self.exclude = exclude
        self.import_fhir = import_fhir
        self.include = include

    def __repr__(self):
        return '<ValueSetCompose %r>' % 'self.property'  # replace self.property


class ValueSetComposeInclude(backboneelement.BackboneElement):
    """ Include one or more codes from a code system.
    """

    __tablename__ = "ValueSetComposeInclude"

    concept = Column(ValueSetComposeIncludeConcept)
    """ A concept defined in the system.
        List of `ValueSetComposeIncludeConcept` items (represented as `dict` in JSON). """

    filter = Column(ValueSetComposeIncludeFilter)
    """ Select codes/concepts by their properties (including relationships).
        List of `ValueSetComposeIncludeFilter` items (represented as `dict` in JSON). """

    system = Column()
    """ The system the codes come from.
        Type `str`. """

    version = Column()
    """ Specific version of the code system referred to.
        Type `str`. """

    def __init__(self, concept, filter, system, version,):
        """ Initialize all valid properties.
        """
        self.concept = concept
        self.filter = filter
        self.system = system
        self.version = version

    def __repr__(self):
        return '<ValueSetComposeInclude %r>' % 'self.property'  # replace self.property


class ValueSetComposeIncludeConcept(backboneelement.BackboneElement):
    """ A concept defined in the system.

    Specifies a concept to be included or excluded.
    """

    __tablename__ = "ValueSetComposeIncludeConcept"

    code = Column()
    """ Code or expression from system.
        Type `str`. """

    designation = Column(ValueSetCodeSystemConceptDesignation)
    """ Additional representations for this valueset.
        List of `ValueSetCodeSystemConceptDesignation` items (represented as `dict` in JSON). """

    display = Column()
    """ Test to display for this code for this value set.
        Type `str`. """

    def __init__(self, code, designation, display,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.designation = designation
        self.display = display

    def __repr__(self):
        return '<ValueSetComposeIncludeConcept %r>' % 'self.property'  # replace self.property


class ValueSetComposeIncludeFilter(backboneelement.BackboneElement):
    """ Select codes/concepts by their properties (including relationships).

    Select concepts by specify a matching criteria based on the properties
    (including relationships) defined by the system. If multiple filters are
    specified, they SHALL all be true.
    """

    __tablename__ = "ValueSetComposeIncludeFilter"

    op = Column()
    """ = | is-a | is-not-a | regex | in | not-in.
        Type `str`. """

    property = Column()
    """ A property defined by the code system.
        Type `str`. """

    value = Column()
    """ Code from the system, or regex criteria.
        Type `str`. """

    def __init__(self, op, property, value,):
        """ Initialize all valid properties.
        """
        self.op = op
        self.property = property
        self.value = value

    def __repr__(self):
        return '<ValueSetComposeIncludeFilter %r>' % 'self.property'  # replace self.property


class ValueSetContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    __tablename__ = "ValueSetContact"

    name = Column()
    """ Name of an individual to contact.
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
        return '<ValueSetContact %r>' % 'self.property'  # replace self.property


class ValueSetExpansion(backboneelement.BackboneElement):
    """ Used when the value set is "expanded".

    A value set can also be "expanded", where the value set is turned into a
    simple collection of enumerated codes. This element holds the expansion, if
    it has been performed.
    """

    __tablename__ = "ValueSetExpansion"

    contains = Column(ValueSetExpansionContains)
    """ Codes in the value set.
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """

    identifier = Column()
    """ Uniquely identifies this expansion.
        Type `str`. """

    offset = Column()
    """ Offset at which this resource starts.
        Type `int`. """

    parameter = Column(ValueSetExpansionParameter)
    """ Parameter that controlled the expansion process.
        List of `ValueSetExpansionParameter` items (represented as `dict` in JSON). """

    timestamp = Column()
    """ Time ValueSet expansion happened.
        Type `FHIRDate` (represented as `str` in JSON). """

    total = Column()
    """ Total number of codes in the expansion.
        Type `int`. """

    def __init__(self, contains, identifier, offset, parameter, timestamp, total,):
        """ Initialize all valid properties.
        """
        self.contains = contains
        self.identifier = identifier
        self.offset = offset
        self.parameter = parameter
        self.timestamp = timestamp
        self.total = total

    def __repr__(self):
        return '<ValueSetExpansion %r>' % 'self.property'  # replace self.property


class ValueSetExpansionContains(backboneelement.BackboneElement):
    """ Codes in the value set.

    The codes that are contained in the value set expansion.
    """

    __tablename__ = "ValueSetExpansionContains"

    abstract = Column()
    """ If user cannot select this entry.
        Type `bool`. """

    code = Column()
    """ Code - if blank, this is not a selectable code.
        Type `str`. """

    contains = Column(ValueSetExpansionContains)
    """ Codes contained under this entry.
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """

    display = Column()
    """ User display for the concept.
        Type `str`. """

    system = Column()
    """ System value for the code.
        Type `str`. """

    version = Column()
    """ Version in which this code/display is defined.
        Type `str`. """

    def __init__(self, abstract, code, contains, display, system, version,):
        """ Initialize all valid properties.
        """
        self.abstract = abstract
        self.code = code
        self.contains = contains
        self.display = display
        self.system = system
        self.version = version

    def __repr__(self):
        return '<ValueSetExpansionContains %r>' % 'self.property'  # replace self.property


class ValueSetExpansionParameter(backboneelement.BackboneElement):
    """ Parameter that controlled the expansion process.

    A parameter that controlled the expansion process. These parameters may be
    used by users of expanded value sets to check whether the expansion is
    suitable for a particular purpose, or to pick the correct expansion.
    """

    __tablename__ = "ValueSetExpansionParameter"

    name = Column()
    """ Name as assigned by the server.
        Type `str`. """

    valueBoolean = Column()
    """ Value of the named parameter.
        Type `bool`. """

    valueCode = Column()
    """ Value of the named parameter.
        Type `str`. """

    valueDecimal = Column()
    """ Value of the named parameter.
        Type `float`. """

    valueInteger = Column()
    """ Value of the named parameter.
        Type `int`. """

    valueString = Column()
    """ Value of the named parameter.
        Type `str`. """

    valueUri = Column()
    """ Value of the named parameter.
        Type `str`. """

    def __init__(self, name, valueBoolean, valueCode, valueDecimal, valueInteger, valueString, valueUri,):
        """ Initialize all valid properties.
        """
        self.name = name
        self.valueBoolean = valueBoolean
        self.valueCode = valueCode
        self.valueDecimal = valueDecimal
        self.valueInteger = valueInteger
        self.valueString = valueString
        self.valueUri = valueUri

    def __repr__(self):
        return '<ValueSetExpansionParameter %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import identifier