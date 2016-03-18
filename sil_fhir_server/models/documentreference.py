#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DocumentReference)
#  Date: 2016-03-18.


from . import domainresource

class DocumentReference(domainresource.DomainResource):
    """ A reference to a document.

    A reference to a document .
    """

    __tablename__ = "DocumentReference"

    authenticator = Column()
    """ Who/what authenticated the document.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """

    author = Column(FHIRReference)
    """ Who and/or what authored the document.
        List of `FHIRReference` items referencing `Practitioner, Organization, Device, Patient, RelatedPerson` (represented as `dict` in JSON). """

    class_fhir = Column()
    """ Categorization of document.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    content = Column(DocumentReferenceContent)
    """ Document referenced.
        List of `DocumentReferenceContent` items (represented as `dict` in JSON). """

    context = Column()
    """ Clinical context of document.
        Type `DocumentReferenceContext` (represented as `dict` in JSON). """

    created = Column()
    """ Document creation time.
        Type `FHIRDate` (represented as `str` in JSON). """

    custodian = Column()
    """ Organization which maintains the document.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    description = Column()
    """ Human-readable description (title).
        Type `str`. """

    docStatus = Column()
    """ preliminary | final | appended | amended | entered-in-error.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Other identifiers for the document.
        List of `Identifier` items (represented as `dict` in JSON). """

    indexed = Column()
    """ When this document reference created.
        Type `FHIRDate` (represented as `str` in JSON). """

    masterIdentifier = Column()
    """ Master Version Specific Identifier.
        Type `Identifier` (represented as `dict` in JSON). """

    relatesTo = Column(DocumentReferenceRelatesTo)
    """ Relationships to other documents.
        List of `DocumentReferenceRelatesTo` items (represented as `dict` in JSON). """

    securityLabel = Column(CodeableConcept)
    """ Document security-tags.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    status = Column()
    """ current | superseded | entered-in-error.
        Type `str`. """

    subject = Column()
    """ Who/what is the subject of the document.
        Type `FHIRReference` referencing `Patient, Practitioner, Group, Device` (represented as `dict` in JSON). """

    type = Column()
    """ Kind of document (LOINC if possible).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, authenticator, author, class_fhir, content, context, created, custodian, description, docStatus, identifier, indexed, masterIdentifier, relatesTo, securityLabel, status, subject, type,):
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


from . import backboneelement

class DocumentReferenceContent(backboneelement.BackboneElement):
    """ Document referenced.

    The document and format referenced. There may be multiple content element
    repetitions, each with a different format.
    """

    __tablename__ = "DocumentReferenceContent"

    attachment = Column()
    """ Where to access the document.
        Type `Attachment` (represented as `dict` in JSON). """

    format = Column(Coding)
    """ Format/content rules for the document.
        List of `Coding` items (represented as `dict` in JSON). """

    def __init__(self, attachment, format,):
        """ Initialize all valid properties.
        """
        self.attachment = attachment
        self.format = format

    def __repr__(self):
        return '<DocumentReferenceContent %r>' % 'self.property'  # replace self.property


class DocumentReferenceContext(backboneelement.BackboneElement):
    """ Clinical context of document.

    The clinical context in which the document was prepared.
    """

    __tablename__ = "DocumentReferenceContext"

    encounter = Column()
    """ Context of the document  content.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    event = Column(CodeableConcept)
    """ Main Clinical Acts Documented.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    facilityType = Column()
    """ Kind of facility where patient was seen.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    period = Column()
    """ Time of service that is being documented.
        Type `Period` (represented as `dict` in JSON). """

    practiceSetting = Column()
    """ Additional details about where the content was created (e.g.
        clinical specialty).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    related = Column(DocumentReferenceContextRelated)
    """ Related identifiers or resources.
        List of `DocumentReferenceContextRelated` items (represented as `dict` in JSON). """

    sourcePatientInfo = Column()
    """ Patient demographics from source.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    def __init__(self, encounter, event, facilityType, period, practiceSetting, related, sourcePatientInfo,):
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


class DocumentReferenceContextRelated(backboneelement.BackboneElement):
    """ Related identifiers or resources.

    Related identifiers or resources associated with the DocumentReference.
    """

    __tablename__ = "DocumentReferenceContextRelated"

    identifier = Column()
    """ Identifier of related objects or events.
        Type `Identifier` (represented as `dict` in JSON). """

    ref = Column()
    """ Related Resource.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

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

    code = Column()
    """ replaces | transforms | signs | appends.
        Type `str`. """

    target = Column()
    """ Target of the relationship.
        Type `FHIRReference` referencing `DocumentReference` (represented as `dict` in JSON). """

    def __init__(self, code, target,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.target = target

    def __repr__(self):
        return '<DocumentReferenceRelatesTo %r>' % 'self.property'  # replace self.property


from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period