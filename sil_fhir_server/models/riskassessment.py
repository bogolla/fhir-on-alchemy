#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/RiskAssessment)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class RiskAssessmentPrediction(backboneelement.BackboneElement):
    """ Outcome predicted.

    Describes the expected outcome for the subject.
    """

    __tablename__ = "RiskAssessmentPrediction"

    outcome = Column(primitives.StringField,
                     ForeignKey('CodeableConcept.id'))
    """ Possible outcome for the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    probabilityCodeableConcept = Column(primitives.StringField,
                                        ForeignKey('CodeableConcept.id'))
    """ Likelihood of specified outcome.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    probabilityDecimal = Column(primitives.DecimalField)
    """ Likelihood of specified outcome.
        Type `float`. """

    probabilityRange = Column(primitives.StringField,
                              ForeignKey('Range.id'))
    """ Likelihood of specified outcome.
        Type `Range` (represented as `dict` in JSON). """

    rationale = Column(primitives.StringField)
    """ Explanation of prediction.
        Type `str`. """

    relativeRisk = Column(primitives.DecimalField)
    """ Relative likelihood.
        Type `float`. """

    whenPeriod = Column(primitives.StringField,
                        ForeignKey('Period.id'))
    """ Timeframe or age range.
        Type `Period` (represented as `dict` in JSON). """

    whenRange = Column(primitives.StringField,
                       ForeignKey('Range.id'))
    """ Timeframe or age range.
        Type `Range` (represented as `dict` in JSON). """

    def __init__(self, outcome, probabilityCodeableConcept, probabilityDecimal,
                 probabilityRange, rationale, relativeRisk, whenPeriod, whenRange,):
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


class RiskAssessment(domainresource.DomainResource):
    """ Potential outcomes for a subject with likelihood.

    An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """

    __tablename__ = "RiskAssessment"
    
    # todo basis = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    basis = Column(primitives.StringField)
    """ Information used in assessment.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
    
    # todo condition = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    condition = Column(primitives.StringField)
    """ Condition assessed.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """
    
    date = Column(primitives.DateTimeField)
    """ When was assessment made?.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    # todo encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ Where was assessment performed?.
        Type `FHIRReference` referencing `Encounter`
        (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Unique identifier for the assessment.
        Type `Identifier` (represented as `dict` in JSON). """
    
    method = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ Evaluation mechanism.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    mitigation = Column(primitives.StringField)
    """ How to reduce risk.
        Type `str`. """
    
    # todo performer = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    performer = Column(primitives.StringField)
    """ Who did assessment?.
        Type `FHIRReference` referencing `Practitioner, Device`
        (represented as `dict` in JSON). """
    
    prediction = Column(primitives.StringField,
                        ForeignKey('RiskAssessmentPrediction.id'))
    """ Outcome predicted.
        List of `RiskAssessmentPrediction` items
        (represented as `dict` in JSON). """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Who/what does assessment apply to?.
        Type `FHIRReference` referencing `Patient, Group`
        (represented as `dict` in JSON). """

    def __init__(self, basis, condition, date, encounter, identifier,
                 method, mitigation, performer, prediction, subject,):
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
