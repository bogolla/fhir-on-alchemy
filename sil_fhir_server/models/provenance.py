#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Provenance)
#  Date: 2016-03-18.


from . import domainresource

class Provenance(domainresource.DomainResource):
    """ Who, What, When for a set of resources.

    Provenance of a resource is a record that describes entities and processes
    involved in producing and delivering or otherwise influencing that
    resource. Provenance provides a critical foundation for assessing
    authenticity, enabling trust, and allowing reproducibility. Provenance
    assertions are a form of contextual metadata and can themselves become
    important records with their own provenance. Provenance statement indicates
    clinical significance in terms of confidence in authenticity, reliability,
    and trustworthiness, integrity, and stage in lifecycle (e.g. Document
    Completion - has the artifact been legally authenticated), all of which may
    impact security, privacy, and trust policies.
    """

    __tablename__ = "Provenance"

    activity = Column()
    """ Activity that occurred.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    agent = Column(ProvenanceAgent)
    """ Agents involved in creating resource.
        List of `ProvenanceAgent` items (represented as `dict` in JSON). """

    entity = Column(ProvenanceEntity)
    """ An entity used in this activity.
        List of `ProvenanceEntity` items (represented as `dict` in JSON). """

    location = Column()
    """ Where the activity occurred, if relevant.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """

    period = Column()
    """ When the activity occurred.
        Type `Period` (represented as `dict` in JSON). """

    policy = Column(str)
    """ Policy or plan the activity was defined by.
        List of `str` items. """

    reason = Column(CodeableConcept)
    """ Reason the activity is occurring.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    recorded = Column()
    """ When the activity was recorded / updated.
        Type `FHIRDate` (represented as `str` in JSON). """

    signature = Column(Signature)
    """ Signature on target.
        List of `Signature` items (represented as `dict` in JSON). """

    target = Column(FHIRReference)
    """ Target Reference(s) (usually version specific).
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """

    def __init__(self, activity, agent, entity, location, period, policy, reason, recorded, signature, target,):
        """ Initialize all valid properties.
        """
        self.activity = activity
        self.agent = agent
        self.entity = entity
        self.location = location
        self.period = period
        self.policy = policy
        self.reason = reason
        self.recorded = recorded
        self.signature = signature
        self.target = target

    def __repr__(self):
        return '<Provenance %r>' % 'self.property'  # replace self.property


from . import backboneelement

class ProvenanceAgent(backboneelement.BackboneElement):
    """ Agents involved in creating resource.

    An agent takes a role in an activity such that the agent can be assigned
    some degree of responsibility for the activity taking place. An agent can
    be a person, an organization, software, or other entities that may be
    ascribed responsibility.
    """

    __tablename__ = "ProvenanceAgent"

    actor = Column()
    """ Individual, device or organization playing role.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient, Device, Organization` (represented as `dict` in JSON). """

    relatedAgent = Column(ProvenanceAgentRelatedAgent)
    """ Track delegation between agents.
        List of `ProvenanceAgentRelatedAgent` items (represented as `dict` in JSON). """

    role = Column()
    """ What the agents involvement was.
        Type `Coding` (represented as `dict` in JSON). """

    userId = Column()
    """ Authorization-system identifier for the agent.
        Type `Identifier` (represented as `dict` in JSON). """

    def __init__(self, actor, relatedAgent, role, userId,):
        """ Initialize all valid properties.
        """
        self.actor = actor
        self.relatedAgent = relatedAgent
        self.role = role
        self.userId = userId

    def __repr__(self):
        return '<ProvenanceAgent %r>' % 'self.property'  # replace self.property


class ProvenanceAgentRelatedAgent(backboneelement.BackboneElement):
    """ Track delegation between agents.

    A relationship between two the agents referenced in this resource. This is
    defined to allow for explicit description of the delegation between agents.
    For example, this human author used this device, or one person acted on
    another's behest.
    """

    __tablename__ = "ProvenanceAgentRelatedAgent"

    target = Column()
    """ Reference to other agent in this resource by identifier.
        Type `str`. """

    type = Column()
    """ Type of relationship between agents.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, target, type,):
        """ Initialize all valid properties.
        """
        self.target = target
        self.type = type

    def __repr__(self):
        return '<ProvenanceAgentRelatedAgent %r>' % 'self.property'  # replace self.property


class ProvenanceEntity(backboneelement.BackboneElement):
    """ An entity used in this activity.
    """

    __tablename__ = "ProvenanceEntity"

    agent = Column()
    """ Entity is attributed to this agent.
        Type `ProvenanceAgent` (represented as `dict` in JSON). """

    display = Column()
    """ Human description of entity.
        Type `str`. """

    reference = Column()
    """ Identity of entity.
        Type `str`. """

    role = Column()
    """ derivation | revision | quotation | source.
        Type `str`. """

    type = Column()
    """ The type of resource in this entity.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, agent, display, reference, role, type,):
        """ Initialize all valid properties.
        """
        self.agent = agent
        self.display = display
        self.reference = reference
        self.role = role
        self.type = type

    def __repr__(self):
        return '<ProvenanceEntity %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import signature