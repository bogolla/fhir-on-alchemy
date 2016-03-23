#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/CarePlan)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class CarePlanActivityDetail(backboneelement.BackboneElement):
    """ In-line definition of activity.

    A simple summary of a planned activity suitable for a general care plan
    system (e.g. form driven) that doesn't know about specific resources such
    as procedure etc.
    """

    __tablename__ = "CarePlanActivityDetail"

    category = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ diet | drug | encounter | observation | procedure | supply | other.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Detail type of activity.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    dailyAmount = Column(primitives.StringField,
                         ForeignKey('Quantity.id'))
    """ How to consume/day?.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    description = Column(primitives.StringField)
    """ Extra info describing activity to perform.
        Type `str`. """

    # todo goal = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    goal = Column(primitives.StringField)
    """ Goals this activity relates to.
        List of `FHIRReference` items referencing `Goal` (represented as `dict` in JSON). """

    # todo location = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    location = Column(primitives.StringField)
    """ Where it should happen.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """

    # todo performer = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    performer = Column(primitives.StringField)
    """ Who will be responsible?.
        List of `FHIRReference` items referencing `Practitioner, Organization, RelatedPerson, Patient` (represented as `dict` in JSON). """

    productCodeableConcept = Column(primitives.StringField,
                                    ForeignKey('CodeableConcept.id'))
    """ What is to be administered/supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    # todo productReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    productReference = Column(primitives.StringField)
    """ What is to be administered/supplied.
        Type `FHIRReference` referencing `Medication, Substance` (represented as `dict` in JSON). """

    prohibited = Column(primitives.BooleanField)
    """ Do NOT do.
        Type `bool`. """

    quantity = Column(primitives.StringField,
                      ForeignKey('Quantity.id'))
    """ How much to administer/supply/consume.
        Type `Quantity` referencing `SimpleQuantity` (represented as
        `dict` in JSON). """

    reasonCode = Column(primitives.StringField,
                        ForeignKey('CodeableConcept.id'))
    """ Why activity should be done.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    # todo reasonReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    reasonReference = Column(primitives.StringField)
    """ Condition triggering need for activity.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """

    scheduledPeriod = Column(primitives.StringField,
                             ForeignKey('Period.id'))
    """ When activity is to occur.
        Type `Period` (represented as `dict` in JSON). """

    scheduledString = Column(primitives.StringField)
    """ When activity is to occur.
        Type `str`. """

    scheduledTiming = Column(primitives.StringField,
                             ForeignKey('Timing.id'))
    """ When activity is to occur.
        Type `Timing` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ not-started | scheduled | in-progress | on-hold | completed |
        cancelled.
        Type `str`. """

    statusReason = Column(primitives.StringField,
                          ForeignKey('CodeableConcept.id'))
    """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, category, code, dailyAmount, description, goal,
                 location, performer, productCodeableConcept,
                 productReference, prohibited, quantity, reasonCode,
                 reasonReference, scheduledPeriod, scheduledString,
                 scheduledTiming, status, statusReason,):
        """ Initialize all valid properties.
        """
        self.category = category
        self.code = code
        self.dailyAmount = dailyAmount
        self.description = description
        self.goal = goal
        self.location = location
        self.performer = performer
        self.productCodeableConcept = productCodeableConcept
        self.productReference = productReference
        self.prohibited = prohibited
        self.quantity = quantity
        self.reasonCode = reasonCode
        self.reasonReference = reasonReference
        self.scheduledPeriod = scheduledPeriod
        self.scheduledString = scheduledString
        self.scheduledTiming = scheduledTiming
        self.status = status
        self.statusReason = statusReason

    def __repr__(self):
        return '<CarePlanActivityDetail %r>' % 'self.property'  # replace self.property


class CarePlanActivity(backboneelement.BackboneElement):
    """ Action to occur as part of plan.

    Identifies a planned action to occur as part of the plan.  For example, a
    medication to be used, lab tests to perform, self-monitoring, education,
    etc.
    """

    __tablename__ = "CarePlanActivity"

    # todo actionResulting = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    actionResulting = Column(primitives.StringField)
    """ Appointments, orders, etc..
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """

    detail = Column(primitives.StringField,
                    ForeignKey('CarePlanActivityDetail.id'))
    """ In-line definition of activity.
        Type `CarePlanActivityDetail` (represented as `dict` in JSON). """

    progress = Column(primitives.StringField,
                      ForeignKey('Annotation.id'))
    """ Comments about the activity status/progress.
        List of `Annotation` items (represented as `dict` in JSON). """

    #todo reference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    reference = Column(primitives.StringField)
    """ Activity details defined in specific resource.
        Type `FHIRReference` referencing `Appointment,
        CommunicationRequest, DeviceUseRequest, DiagnosticOrder,
        MedicationOrder, NutritionOrder, Order, ProcedureRequest,
        ProcessRequest, ReferralRequest, SupplyRequest,
        VisionPrescription` (represented as `dict` in JSON). """

    def __init__(self, actionResulting, detail, progress, reference,):
        """ Initialize all valid properties.
        """
        self.actionResulting = actionResulting
        self.detail = detail
        self.progress = progress
        self.reference = reference

    def __repr__(self):
        return '<CarePlanActivity %r>' % 'self.property'  # replace self.property


class CarePlanParticipant(backboneelement.BackboneElement):
    """ Who's involved in plan?.

    Identifies all people and organizations who are expected to be involved in
    the care envisioned by this plan.
    """

    __tablename__ = "CarePlanParticipant"

    # todo member = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    member = Column(primitives.StringField)
    """ Who is involved.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson,
        Patient, Organization` (represented as `dict` in JSON). """

    role = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Type of involvement.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, member, role,):
        """ Initialize all valid properties.
        """
        self.member = member
        self.role = role

    def __repr__(self):
        return '<CarePlanParticipant %r>' % 'self.property'  # replace self.property


class CarePlanRelatedPlan(backboneelement.BackboneElement):
    """ Plans related to this one.

    Identifies CarePlans with some sort of formal relationship to the current
    plan.
    """

    __tablename__ = "CarePlanRelatedPlan"

    code = Column(primitives.StringField)
    """ includes | replaces | fulfills.
        Type `str`. """

    # todo plan = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    plan = Column(primitives.StringField)
    """ Plan relationship exists with.
        Type `FHIRReference` referencing `CarePlan` (represented as `dict` in JSON). """

    def __init__(self, code, plan,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.plan = plan

    def __repr__(self):
        return '<CarePlanRelatedPlan %r>' % 'self.property'  # replace self.property


class CarePlan(domainresource.DomainResource):
    """ Healthcare plan for patient or group.

    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient, group or community for a period of time,
    possibly limited to care for a specific condition or set of conditions.
    """

    __tablename__ = "CarePlan"
    
    activity = Column(primitives.StringField,
                      ForeignKey('CarePlanActivity.id'))
    """ Action to occur as part of plan.
        List of `CarePlanActivity` items (represented as `dict` in JSON). """
    
    # todo addresses = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    addresses = Column(primitives.StringField)
    """ Health issues this plan addresses.
        List of `FHIRReference` items referencing `Condition`
        (represented as `dict` in JSON). """
    
    # todo author = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    author = Column(primitives.StringField)
    """ Who is responsible for contents of the plan.
        List of `FHIRReference` items referencing `Patient,
        Practitioner, RelatedPerson, Organization` (represented as `dict` in JSON). """
    
    category = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Type of plan.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    # todo context = Column(primitives.StringField,
    #                  ForeignKey('FHIRReference.id'))
    context = Column(primitives.StringField)
    """ Created in context of.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare`
        (represented as `dict` in JSON). """
    
    description = Column(primitives.StringField)
    """ Summary of nature of plan.
        Type `str`. """
    
    # todo goal = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    goal = Column(primitives.StringField)
    """ Desired outcome of plan.
        List of `FHIRReference` items referencing `Goal`
        (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ External Ids for this plan.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    modified = Column(primitives.DateTimeField)
    """ When last updated.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    note = Column(primitives.StringField, ForeignKey('Annotation.id'))
    """ Comments about the plan.
        Type `Annotation` (represented as `dict` in JSON). """
    
    participant = Column(primitives.StringField,
                         ForeignKey('CarePlanParticipant.id'))
    """ Who's involved in plan?.
        List of `CarePlanParticipant` items (represented as `dict` in JSON). """
    
    period = Column(primitives.StringField, ForeignKey('Period.id'))
    """ Time period plan covers.
        Type `Period` (represented as `dict` in JSON). """
    
    relatedPlan = Column(primitives.StringField,
                         ForeignKey('CarePlanRelatedPlan.id'))
    """ Plans related to this one.
        List of `CarePlanRelatedPlan` items (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ proposed | draft | active | completed | cancelled.
        Type `str`. """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Who care plan is for.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
    
    # todo support = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    support = Column(primitives.StringField)
    """ Information considered as part of plan.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """

    def __init__(self, activity, addresses, author, category, context, description, goal, identifier, modified, note, participant, period, relatedPlan, status, subject, support,):
        """ Initialize all valid properties.
        """
        self.activity = activity
        self.addresses = addresses
        self.author = author
        self.category = category
        self.context = context
        self.description = description
        self.goal = goal
        self.identifier = identifier
        self.modified = modified
        self.note = note
        self.participant = participant
        self.period = period
        self.relatedPlan = relatedPlan
        self.status = status
        self.subject = subject
        self.support = support

    def __repr__(self):
        return '<CarePlan %r>' % 'self.property'  # replace self.property
