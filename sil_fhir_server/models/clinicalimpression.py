#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ClinicalImpression)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource



from . import backboneelement


class ClinicalImpressionFinding(backboneelement.BackboneElement):
    """ Possible or likely findings and diagnoses.

    Specific findings or diagnoses that was considered likely or relevant to
    ongoing treatment.
    """

    __tablename__ = "ClinicalImpressionFinding"

    cause = Column(primitives.StringField)
    """ Which investigations support finding.
        Type `str`. """

    item = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Specific text or code for finding.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, cause, item,):
        """ Initialize all valid properties.
        """
        self.cause = cause
        self.item = item

    def __repr__(self):
        return '<ClinicalImpressionFinding %r>' % 'self.property'  # replace self.property


class ClinicalImpressionInvestigations(backboneelement.BackboneElement):
    """ One or more sets of investigations (signs, symptions, etc.).

    One or more sets of investigations (signs, symptions, etc.). The actual
    grouping of investigations vary greatly depending on the type and context
    of the assessment. These investigations may include data generated during
    the assessment process, or data previously generated and recorded that is
    pertinent to the outcomes.
    """

    __tablename__ = "ClinicalImpressionInvestigations"

    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ A name/code for the set.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    # todo item = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    item = Column(primitives.StringField)
    """ Record of a specific investigation.
        List of `FHIRReference` items referencing `Observation,
        QuestionnaireResponse, FamilyMemberHistory,
        DiagnosticReport` (represented as `dict` in JSON). """

    def __init__(self, code, item,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.item = item

    def __repr__(self):
        return '<ClinicalImpressionInvestigations %r>' % 'self.property'  # replace self.property


class ClinicalImpressionRuledOut(backboneelement.BackboneElement):
    """ Diagnosis considered not possible.
    """

    __tablename__ = "ClinicalImpressionRuledOut"

    item = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Specific text of code for diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    reason = Column(primitives.StringField)
    """ Grounds for elimination.
        Type `str`. """

    def __init__(self, item, reason,):
        """ Initialize all valid properties.
        """
        self.item = item
        self.reason = reason

    def __repr__(self):
        return '<ClinicalImpressionRuledOut %r>' % 'self.property'  # replace self.property


class ClinicalImpression(domainresource.DomainResource):
    """ A clinical assessment performed when planning treatments and management
    strategies for a patient.

    A record of a clinical assessment performed to determine what problem(s)
    may affect the patient and before planning the treatments or management
    strategies that are best to manage a patient's condition. Assessments are
    often 1:1 with a clinical consultation / encounter,  but this varies
    greatly depending on the clinical workflow. This resource is called
    "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion
    with the recording of assessment tools such as Apgar score.
    """

    __tablename__ = "ClinicalImpression"
    
    # todo action = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    action = Column(primitives.StringField)
    """ Actions taken during assessment.
        List of `FHIRReference` items referencing `ReferralRequest,
        ProcedureRequest, Procedure, MedicationOrder, DiagnosticOrder,
        NutritionOrder, SupplyRequest, Appointment` (represented as `dict` in JSON). """
    
    # todo assessor = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    assessor = Column(primitives.StringField)
    """ The clinician performing the assessment.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    date = Column(primitives.DateTimeField)
    """ When the assessment occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    description = Column(primitives.StringField)
    """ Why/how the assessment was performed.
        Type `str`. """
    
    finding = Column(primitives.StringField,
                     ForeignKey('ClinicalImpressionFinding.id'))
    """ Possible or likely findings and diagnoses.
        List of `ClinicalImpressionFinding` items (represented as `dict` in JSON). """
    
    investigations = Column(primitives.StringField,
                            ForeignKey(
                                'ClinicalImpressionInvestigations.id'))
    """ One or more sets of investigations (signs, symptions, etc.).
        List of `ClinicalImpressionInvestigations` items (represented as `dict` in JSON). """
    
    # todo patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    patient = Column(primitives.StringField)
    """ The patient being assessed.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    # todo plan = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    plan = Column(primitives.StringField)
    """ Plan of action after assessment.
        List of `FHIRReference` items referencing `CarePlan,
        Appointment, CommunicationRequest, DeviceUseRequest,
        DiagnosticOrder, MedicationOrder, NutritionOrder,
        Order, ProcedureRequest, ProcessRequest, ReferralRequest,
        SupplyRequest, VisionPrescription` (represented as `dict` in JSON). """
    
    # todo previous = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    previous = Column(primitives.StringField)
    """ Reference to last assessment.
        Type `FHIRReference` referencing `ClinicalImpression`
        (represented as `dict` in JSON). """
    
    # todo problem = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    problem = Column(primitives.StringField)
    """ General assessment of patient state.
        List of `FHIRReference` items referencing `Condition, AllergyIntolerance`
        (represented as `dict` in JSON). """
    
    prognosis = Column(primitives.StringField)
    """ Estimate of likely outcome.
        Type `str`. """
    
    protocol = Column(primitives.StringField)
    """ Clinical Protocol followed.
        Type `str`. """
    
    resolved = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Diagnoses/conditions resolved since previous assessment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    ruledOut = Column(primitives.StringField,
                      ForeignKey('ClinicalImpressionRuledOut.id'))
    """ Diagnosis considered not possible.
        List of `ClinicalImpressionRuledOut` items (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ in-progress | completed | entered-in-error.
        Type `str`. """
    
    summary = Column(primitives.StringField)
    """ Summary of the assessment.
        Type `str`. """
    
    triggerCodeableConcept = Column(primitives.StringField,
                                    ForeignKey('CodeableConcept.id'))
    """ Request or event that necessitated this assessment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo triggerReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    triggerReference = Column(primitives.StringField)
    """ Request or event that necessitated this assessment.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    def __init__(self, action, assessor, date, description, finding,
                 investigations, patient, plan, previous, problem,
                 prognosis, protocol, resolved, ruledOut, status,
                 summary, triggerCodeableConcept, triggerReference,):
        """ Initialize all valid properties.
        """
        self.action = action
        self.assessor = assessor
        self.date = date
        self.description = description
        self.finding = finding
        self.investigations = investigations
        self.patient = patient
        self.plan = plan
        self.previous = previous
        self.problem = problem
        self.prognosis = prognosis
        self.protocol = protocol
        self.resolved = resolved
        self.ruledOut = ruledOut
        self.status = status
        self.summary = summary
        self.triggerCodeableConcept = triggerCodeableConcept
        self.triggerReference = triggerReference

    def __repr__(self):
        return '<ClinicalImpression %r>' % 'self.property'  # replace self.property
