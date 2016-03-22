#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/EpisodeOfCare)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class EpisodeOfCare(domainresource.DomainResource):
    """ An association of a Patient with an Organization and  Healthcare
    Provider(s) for a period of time that the Organization assumes some level
    of responsibility.

    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during this
    time.
    """

    __tablename__ = "EpisodeOfCare"

    careManager = Column(FHIRReference)
    """ Care manager/care co-ordinator for the patient.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    careTeam = Column(EpisodeOfCareCareTeam)
    """ Other practitioners facilitating this episode of care.
        List of `EpisodeOfCareCareTeam` items (represented as `dict` in JSON). """

    condition = Column(FHIRReference)
    """ Conditions/problems/diagnoses this episode of care is for.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Identifier(s) for the EpisodeOfCare.
        List of `Identifier` items (represented as `dict` in JSON). """

    managingOrganization = Column(FHIRReference)
    """ Organization that assumes care.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    patient = Column(FHIRReference)
    """ Patient for this episode of care.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    period = Column(Period)
    """ Interval during responsibility is assumed.
        Type `Period` (represented as `dict` in JSON). """

    referralRequest = Column(FHIRReference)
    """ Originating Referral Request(s).
        List of `FHIRReference` items referencing `ReferralRequest` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ planned | waitlist | active | onhold | finished | cancelled.
        Type `str`. """

    statusHistory = Column(EpisodeOfCareStatusHistory)
    """ Past list of status codes.
        List of `EpisodeOfCareStatusHistory` items (represented as `dict` in JSON). """

    type = Column(CodeableConcept)
    """ Type/class  - e.g. specialist referral, disease management.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, careManager, careTeam, condition, identifier, managingOrganization, patient, period, referralRequest, status, statusHistory, type,):
        """ Initialize all valid properties.
        """
        self.careManager = careManager
        self.careTeam = careTeam
        self.condition = condition
        self.identifier = identifier
        self.managingOrganization = managingOrganization
        self.patient = patient
        self.period = period
        self.referralRequest = referralRequest
        self.status = status
        self.statusHistory = statusHistory
        self.type = type

    def __repr__(self):
        return '<EpisodeOfCare %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class EpisodeOfCareCareTeam(backboneelement.BackboneElement):
    """ Other practitioners facilitating this episode of care.

    The list of practitioners that may be facilitating this episode of care for
    specific purposes.
    """

    __tablename__ = "EpisodeOfCareCareTeam"

    member = Column(FHIRReference)
    """ The practitioner (or Organization) within the team.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """

    period = Column(Period)
    """ Period of time for this role.
        Type `Period` (represented as `dict` in JSON). """

    role = Column(CodeableConcept)
    """ Role taken by this team member.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, member, period, role,):
        """ Initialize all valid properties.
        """
        self.member = member
        self.period = period
        self.role = role

    def __repr__(self):
        return '<EpisodeOfCareCareTeam %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class EpisodeOfCareStatusHistory(backboneelement.BackboneElement):
    """ Past list of status codes.

    The history of statuses that the EpisodeOfCare has been through (without
    requiring processing the history of the resource).
    """

    __tablename__ = "EpisodeOfCareStatusHistory"

    period = Column(Period)
    """ Period for the status.
        Type `Period` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ planned | waitlist | active | onhold | finished | cancelled.
        Type `str`. """

    def __init__(self, period, status,):
        """ Initialize all valid properties.
        """
        self.period = period
        self.status = status

    def __repr__(self):
        return '<EpisodeOfCareStatusHistory %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import period