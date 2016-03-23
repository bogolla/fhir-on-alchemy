#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Condition)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class ConditionEvidence(backboneelement.BackboneElement):
    """ Supporting evidence.

    Supporting Evidence / manifestations that are the basis on which this
    condition is suspected or confirmed.
    """

    __tablename__ = "ConditionEvidence"

    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Manifestation/symptom.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    # todo detail = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    detail = Column(primitives.StringField)
    """ Supporting information found elsewhere.
        List of `FHIRReference` items referencing `Resource`
        (represented as `dict` in JSON). """

    def __init__(self, code, detail,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.detail = detail

    def __repr__(self):
        return '<ConditionEvidence %r>' % 'self.property'  # replace self.property


class ConditionStage(backboneelement.BackboneElement):
    """ Stage/grade, usually assessed formally.

    Clinical stage or grade of a condition. May include formal severity
    assessments.
    """

    __tablename__ = "ConditionStage"

    # todo assessment = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    assessment = Column(primitives.StringField)
    """ Formal record of assessment.
        List of `FHIRReference` items referencing `ClinicalImpression,
        DiagnosticReport, Observation` (represented as `dict` in JSON). """

    summary = Column(primitives.StringField,
                     ForeignKey('CodeableConcept.id'))
    """ Simple summary (disease specific).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, assessment, summary,):
        """ Initialize all valid properties.
        """
        self.assessment = assessment
        self.summary = summary

    def __repr__(self):
        return '<ConditionStage %r>' % 'self.property'  # replace self.property


class Condition(domainresource.DomainResource):
    """ Detailed information about conditions, problems or diagnoses.

    Use to record detailed information about conditions, problems or diagnoses
    recognized by a clinician. There are many uses including: recording a
    diagnosis during an encounter; populating a problem list or a summary
    statement, such as a discharge summary.
    """

    __tablename__ = "Condition"
    
    abatementBoolean = Column(primitives.BooleanField)
    """ If/when in resolution/remission.
        Type `bool`. """
    
    abatementDateTime = Column(primitives.DateTimeField)
    """ If/when in resolution/remission.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    abatementPeriod = Column(primitives.StringField,
                             ForeignKey('Period.id'))
    """ If/when in resolution/remission.
        Type `Period` (represented as `dict` in JSON). """
    
    abatementQuantity = Column(primitives.StringField,
                               ForeignKey('Quantity.id'))
    """ If/when in resolution/remission.
        Type `Quantity` referencing `Age`
        (represented as `dict` in JSON). """
    
    abatementRange = Column(primitives.StringField,
                            ForeignKey('Range.id'))
    """ If/when in resolution/remission.
        Type `Range` (represented as `dict` in JSON). """
    
    abatementString = Column(primitives.StringField)
    """ If/when in resolution/remission.
        Type `str`. """
    
    # todo asserter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    asserter = Column(primitives.StringField)
    """ Person who asserts this condition.
        Type `FHIRReference` referencing `Practitioner,
        Patient` (represented as `dict` in JSON). """
    
    bodySite = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Anatomical location, if relevant.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    category = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ complaint | symptom | finding | diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    clinicalStatus = Column(primitives.StringField)
    """ active | relapse | remission | resolved.
        Type `str`. """
    
    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Identification of the condition, problem or diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    dateRecorded = Column(primitives.DateTimeField)
    """ When first entered.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    # todo encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ Encounter when condition first asserted.
        Type `FHIRReference` referencing `Encounter`
        (represented as `dict` in JSON). """
    
    evidence = Column(primitives.StringField,
                      ForeignKey('ConditionEvidence.id'))
    """ Supporting evidence.
        List of `ConditionEvidence` items (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ External Ids for this condition.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    notes = Column(primitives.StringField)
    """ Additional information about the Condition.
        Type `str`. """
    
    onsetDateTime = Column(primitives.DateTimeField)
    """ Estimated or actual date,  date-time, or age.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    onsetPeriod = Column(primitives.StringField,
                         ForeignKey('Period.id'))
    """ Estimated or actual date,  date-time, or age.
        Type `Period` (represented as `dict` in JSON). """
    
    onsetQuantity = Column(primitives.StringField,
                           ForeignKey('Quantity.id'))
    """ Estimated or actual date,  date-time, or age.
        Type `Quantity` referencing `Age` (represented as `dict` in JSON). """
    
    onsetRange = Column(primitives.StringField,
                        ForeignKey('Range.id'))
    """ Estimated or actual date,  date-time, or age.
        Type `Range` (represented as `dict` in JSON). """
    
    onsetString = Column(primitives.StringField)
    """ Estimated or actual date,  date-time, or age.
        Type `str`. """
    
    # todo patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ Who has the condition?.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    severity = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Subjective severity of condition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    stage = Column(primitives.StringField,
                   ForeignKey('ConditionStage.id'))
    """ Stage/grade, usually assessed formally.
        Type `ConditionStage` (represented as `dict` in JSON). """
    
    verificationStatus = Column(primitives.StringField)
    """ provisional | differential | confirmed | refuted | entered-in-error
        | unknown.
        Type `str`. """

    def __init__(self, abatementBoolean, abatementDateTime,
                 abatementPeriod, abatementQuantity, abatementRange,
                 abatementString, asserter, bodySite, category,
                 clinicalStatus, code, dateRecorded, encounter,
                 evidence, identifier, notes, onsetDateTime, onsetPeriod,
                 onsetQuantity, onsetRange, onsetString, patient,
                 severity, stage, verificationStatus,):
        """ Initialize all valid properties.
        """
        self.abatementBoolean = abatementBoolean
        self.abatementDateTime = abatementDateTime
        self.abatementPeriod = abatementPeriod
        self.abatementQuantity = abatementQuantity
        self.abatementRange = abatementRange
        self.abatementString = abatementString
        self.asserter = asserter
        self.bodySite = bodySite
        self.category = category
        self.clinicalStatus = clinicalStatus
        self.code = code
        self.dateRecorded = dateRecorded
        self.encounter = encounter
        self.evidence = evidence
        self.identifier = identifier
        self.notes = notes
        self.onsetDateTime = onsetDateTime
        self.onsetPeriod = onsetPeriod
        self.onsetQuantity = onsetQuantity
        self.onsetRange = onsetRange
        self.onsetString = onsetString
        self.patient = patient
        self.severity = severity
        self.stage = stage
        self.verificationStatus = verificationStatus

    def __repr__(self):
        return '<Condition %r>' % 'self.property'  # replace self.property
