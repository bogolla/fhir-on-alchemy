#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DocumentManifest)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class DocumentManifest(domainresource.DomainResource):
    """ A manifest that defines a set of documents.
    """

    __tablename__ = "DocumentManifest"

    author = Column(FHIRReference)
    """ Who and/or what authored the manifest.
        List of `FHIRReference` items referencing `Practitioner, Organization, Device, Patient, RelatedPerson` (represented as `dict` in JSON). """

    content = Column(DocumentManifestContent)
    """ The items included.
        List of `DocumentManifestContent` items (represented as `dict` in JSON). """

    created = Column(FHIRDate)
    """ When this document manifest created.
        Type `FHIRDate` (represented as `str` in JSON). """

    description = Column(primitives.StringField)
    """ Human-readable description (title).
        Type `str`. """

    identifier = Column(Identifier)
    """ Other identifiers for the manifest.
        List of `Identifier` items (represented as `dict` in JSON). """

    masterIdentifier = Column(Identifier)
    """ Unique Identifier for the set of documents.
        Type `Identifier` (represented as `dict` in JSON). """

    recipient = Column(FHIRReference)
    """ Intended to get notified about this set of documents.
        List of `FHIRReference` items referencing `Patient, Practitioner, RelatedPerson, Organization` (represented as `dict` in JSON). """

    related = Column(DocumentManifestRelated)
    """ Related things.
        List of `DocumentManifestRelated` items (represented as `dict` in JSON). """

    source = Column(primitives.StringField)
    """ The source system/application/software.
        Type `str`. """

    status = Column(primitives.StringField)
    """ current | superseded | entered-in-error.
        Type `str`. """

    subject = Column(FHIRReference)
    """ The subject of the set of documents.
        Type `FHIRReference` referencing `Patient, Practitioner, Group, Device` (represented as `dict` in JSON). """

    type = Column(CodeableConcept)
    """ Kind of document set.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, author, content, created, description, identifier, masterIdentifier, recipient, related, source, status, subject, type,):
        """ Initialize all valid properties.
        """
        self.author = author
        self.content = content
        self.created = created
        self.description = description
        self.identifier = identifier
        self.masterIdentifier = masterIdentifier
        self.recipient = recipient
        self.related = related
        self.source = source
        self.status = status
        self.subject = subject
        self.type = type

    def __repr__(self):
        return '<DocumentManifest %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class DocumentManifestContent(backboneelement.BackboneElement):
    """ The items included.

    The list of Documents included in the manifest.
    """

    __tablename__ = "DocumentManifestContent"

    pAttachment = Column(Attachment)
    """ Contents of this set of documents.
        Type `Attachment` (represented as `dict` in JSON). """

    pReference = Column(FHIRReference)
    """ Contents of this set of documents.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    def __init__(self, pAttachment, pReference,):
        """ Initialize all valid properties.
        """
        self.pAttachment = pAttachment
        self.pReference = pReference

    def __repr__(self):
        return '<DocumentManifestContent %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class DocumentManifestRelated(backboneelement.BackboneElement):
    """ Related things.

    Related identifiers or resources associated with the DocumentManifest.
    """

    __tablename__ = "DocumentManifestRelated"

    identifier = Column(Identifier)
    """ Identifiers of things that are related.
        Type `Identifier` (represented as `dict` in JSON). """

    ref = Column(FHIRReference)
    """ Related Resource.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    def __init__(self, identifier, ref,):
        """ Initialize all valid properties.
        """
        self.identifier = identifier
        self.ref = ref

    def __repr__(self):
        return '<DocumentManifestRelated %r>' % 'self.property'  # replace self.property


from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier