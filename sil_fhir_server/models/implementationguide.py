#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ImplementationGuide)
#  Date: 2016-03-18.


from . import domainresource

class ImplementationGuide(domainresource.DomainResource):
    """ A set of rules about how FHIR is used.

    A set of rules or how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into a
    logical whole, and to publish a computable definition of all the parts.
    """

    __tablename__ = "ImplementationGuide"

    binary = Column(str)
    """ Image, css, script, etc..
        List of `str` items. """

    contact = Column(ImplementationGuideContact)
    """ Contact details of the publisher.
        List of `ImplementationGuideContact` items (represented as `dict` in JSON). """

    copyright = Column()
    """ Use and/or publishing restrictions.
        Type `str`. """

    date = Column()
    """ Date for this version of the Implementation Guide.
        Type `FHIRDate` (represented as `str` in JSON). """

    dependency = Column(ImplementationGuideDependency)
    """ Another Implementation guide this depends on.
        List of `ImplementationGuideDependency` items (represented as `dict` in JSON). """

    description = Column()
    """ Natural language description of the Implementation Guide.
        Type `str`. """

    experimental = Column()
    """ If for testing purposes, not real usage.
        Type `bool`. """

    fhirVersion = Column()
    """ FHIR Version this Implementation Guide targets.
        Type `str`. """

    global_fhir = Column(ImplementationGuideGlobal)
    """ Profiles that apply globally.
        List of `ImplementationGuideGlobal` items (represented as `dict` in JSON). """

    name = Column()
    """ Informal name for this Implementation Guide.
        Type `str`. """

    package = Column(ImplementationGuidePackage)
    """ Group of resources as used in .page.package.
        List of `ImplementationGuidePackage` items (represented as `dict` in JSON). """

    page = Column()
    """ Page/Section in the Guide.
        Type `ImplementationGuidePage` (represented as `dict` in JSON). """

    publisher = Column()
    """ Name of the publisher (Organization or individual).
        Type `str`. """

    status = Column()
    """ draft | active | retired.
        Type `str`. """

    url = Column()
    """ Absolute URL used to reference this Implementation Guide.
        Type `str`. """

    useContext = Column(CodeableConcept)
    """ The implementation guide is intended to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    version = Column()
    """ Logical id for this version of the Implementation Guide.
        Type `str`. """

    def __init__(self, binary, contact, copyright, date, dependency, description, experimental, fhirVersion, global_fhir, name, package, page, publisher, status, url, useContext, version,):
        """ Initialize all valid properties.
        """
        self.binary = binary
        self.contact = contact
        self.copyright = copyright
        self.date = date
        self.dependency = dependency
        self.description = description
        self.experimental = experimental
        self.fhirVersion = fhirVersion
        self.global_fhir = global_fhir
        self.name = name
        self.package = package
        self.page = page
        self.publisher = publisher
        self.status = status
        self.url = url
        self.useContext = useContext
        self.version = version

    def __repr__(self):
        return '<ImplementationGuide %r>' % 'self.property'  # replace self.property


from . import backboneelement

class ImplementationGuideContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    __tablename__ = "ImplementationGuideContact"

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
        return '<ImplementationGuideContact %r>' % 'self.property'  # replace self.property


class ImplementationGuideDependency(backboneelement.BackboneElement):
    """ Another Implementation guide this depends on.

    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """

    __tablename__ = "ImplementationGuideDependency"

    type = Column()
    """ reference | inclusion.
        Type `str`. """

    uri = Column()
    """ Where to find dependency.
        Type `str`. """

    def __init__(self, type, uri,):
        """ Initialize all valid properties.
        """
        self.type = type
        self.uri = uri

    def __repr__(self):
        return '<ImplementationGuideDependency %r>' % 'self.property'  # replace self.property


class ImplementationGuideGlobal(backboneelement.BackboneElement):
    """ Profiles that apply globally.

    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """

    __tablename__ = "ImplementationGuideGlobal"

    profile = Column()
    """ Profile that all resources must conform to.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """

    type = Column()
    """ Type this profiles applies to.
        Type `str`. """

    def __init__(self, profile, type,):
        """ Initialize all valid properties.
        """
        self.profile = profile
        self.type = type

    def __repr__(self):
        return '<ImplementationGuideGlobal %r>' % 'self.property'  # replace self.property


class ImplementationGuidePackage(backboneelement.BackboneElement):
    """ Group of resources as used in .page.package.

    A logical group of resources. Logical groups can be used when building
    pages.
    """

    __tablename__ = "ImplementationGuidePackage"

    description = Column()
    """ Human readable text describing the package.
        Type `str`. """

    name = Column()
    """ Name used .page.package.
        Type `str`. """

    resource = Column(ImplementationGuidePackageResource)
    """ Resource in the implementation guide.
        List of `ImplementationGuidePackageResource` items (represented as `dict` in JSON). """

    def __init__(self, description, name, resource,):
        """ Initialize all valid properties.
        """
        self.description = description
        self.name = name
        self.resource = resource

    def __repr__(self):
        return '<ImplementationGuidePackage %r>' % 'self.property'  # replace self.property


class ImplementationGuidePackageResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.

    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, conformance statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """

    __tablename__ = "ImplementationGuidePackageResource"

    acronym = Column()
    """ Short code to identify the resource.
        Type `str`. """

    description = Column()
    """ Reason why included in guide.
        Type `str`. """

    exampleFor = Column()
    """ Resource this is an example of (if applicable).
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """

    name = Column()
    """ Human Name for the resource.
        Type `str`. """

    purpose = Column()
    """ example | terminology | profile | extension | dictionary | logical.
        Type `str`. """

    sourceReference = Column()
    """ Location of the resource.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    sourceUri = Column()
    """ Location of the resource.
        Type `str`. """

    def __init__(self, acronym, description, exampleFor, name, purpose, sourceReference, sourceUri,):
        """ Initialize all valid properties.
        """
        self.acronym = acronym
        self.description = description
        self.exampleFor = exampleFor
        self.name = name
        self.purpose = purpose
        self.sourceReference = sourceReference
        self.sourceUri = sourceUri

    def __repr__(self):
        return '<ImplementationGuidePackageResource %r>' % 'self.property'  # replace self.property


class ImplementationGuidePage(backboneelement.BackboneElement):
    """ Page/Section in the Guide.

    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """

    __tablename__ = "ImplementationGuidePage"

    format = Column()
    """ Format of the page (e.g. html, markdown, etc.).
        Type `str`. """

    kind = Column()
    """ page | example | list | include | directory | dictionary | toc |
        resource.
        Type `str`. """

    name = Column()
    """ Short name shown for navigational assistance.
        Type `str`. """

    package = Column(str)
    """ Name of package to include.
        List of `str` items. """

    page = Column(ImplementationGuidePage)
    """ Nested Pages / Sections.
        List of `ImplementationGuidePage` items (represented as `dict` in JSON). """

    source = Column()
    """ Where to find that page.
        Type `str`. """

    type = Column(str)
    """ Kind of resource to include in the list.
        List of `str` items. """

    def __init__(self, format, kind, name, package, page, source, type,):
        """ Initialize all valid properties.
        """
        self.format = format
        self.kind = kind
        self.name = name
        self.package = package
        self.page = page
        self.source = source
        self.type = type

    def __repr__(self):
        return '<ImplementationGuidePage %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference