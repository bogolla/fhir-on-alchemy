#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/RiskAssessment)
#  Date: 2016-03-18.


from . import domainresource

class RiskAssessment(domainresource.DomainResource):
    """ Potential outcomes for a subject with likelihood.

    An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """

    __tablename__ = "RiskAssessment"

    basis = Column(FHIRReference)
    """ Information used in assessment.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """

    condition = Column()
    """ Condition assessed.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """

    date = Column()
    """ When was assessment made?.
        Type `FHIRDate` (represented as `str` in JSON). """

    encounter = Column()
    """ Where was assessment performed?.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    identifier = Column()
    """ Unique identifier for the assessment.
        Type `Identifier` (represented as `dict` in JSON). """

    method = Column()
    """ Evaluation mechanism.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    mitigation = Column()
    """ How to reduce risk.
        Type `str`. """

    performer = Column()
    """ Who did assessment?.
        Type `FHIRReference` referencing `Practitioner, Device` (represented as `dict` in JSON). """

    prediction = Column(RiskAssessmentPrediction)
    """ Outcome predicted.
        List of `RiskAssessmentPrediction` items (represented as `dict` in JSON). """

    subject = Column()
    """ Who/what does assessment apply to?.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """

    def __init__(self, basis, condition, date, encounter, identifier, method, mitigation, performer, prediction, subject,):
        """ Initialize all valid properties.
        """
        self.basis = basis
        self.condition = condition
        self.date = date
        self.encounter = encounter
        self.identifier = identifier
        self.method = method
        self.mitigation = mitigation
        self.performer = performer
        self.prediction = prediction
        self.subject = subject

    def __repr__(self):
        return '<RiskAssessment %r>' % 'self.property'  # replace self.property


from . import backboneelement

class RiskAssessmentPrediction(backboneelement.BackboneElement):
    """ Outcome predicted.

    Describes the expected outcome for the subject.
    """

    __tablename__ = "RiskAssessmentPrediction"

    outcome = Column()
    """ Possible outcome for the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    probabilityCodeableConcept = Column()
    """ Likelihood of specified outcome.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    probabilityDecimal = Column()
    """ Likelihood of specified outcome.
        Type `float`. """

    probabilityRange = Column()
    """ Likelihood of specified outcome.
        Type `Range` (represented as `dict` in JSON). """

    rationale = Column()
    """ Explanation of prediction.
        Type `str`. """

    relativeRisk = Column()
    """ Relative likelihood.
        Type `float`. """

    whenPeriod = Column()
    """ Timeframe or age range.
        Type `Period` (represented as `dict` in JSON). """

    whenRange = Column()
    """ Timeframe or age range.
        Type `Range` (represented as `dict` in JSON). """

    def __init__(self, outcome, probabilityCodeableConcept, probabilityDecimal, probabilityRange, rationale, relativeRisk, whenPeriod, whenRange,):
        """ Initialize all valid properties.
        """
        self.outcome = outcome
        self.probabilityCodeableConcept = probabilityCodeableConcept
        self.probabilityDecimal = probabilityDecimal
        self.probabilityRange = probabilityRange
        self.rationale = rationale
        self.relativeRisk = relativeRisk
        self.whenPeriod = whenPeriod
        self.whenRange = whenRange

    def __repr__(self):
        return '<RiskAssessmentPrediction %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import range