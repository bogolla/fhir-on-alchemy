#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DocumentReference)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class DocumentReferenceContent(backboneelement.BackboneElement):
    """ Document referenced.

    The document and format referenced. There may be multiple content element
    repetitions, each with a different format.
    """

    __tablename__ = "DocumentReferenceContent"

    attachment = Column(primitives.StringField,
                        ForeignKey('Attachment.id'))
    """ Where to access the document.
        Type `Attachment` (represented as `dict` in JSON). """

    format = Column(primitives.StringField,
                    ForeignKey('Coding.id'))
    """ Format/content rules for the document.
        List of `Coding` items (represented as `dict` in JSON). """

    def __init__(self, attachment, format,):
        """ Initialize all valid properties.
        """
        self.attachment = attachment
        self.format = format

    def __repr__(self):
        return '<DocumentReferenceContent %r>' % 'self.property'  # replace self.property


class DocumentReferenceContextRelated(backboneelement.BackboneElement):
    """ Related identifiers or resources.

    Related identifiers or resources associated with the DocumentReference.
    """

    __tablename__ = "DocumentReferenceContextRelated"

    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Identifier of related objects or events.
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
        return '<DocumentReferenceContextRelated %r>' % 'self.property'  # replace self.property


class DocumentReferenceRelatesTo(backboneelement.BackboneElement):
    """ Relationships to other documents.

    Relationships that this document has with other document references that
    already exist.
    """

    __tablename__ = "DocumentReferenceRelatesTo"

    code = Column(primitives.StringField)
    """ replaces | transforms | signs | appends.
        Type `str`. """

    # todo target = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    target = Column(primitives.StringField)
    """ Target of the relationship.
        Type `FHIRReference` referencing `DocumentReference`
        (represented as `dict` in JSON). """

    def __init__(self, code, target,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.target = target

    def __repr__(self):
        return '<DocumentReferenceRelatesTo %r>' % 'self.property'  # replace self.property


class DocumentReferenceContext(backboneelement.BackboneElement):
    """ Clinical context of document.

    The clinical context in which the document was prepared.
    """

    __tablename__ = "DocumentReferenceContext"

    # todo encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ Context of the document  content.
        Type `FHIRReference` referencing `Encounter`
        (represented as `dict` in JSON). """

    event = Column(primitives.StringField,
                   ForeignKey('CodeableConcept.id'))
    """ Main Clinical Acts Documented.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    facilityType = Column(primitives.StringField,
                          ForeignKey('CodeableConcept.id'))
    """ Kind of facility where patient was seen.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    period = Column(primitives.StringField,
                    ForeignKey('Period.id'))
    """ Time of service that is being documented.
        Type `Period` (represented as `dict` in JSON). """

    practiceSetting = Column(primitives.StringField,
                             ForeignKey('CodeableConcept.id'))
    """ Additional details about where the content was created (e.g.
        clinical specialty).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    related = Column(primitives.StringField,
                     ForeignKey('DocumentReferenceContextRelated.id'))
    """ Related identifiers or resources.
        List of `DocumentReferenceContextRelated` items
        (represented as `dict` in JSON). """

    # todo sourcePatientInfo = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    sourcePatientInfo = Column(primitives.StringField)
    """ Patient demographics from source.
        Type `FHIRReference` referencing `Patient`
        (represented as `dict` in JSON). """

    def __init__(self, encounter, event, facilityType, period,
                 practiceSetting, related, sourcePatientInfo,):
        """ Initialize all valid properties.
        """
        self.encounter = encounter
        self.event = event
        self.facilityType = facilityType
        self.period = period
        self.practiceSetting = practiceSetting
        self.related = related
        self.sourcePatientInfo = sourcePatientInfo

    def __repr__(self):
        return '<DocumentReferenceContext %r>' % 'self.property'  # replace self.property


class DocumentReference(domainresource.DomainResource):
    """ A reference to a document.

    A reference to a document .
    """

    __tablename__ = "DocumentReference"
    
    # todo authenticator = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    authenticator = Column(primitives.StringField)
    """ Who/what authenticated the document.
        Type `FHIRReference` referencing `Practitioner, Organization`
        (represented as `dict` in JSON). """
    
    # todo author = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    author = Column(primitives.StringField)
    """ Who and/or what authored the document.
        List of `FHIRReference` items referencing `Practitioner,
        Organization, Device, Patient, RelatedPerson`
        (represented as `dict` in JSON). """
    
    class_fhir = Column(primitives.StringField,
                        ForeignKey('CodeableConcept.id'))
    """ Categorization of document.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    content = Column(primitives.StringField,
                     ForeignKey('DocumentReferenceContent.id'))
    """ Document referenced.
        List of `DocumentReferenceContent` items (represented as `dict` in JSON). """
    
    context = Column(primitives.StringField,
                     ForeignKey('DocumentReferenceContext.id'))
    """ Clinical context of document.
        Type `DocumentReferenceContext` (represented as `dict` in JSON). """
    
    created = Column(primitives.DateTimeField)
    """ Document creation time.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    # todo custodian = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    custodian = Column(primitives.StringField)
    """ Organization which maintains the document.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
    
    description = Column(primitives.StringField)
    """ Human-readable description (title).
        Type `str`. """
    
    docStatus = Column(primitives.StringField,
                       ForeignKey('CodeableConcept.id'))
    """ preliminary | final | appended | amended | entered-in-error.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Other identifiers for the document.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    indexed = Column(primitives.DateTimeField)
    """ When this document reference created.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    masterIdentifier = Column(primitives.StringField,
                              ForeignKey('Identifier.id'))
    """ Master Version Specific Identifier.
        Type `Identifier` (represented as `dict` in JSON). """
    
    relatesTo = Column(primitives.StringField,
                       ForeignKey('DocumentReferenceRelatesTo.id'))
    """ Relationships to other documents.
        List of `DocumentReferenceRelatesTo` items (represented as `dict` in JSON). """
    
    securityLabel = Column(primitives.StringField,
                           ForeignKey('CodeableConcept.id'))
    """ Document security-tags.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ current | superseded | entered-in-error.
        Type `str`. """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Who/what is the subject of the document.
        Type `FHIRReference` referencing `Patient, Practitioner, Group, Device`
        (represented as `dict` in JSON). """
    
    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Kind of document (LOINC if possible).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, authenticator, author, class_fhir, content, context,
                 created, custodian, description, docStatus, identifier,
                 indexed, masterIdentifier, relatesTo, securityLabel,
                 status, subject, type):
        """ Initialize all valid properties.
        """
        self.authenticator = authenticator
        self.author = author
        self.class_fhir = class_fhir
        self.content = content
        self.context = context
        self.created = created
        self.custodian = custodian
        self.description = description
        self.docStatus = docStatus
        self.identifier = identifier
        self.indexed = indexed
        self.masterIdentifier = masterIdentifier
        self.relatesTo = relatesTo
        self.securityLabel = securityLabel
        self.status = status
        self.subject = subject
        self.type = type

    def __repr__(self):
        return '<DocumentReference %r>' % 'self.property'  # replace self.property
