#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Goal)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class GoalOutcome(backboneelement.BackboneElement):
    """ What was end result of goal?.

    Identifies the change (or lack of change) at the point where the goal was
    deepmed to be cancelled or achieved.
    """

    __tablename__ = "GoalOutcome"

    resultCodeableConcept = Column(primitives.StringField,
                                   ForeignKey('CodeableConcept.id'))
    """ Code or observation that resulted from goal.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    # todo resultReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    resultReference = Column(primitives.StringField)
    """ Code or observation that resulted from goal.
        Type `FHIRReference` referencing `Observation` (represented as `dict` in JSON). """

    def __init__(self, resultCodeableConcept, resultReference,):
        """ Initialize all valid properties.
        """
        self.resultCodeableConcept = resultCodeableConcept
        self.resultReference = resultReference

    def __repr__(self):
        return '<GoalOutcome %r>' % 'self.property'  # replace self.property


class Goal(domainresource.DomainResource):
    """ Describes the intended objective(s) for a patient, group or organization.

    Describes the intended objective(s) for a patient, group or organization
    care, for example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """

    __tablename__ = "Goal"
    
    # todo addresses = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    addresses = Column(primitives.StringField)
    """ Issues addressed by this goal.
        List of `FHIRReference` items referencing `Condition,
        Observation, MedicationStatement, NutritionOrder,
        ProcedureRequest, RiskAssessment` (represented as `dict` in JSON). """
    
    # todo author = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    author = Column(primitives.StringField)
    """ Who's responsible for creating Goal?.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson`
        (represented as `dict` in JSON). """
    
    category = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ E.g. Treatment, dietary, behavioral, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    description = Column(primitives.StringField)
    """ What's the desired outcome?.
        Type `str`. """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ External Ids for this goal.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    note = Column(primitives.StringField,
                  ForeignKey('Annotation.id'))
    """ Comments about the goal.
        List of `Annotation` items (represented as `dict` in JSON). """
    
    outcome = Column(primitives.StringField,
                     ForeignKey('GoalOutcome.id'))
    """ What was end result of goal?.
        List of `GoalOutcome` items (represented as `dict` in JSON). """
    
    priority = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ high | medium |low.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    startCodeableConcept = Column(primitives.StringField,
                                  ForeignKey('CodeableConcept.id'))
    """ When goal pursuit begins.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo startDate = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    startDate = Column(primitives.StringField)
    """ When goal pursuit begins.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    status = Column(primitives.StringField)
    """ proposed | planned | accepted | rejected | in-progress | achieved |
        sustaining | on-hold | cancelled.
        Type `str`. """
    
    # todo statusDate = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    statusDate = Column(primitives.StringField)
    """ When goal status took effect.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    statusReason = Column(primitives.StringField,
                          ForeignKey('CodeableConcept.id'))
    """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Who this goal is intended for.
        Type `FHIRReference` referencing `Patient, Group, Organization`
        (represented as `dict` in JSON). """
    
    targetDate = Column(primitives.DateTimeField)
    """ Reach goal on or before.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    targetQuantity = Column(primitives.StringField,
                            ForeignKey('Quantity.id'))
    """ Reach goal on or before.
        Type `Quantity` referencing `Duration` (represented as `dict` in JSON). """

    def __init__(self, addresses, author, category, description,
                 identifier, note, outcome, priority, startCodeableConcept,
                 startDate, status, statusDate, statusReason, subject,
                 targetDate, targetQuantity,):
        """ Initialize all valid properties.
        """
        self.addresses = addresses
        self.author = author
        self.category = category
        self.description = description
        self.identifier = identifier
        self.note = note
        self.outcome = outcome
        self.priority = priority
        self.startCodeableConcept = startCodeableConcept
        self.startDate = startDate
        self.status = status
        self.statusDate = statusDate
        self.statusReason = statusReason
        self.subject = subject
        self.targetDate = targetDate
        self.targetQuantity = targetQuantity

    def __repr__(self):
        return '<Goal %r>' % 'self.property'  # replace self.property
