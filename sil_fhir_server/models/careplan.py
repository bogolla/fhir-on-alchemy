#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/CarePlan)
#  Date: 2016-03-18.


from . import domainresource

class CarePlan(domainresource.DomainResource):
    """ Healthcare plan for patient or group.

    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient, group or community for a period of time,
    possibly limited to care for a specific condition or set of conditions.
    """

    __tablename__ = "CarePlan"

    activity = Column(CarePlanActivity)
    """ Action to occur as part of plan.
        List of `CarePlanActivity` items (represented as `dict` in JSON). """

    addresses = Column(FHIRReference)
    """ Health issues this plan addresses.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """

    author = Column(FHIRReference)
    """ Who is responsible for contents of the plan.
        List of `FHIRReference` items referencing `Patient, Practitioner, RelatedPerson, Organization` (represented as `dict` in JSON). """

    category = Column(CodeableConcept)
    """ Type of plan.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    context = Column()
    """ Created in context of.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """

    description = Column()
    """ Summary of nature of plan.
        Type `str`. """

    goal = Column(FHIRReference)
    """ Desired outcome of plan.
        List of `FHIRReference` items referencing `Goal` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ External Ids for this plan.
        List of `Identifier` items (represented as `dict` in JSON). """

    modified = Column()
    """ When last updated.
        Type `FHIRDate` (represented as `str` in JSON). """

    note = Column()
    """ Comments about the plan.
        Type `Annotation` (represented as `dict` in JSON). """

    participant = Column(CarePlanParticipant)
    """ Who's involved in plan?.
        List of `CarePlanParticipant` items (represented as `dict` in JSON). """

    period = Column()
    """ Time period plan covers.
        Type `Period` (represented as `dict` in JSON). """

    relatedPlan = Column(CarePlanRelatedPlan)
    """ Plans related to this one.
        List of `CarePlanRelatedPlan` items (represented as `dict` in JSON). """

    status = Column()
    """ proposed | draft | active | completed | cancelled.
        Type `str`. """

    subject = Column()
    """ Who care plan is for.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """

    support = Column(FHIRReference)
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


from . import backboneelement

class CarePlanActivity(backboneelement.BackboneElement):
    """ Action to occur as part of plan.

    Identifies a planned action to occur as part of the plan.  For example, a
    medication to be used, lab tests to perform, self-monitoring, education,
    etc.
    """

    __tablename__ = "CarePlanActivity"

    actionResulting = Column(FHIRReference)
    """ Appointments, orders, etc..
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """

    detail = Column()
    """ In-line definition of activity.
        Type `CarePlanActivityDetail` (represented as `dict` in JSON). """

    progress = Column(Annotation)
    """ Comments about the activity status/progress.
        List of `Annotation` items (represented as `dict` in JSON). """

    reference = Column()
    """ Activity details defined in specific resource.
        Type `FHIRReference` referencing `Appointment, CommunicationRequest, DeviceUseRequest, DiagnosticOrder, MedicationOrder, NutritionOrder, Order, ProcedureRequest, ProcessRequest, ReferralRequest, SupplyRequest, VisionPrescription` (represented as `dict` in JSON). """

    def __init__(self, actionResulting, detail, progress, reference,):
        """ Initialize all valid properties.
        """
        self.actionResulting = actionResulting
        self.detail = detail
        self.progress = progress
        self.reference = reference

    def __repr__(self):
        return '<CarePlanActivity %r>' % 'self.property'  # replace self.property


class CarePlanActivityDetail(backboneelement.BackboneElement):
    """ In-line definition of activity.

    A simple summary of a planned activity suitable for a general care plan
    system (e.g. form driven) that doesn't know about specific resources such
    as procedure etc.
    """

    __tablename__ = "CarePlanActivityDetail"

    category = Column()
    """ diet | drug | encounter | observation | procedure | supply | other.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    code = Column()
    """ Detail type of activity.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    dailyAmount = Column()
    """ How to consume/day?.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    description = Column()
    """ Extra info describing activity to perform.
        Type `str`. """

    goal = Column(FHIRReference)
    """ Goals this activity relates to.
        List of `FHIRReference` items referencing `Goal` (represented as `dict` in JSON). """

    location = Column()
    """ Where it should happen.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """

    performer = Column(FHIRReference)
    """ Who will be responsible?.
        List of `FHIRReference` items referencing `Practitioner, Organization, RelatedPerson, Patient` (represented as `dict` in JSON). """

    productCodeableConcept = Column()
    """ What is to be administered/supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    productReference = Column()
    """ What is to be administered/supplied.
        Type `FHIRReference` referencing `Medication, Substance` (represented as `dict` in JSON). """

    prohibited = Column()
    """ Do NOT do.
        Type `bool`. """

    quantity = Column()
    """ How much to administer/supply/consume.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    reasonCode = Column(CodeableConcept)
    """ Why activity should be done.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    reasonReference = Column(FHIRReference)
    """ Condition triggering need for activity.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """

    scheduledPeriod = Column()
    """ When activity is to occur.
        Type `Period` (represented as `dict` in JSON). """

    scheduledString = Column()
    """ When activity is to occur.
        Type `str`. """

    scheduledTiming = Column()
    """ When activity is to occur.
        Type `Timing` (represented as `dict` in JSON). """

    status = Column()
    """ not-started | scheduled | in-progress | on-hold | completed |
        cancelled.
        Type `str`. """

    statusReason = Column()
    """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, category, code, dailyAmount, description, goal, location, performer, productCodeableConcept, productReference, prohibited, quantity, reasonCode, reasonReference, scheduledPeriod, scheduledString, scheduledTiming, status, statusReason,):
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


class CarePlanParticipant(backboneelement.BackboneElement):
    """ Who's involved in plan?.

    Identifies all people and organizations who are expected to be involved in
    the care envisioned by this plan.
    """

    __tablename__ = "CarePlanParticipant"

    member = Column()
    """ Who is involved.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient, Organization` (represented as `dict` in JSON). """

    role = Column()
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

    code = Column()
    """ includes | replaces | fulfills.
        Type `str`. """

    plan = Column()
    """ Plan relationship exists with.
        Type `FHIRReference` referencing `CarePlan` (represented as `dict` in JSON). """

    def __init__(self, code, plan,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.plan = plan

    def __repr__(self):
        return '<CarePlanRelatedPlan %r>' % 'self.property'  # replace self.property


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import timing