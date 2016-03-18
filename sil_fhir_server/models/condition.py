#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Condition)
#  Date: 2016-03-18.


from . import domainresource

class Condition(domainresource.DomainResource):
    """ Detailed information about conditions, problems or diagnoses.

    Use to record detailed information about conditions, problems or diagnoses
    recognized by a clinician. There are many uses including: recording a
    diagnosis during an encounter; populating a problem list or a summary
    statement, such as a discharge summary.
    """

    __tablename__ = "Condition"

    abatementBoolean = Column()
    """ If/when in resolution/remission.
        Type `bool`. """

    abatementDateTime = Column()
    """ If/when in resolution/remission.
        Type `FHIRDate` (represented as `str` in JSON). """

    abatementPeriod = Column()
    """ If/when in resolution/remission.
        Type `Period` (represented as `dict` in JSON). """

    abatementQuantity = Column()
    """ If/when in resolution/remission.
        Type `Quantity` referencing `Age` (represented as `dict` in JSON). """

    abatementRange = Column()
    """ If/when in resolution/remission.
        Type `Range` (represented as `dict` in JSON). """

    abatementString = Column()
    """ If/when in resolution/remission.
        Type `str`. """

    asserter = Column()
    """ Person who asserts this condition.
        Type `FHIRReference` referencing `Practitioner, Patient` (represented as `dict` in JSON). """

    bodySite = Column(CodeableConcept)
    """ Anatomical location, if relevant.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    category = Column()
    """ complaint | symptom | finding | diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    clinicalStatus = Column()
    """ active | relapse | remission | resolved.
        Type `str`. """

    code = Column()
    """ Identification of the condition, problem or diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    dateRecorded = Column()
    """ When first entered.
        Type `FHIRDate` (represented as `str` in JSON). """

    encounter = Column()
    """ Encounter when condition first asserted.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    evidence = Column(ConditionEvidence)
    """ Supporting evidence.
        List of `ConditionEvidence` items (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ External Ids for this condition.
        List of `Identifier` items (represented as `dict` in JSON). """

    notes = Column()
    """ Additional information about the Condition.
        Type `str`. """

    onsetDateTime = Column()
    """ Estimated or actual date,  date-time, or age.
        Type `FHIRDate` (represented as `str` in JSON). """

    onsetPeriod = Column()
    """ Estimated or actual date,  date-time, or age.
        Type `Period` (represented as `dict` in JSON). """

    onsetQuantity = Column()
    """ Estimated or actual date,  date-time, or age.
        Type `Quantity` referencing `Age` (represented as `dict` in JSON). """

    onsetRange = Column()
    """ Estimated or actual date,  date-time, or age.
        Type `Range` (represented as `dict` in JSON). """

    onsetString = Column()
    """ Estimated or actual date,  date-time, or age.
        Type `str`. """

    patient = Column()
    """ Who has the condition?.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    severity = Column()
    """ Subjective severity of condition.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    stage = Column()
    """ Stage/grade, usually assessed formally.
        Type `ConditionStage` (represented as `dict` in JSON). """

    verificationStatus = Column()
    """ provisional | differential | confirmed | refuted | entered-in-error
        | unknown.
        Type `str`. """

    def __init__(self, abatementBoolean, abatementDateTime, abatementPeriod, abatementQuantity, abatementRange, abatementString, asserter, bodySite, category, clinicalStatus, code, dateRecorded, encounter, evidence, identifier, notes, onsetDateTime, onsetPeriod, onsetQuantity, onsetRange, onsetString, patient, severity, stage, verificationStatus,):
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


from . import backboneelement

class ConditionEvidence(backboneelement.BackboneElement):
    """ Supporting evidence.

    Supporting Evidence / manifestations that are the basis on which this
    condition is suspected or confirmed.
    """

    __tablename__ = "ConditionEvidence"

    code = Column()
    """ Manifestation/symptom.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    detail = Column(FHIRReference)
    """ Supporting information found elsewhere.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """

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

    assessment = Column(FHIRReference)
    """ Formal record of assessment.
        List of `FHIRReference` items referencing `ClinicalImpression, DiagnosticReport, Observation` (represented as `dict` in JSON). """

    summary = Column()
    """ Simple summary (disease specific).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, assessment, summary,):
        """ Initialize all valid properties.
        """
        self.assessment = assessment
        self.summary = summary

    def __repr__(self):
        return '<ConditionStage %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range