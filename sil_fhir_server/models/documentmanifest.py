#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DocumentManifest)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class DocumentManifestContent(backboneelement.BackboneElement):
    """ The items included.

    The list of Documents included in the manifest.
    """

    __tablename__ = "DocumentManifestContent"

    pAttachment = Column(primitives.StringField,
                         ForeignKey('Attachment.id'))
    """ Contents of this set of documents.
        Type `Attachment` (represented as `dict` in JSON). """

    # todo pReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    pReference = Column(primitives.StringField)
    """ Contents of this set of documents.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    def __init__(self, pAttachment, pReference,):
        """ Initialize all valid properties.
        """
        self.pAttachment = pAttachment
        self.pReference = pReference

    def __repr__(self):
        return '<DocumentManifestContent %r>' % 'self.property'  # replace self.property


class DocumentManifestRelated(backboneelement.BackboneElement):
    """ Related things.

    Related identifiers or resources associated with the DocumentManifest.
    """

    __tablename__ = "DocumentManifestRelated"

    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Identifiers of things that are related.
        Type `Identifier` (represented as `dict` in JSON). """

    # todo ref = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    ref = Column(primitives.StringField)
    """ Related Resource.
        Type `FHIRReference` referencing `Resource`
        (represented as `dict` in JSON). """

    def __init__(self, identifier, ref,):
        """ Initialize all valid properties.
        """
        self.identifier = identifier
        self.ref = ref

    def __repr__(self):
        return '<DocumentManifestRelated %r>' % 'self.property'  # replace self.property


class DocumentManifest(domainresource.DomainResource):
    """ A manifest that defines a set of documents.
    """

    __tablename__ = "DocumentManifest"
    
    # todo author = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    author = Column(primitives.StringField)
    """ Who and/or what authored the manifest.
        List of `FHIRReference` items referencing `Practitioner,
        Organization, Device, Patient, RelatedPerson`
        (represented as `dict` in JSON). """
    
    content = Column(primitives.StringField,
                     ForeignKey('DocumentManifestContent.id'))
    """ The items included.
        List of `DocumentManifestContent` items (represented as `dict` in JSON). """
    
    created = Column(primitives.DateTimeField)
    """ When this document manifest created.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    description = Column(primitives.StringField)
    """ Human-readable description (title).
        Type `str`. """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Other identifiers for the manifest.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    masterIdentifier = Column(primitives.StringField,
                              ForeignKey('Identifier.id'))
    """ Unique Identifier for the set of documents.
        Type `Identifier` (represented as `dict` in JSON). """
    
    # todo recipient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    recipient = Column(primitives.StringField)
    """ Intended to get notified about this set of documents.
        List of `FHIRReference` items referencing `Patient,
        Practitioner, RelatedPerson, Organization` (represented as `dict` in JSON). """
    
    related = Column(primitives.StringField,
                     ForeignKey('DocumentManifestRelated.id'))
    """ Related things.
        List of `DocumentManifestRelated` items (represented as `dict` in JSON). """
    
    source = Column(primitives.StringField)
    """ The source system/application/software.
        Type `str`. """
    
    status = Column(primitives.StringField)
    """ current | superseded | entered-in-error.
        Type `str`. """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ The subject of the set of documents.
        Type `FHIRReference` referencing `Patient, Practitioner,
         Group, Device` (represented as `dict` in JSON). """
    
    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Kind of document set.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, author, content, created, description,
                 identifier, masterIdentifier, recipient,
                 related, source, status, subject, type,):
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
