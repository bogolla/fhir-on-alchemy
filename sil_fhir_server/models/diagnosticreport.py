#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DiagnosticReport)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class DiagnosticReportImage(backboneelement.BackboneElement):
    """ Key images associated with this report.

    A list of key images associated with this report. The images are generally
    created during the diagnostic process, and may be directly of the patient,
    or of treated specimens (i.e. slides of interest).
    """

    __tablename__ = "DiagnosticReportImage"

    comment = Column(primitives.StringField)
    """ Comment about the image (e.g. explanation).
        Type `str`. """

    # todo link = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    link = Column(primitives.StringField)
    """ Reference to the image source.
        Type `FHIRReference` referencing `Media` (represented as `dict` in JSON). """

    def __init__(self, comment, link,):
        """ Initialize all valid properties.
        """
        self.comment = comment
        self.link = link

    def __repr__(self):
        return '<DiagnosticReportImage %r>' % 'self.property'  # replace self.property


class DiagnosticReport(domainresource.DomainResource):
    """ A Diagnostic report - a combination of request information, atomic results,
    images, interpretation, as well as formatted reports.

    The findings and interpretation of diagnostic  tests performed on patients,
    groups of patients, devices, and locations, and/or specimens derived from
    these. The report includes clinical context such as requesting and provider
    information, and some mix of atomic results, images, textual and coded
    interpretations, and formatted representation of diagnostic reports.
    """

    __tablename__ = "DiagnosticReport"
    
    category = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Service category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Name/Code for this diagnostic report.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    codedDiagnosis = Column(primitives.StringField,
                            ForeignKey('CodeableConcept.id'))
    """ Codes for the conclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    conclusion = Column(primitives.StringField)
    """ Clinical Interpretation of test results.
        Type `str`. """
    
    effectiveDateTime = Column(primitives.DateTimeField)
    """ Clinically Relevant time/time-period for report.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    effectivePeriod = Column(primitives.StringField,
                             ForeignKey('Period.id'))
    """ Clinically Relevant time/time-period for report.
        Type `Period` (represented as `dict` in JSON). """
    
    # todo encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ Health care event when test ordered.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Id for external references to this report.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    image = Column(primitives.StringField,
                   ForeignKey('DiagnosticReportImage.id'))
    """ Key images associated with this report.
        List of `DiagnosticReportImage` items (represented as `dict` in JSON). """
    
    # todo imagingStudy = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    imagingStudy = Column(primitives.StringField)
    """ Reference to full details of imaging associated with the diagnostic
        report.
        List of `FHIRReference` items referencing `ImagingStudy,
        ImagingObjectSelection` (represented as `dict` in JSON). """
    
    issued = Column(primitives.DateTimeField)
    """ DateTime this version was released.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    # todo performer = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    performer = Column(primitives.StringField)
    """ Responsible Diagnostic Service.
        Type `FHIRReference` referencing `Practitioner, Organization`
        (represented as `dict` in JSON). """
    
    presentedForm = Column(primitives.StringField,
                           ForeignKey('Attachment.id'))
    """ Entire report as issued.
        List of `Attachment` items (represented as `dict` in JSON). """
    
    # todo request = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    request = Column(primitives.StringField)
    """ What was requested.
        List of `FHIRReference` items referencing `DiagnosticOrder,
        ProcedureRequest, ReferralRequest` (represented as `dict` in JSON). """
    
    # todo result = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    result = Column(primitives.StringField)
    """ Observations - simple, or complex nested groups.
        List of `FHIRReference` items referencing `Observation`
        (represented as `dict` in JSON). """
    
    # todo specimen = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    specimen = Column(primitives.StringField)
    """ Specimens this report is based on.
        List of `FHIRReference` items referencing `Specimen`
        (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ registered | partial | final | corrected | appended | cancelled |
        entered-in-error.
        Type `str`. """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ The subject of the report, usually, but not always, the patient.
        Type `FHIRReference` referencing `Patient, Group, Device, Location`
        (represented as `dict` in JSON). """

    def __init__(self, category, code, codedDiagnosis, conclusion,
                 effectiveDateTime, effectivePeriod, encounter,
                 identifier, image, imagingStudy, issued, performer,
                 presentedForm, request, result, specimen, status, subject,):
        """ Initialize all valid properties.
        """
        self.category = category
        self.code = code
        self.codedDiagnosis = codedDiagnosis
        self.conclusion = conclusion
        self.effectiveDateTime = effectiveDateTime
        self.effectivePeriod = effectivePeriod
        self.encounter = encounter
        self.identifier = identifier
        self.image = image
        self.imagingStudy = imagingStudy
        self.issued = issued
        self.performer = performer
        self.presentedForm = presentedForm
        self.request = request
        self.result = result
        self.specimen = specimen
        self.status = status
        self.subject = subject

    def __repr__(self):
        return '<DiagnosticReport %r>' % 'self.property'  # replace self.property
