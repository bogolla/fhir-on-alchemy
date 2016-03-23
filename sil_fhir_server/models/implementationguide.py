#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ImplementationGuide)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource

class ImplementationGuide(domainresource.DomainResource):
    """ A set of rules about how FHIR is used.

    A set of rules or how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into a
    logical whole, and to publish a computable definition of all the parts.
    """

    __tablename__ = "ImplementationGuide"
    
    binary = Column(primitives.StringField)
    """ Image, css, script, etc..
        List of `str` items. """
    
    contact = Column(primitives.StringField, ForeignKey('ImplementationGuideContact.id'))
    """ Contact details of the publisher.
        List of `ImplementationGuideContact` items (represented as `dict` in JSON). """
    
    copyright = Column(primitives.StringField)
    """ Use and/or publishing restrictions.
        Type `str`. """
    
    date = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ Date for this version of the Implementation Guide.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    dependency = Column(primitives.StringField, ForeignKey('ImplementationGuideDependency.id'))
    """ Another Implementation guide this depends on.
        List of `ImplementationGuideDependency` items (represented as `dict` in JSON). """
    
    description = Column(primitives.StringField)
    """ Natural language description of the Implementation Guide.
        Type `str`. """
    
    experimental = Column(primitives.BooleanField)
    """ If for testing purposes, not real usage.
        Type `bool`. """
    
    fhirVersion = Column(primitives.StringField)
    """ FHIR Version this Implementation Guide targets.
        Type `str`. """
    
    global_fhir = Column(primitives.StringField, ForeignKey('ImplementationGuideGlobal.id'))
    """ Profiles that apply globally.
        List of `ImplementationGuideGlobal` items (represented as `dict` in JSON). """
    
    name = Column(primitives.StringField)
    """ Informal name for this Implementation Guide.
        Type `str`. """
    
    package = Column(primitives.StringField, ForeignKey('ImplementationGuidePackage.id'))
    """ Group of resources as used in .page.package.
        List of `ImplementationGuidePackage` items (represented as `dict` in JSON). """
    
    page = Column(primitives.StringField, ForeignKey('ImplementationGuidePage.id'))
    """ Page/Section in the Guide.
        Type `ImplementationGuidePage` (represented as `dict` in JSON). """
    
    publisher = Column(primitives.StringField)
    """ Name of the publisher (Organization or individual).
        Type `str`. """
    
    status = Column(primitives.StringField)
    """ draft | active | retired.
        Type `str`. """
    
    url = Column(primitives.StringField)
    """ Absolute URL used to reference this Implementation Guide.
        Type `str`. """
    
    useContext = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ The implementation guide is intended to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    version = Column(primitives.StringField)
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


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import backboneelement

class ImplementationGuideContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    __tablename__ = "ImplementationGuideContact"
    
    name = Column(primitives.StringField)
    """ Name of a individual to contact.
        Type `str`. """
    
    telecom = Column(primitives.StringField, ForeignKey('ContactPoint.id'))
    """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, name, telecom,):
        """ Initialize all valid properties.
        """
        self.name = name
        self.telecom = telecom

    def __repr__(self):
        return '<ImplementationGuideContact %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
class ImplementationGuideDependency(backboneelement.BackboneElement):
    """ Another Implementation guide this depends on.

    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """

    __tablename__ = "ImplementationGuideDependency"
    
    type = Column(primitives.StringField)
    """ reference | inclusion.
        Type `str`. """
    
    uri = Column(primitives.StringField)
    """ Where to find dependency.
        Type `str`. """

    def __init__(self, type, uri,):
        """ Initialize all valid properties.
        """
        self.type = type
        self.uri = uri

    def __repr__(self):
        return '<ImplementationGuideDependency %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
class ImplementationGuideGlobal(backboneelement.BackboneElement):
    """ Profiles that apply globally.

    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """

    __tablename__ = "ImplementationGuideGlobal"
    
    profile = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Profile that all resources must conform to.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
    
    type = Column(primitives.StringField)
    """ Type this profiles applies to.
        Type `str`. """

    def __init__(self, profile, type,):
        """ Initialize all valid properties.
        """
        self.profile = profile
        self.type = type

    def __repr__(self):
        return '<ImplementationGuideGlobal %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
class ImplementationGuidePackage(backboneelement.BackboneElement):
    """ Group of resources as used in .page.package.

    A logical group of resources. Logical groups can be used when building
    pages.
    """

    __tablename__ = "ImplementationGuidePackage"
    
    description = Column(primitives.StringField)
    """ Human readable text describing the package.
        Type `str`. """
    
    name = Column(primitives.StringField)
    """ Name used .page.package.
        Type `str`. """
    
    resource = Column(primitives.StringField, ForeignKey('ImplementationGuidePackageResource.id'))
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


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
class ImplementationGuidePackageResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.

    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, conformance statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """

    __tablename__ = "ImplementationGuidePackageResource"
    
    acronym = Column(primitives.StringField)
    """ Short code to identify the resource.
        Type `str`. """
    
    description = Column(primitives.StringField)
    """ Reason why included in guide.
        Type `str`. """
    
    exampleFor = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Resource this is an example of (if applicable).
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
    
    name = Column(primitives.StringField)
    """ Human Name for the resource.
        Type `str`. """
    
    purpose = Column(primitives.StringField)
    """ example | terminology | profile | extension | dictionary | logical.
        Type `str`. """
    
    sourceReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Location of the resource.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
    
    sourceUri = Column(primitives.StringField)
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


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
class ImplementationGuidePage(backboneelement.BackboneElement):
    """ Page/Section in the Guide.

    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """

    __tablename__ = "ImplementationGuidePage"
    
    format = Column(primitives.StringField)
    """ Format of the page (e.g. html, markdown, etc.).
        Type `str`. """
    
    kind = Column(primitives.StringField)
    """ page | example | list | include | directory | dictionary | toc |
        resource.
        Type `str`. """
    
    name = Column(primitives.StringField)
    """ Short name shown for navigational assistance.
        Type `str`. """
    
    package = Column(primitives.StringField)
    """ Name of package to include.
        List of `str` items. """
    
    page = Column(primitives.StringField, ForeignKey('ImplementationGuidePage.id'))
    """ Nested Pages / Sections.
        List of `ImplementationGuidePage` items (represented as `dict` in JSON). """
    
    source = Column(primitives.StringField)
    """ Where to find that page.
        Type `str`. """
    
    type = Column(primitives.StringField)
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