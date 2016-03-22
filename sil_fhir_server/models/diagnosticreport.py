#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DiagnosticReport)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

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

    category = Column(CodeableConcept)
    """ Service category.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    code = Column(CodeableConcept)
    """ Name/Code for this diagnostic report.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    codedDiagnosis = Column(CodeableConcept)
    """ Codes for the conclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    conclusion = Column(primitives.StringField)
    """ Clinical Interpretation of test results.
        Type `str`. """

    effectiveDateTime = Column(FHIRDate)
    """ Clinically Relevant time/time-period for report.
        Type `FHIRDate` (represented as `str` in JSON). """

    effectivePeriod = Column(Period)
    """ Clinically Relevant time/time-period for report.
        Type `Period` (represented as `dict` in JSON). """

    encounter = Column(FHIRReference)
    """ Health care event when test ordered.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Id for external references to this report.
        List of `Identifier` items (represented as `dict` in JSON). """

    image = Column(DiagnosticReportImage)
    """ Key images associated with this report.
        List of `DiagnosticReportImage` items (represented as `dict` in JSON). """

    imagingStudy = Column(FHIRReference)
    """ Reference to full details of imaging associated with the diagnostic
        report.
        List of `FHIRReference` items referencing `ImagingStudy, ImagingObjectSelection` (represented as `dict` in JSON). """

    issued = Column(FHIRDate)
    """ DateTime this version was released.
        Type `FHIRDate` (represented as `str` in JSON). """

    performer = Column(FHIRReference)
    """ Responsible Diagnostic Service.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """

    presentedForm = Column(Attachment)
    """ Entire report as issued.
        List of `Attachment` items (represented as `dict` in JSON). """

    request = Column(FHIRReference)
    """ What was requested.
        List of `FHIRReference` items referencing `DiagnosticOrder, ProcedureRequest, ReferralRequest` (represented as `dict` in JSON). """

    result = Column(FHIRReference)
    """ Observations - simple, or complex nested groups.
        List of `FHIRReference` items referencing `Observation` (represented as `dict` in JSON). """

    specimen = Column(FHIRReference)
    """ Specimens this report is based on.
        List of `FHIRReference` items referencing `Specimen` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ registered | partial | final | corrected | appended | cancelled |
        entered-in-error.
        Type `str`. """

    subject = Column(FHIRReference)
    """ The subject of the report, usually, but not always, the patient.
        Type `FHIRReference` referencing `Patient, Group, Device, Location` (represented as `dict` in JSON). """

    def __init__(self, category, code, codedDiagnosis, conclusion, effectiveDateTime, effectivePeriod, encounter, identifier, image, imagingStudy, issued, performer, presentedForm, request, result, specimen, status, subject,):
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


from sqlalchemy import Column, Integer, String
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

    link = Column(FHIRReference)
    """ Reference to the image source.
        Type `FHIRReference` referencing `Media` (represented as `dict` in JSON). """

    def __init__(self, comment, link,):
        """ Initialize all valid properties.
        """
        self.comment = comment
        self.link = link

    def __repr__(self):
        return '<DiagnosticReportImage %r>' % 'self.property'  # replace self.property


from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period