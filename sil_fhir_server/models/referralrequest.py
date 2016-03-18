#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ReferralRequest)
#  Date: 2016-03-18.


from . import domainresource

class ReferralRequest(domainresource.DomainResource):
    """ A request for referral or transfer of care.

    Used to record and send details about a request for referral service or
    transfer of a patient to the care of another provider or provider
    organization.
    """

    __tablename__ = "ReferralRequest"

    date = Column()
    """ Date of creation/activation.
        Type `FHIRDate` (represented as `str` in JSON). """

    dateSent = Column()
    """ Date referral/transfer of care request is sent.
        Type `FHIRDate` (represented as `str` in JSON). """

    description = Column()
    """ A textual description of the referral.
        Type `str`. """

    encounter = Column()
    """ Originating encounter.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    fulfillmentTime = Column()
    """ Requested service(s) fulfillment time.
        Type `Period` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    patient = Column()
    """ Patient referred to care or transfer.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    priority = Column()
    """ Urgency of referral / transfer of care request.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    reason = Column()
    """ Reason for referral / transfer of care request.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    recipient = Column(FHIRReference)
    """ Receiver of referral / transfer of care request.
        List of `FHIRReference` items referencing `Practitioner, Organization` (represented as `dict` in JSON). """

    requester = Column()
    """ Requester of referral / transfer of care.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient` (represented as `dict` in JSON). """

    serviceRequested = Column(CodeableConcept)
    """ Actions requested as part of the referral.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    specialty = Column()
    """ The clinical specialty (discipline) that the referral is requested
        for.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    status = Column()
    """ draft | requested | active | cancelled | accepted | rejected |
        completed.
        Type `str`. """

    supportingInformation = Column(FHIRReference)
    """ Additonal information to support referral or transfer of care
        request.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """

    type = Column()
    """ Referral/Transition of care request type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, date, dateSent, description, encounter, fulfillmentTime, identifier, patient, priority, reason, recipient, requester, serviceRequested, specialty, status, supportingInformation, type,):
        """ Initialize all valid properties.
        """
        self.date = date
        self.dateSent = dateSent
        self.description = description
        self.encounter = encounter
        self.fulfillmentTime = fulfillmentTime
        self.identifier = identifier
        self.patient = patient
        self.priority = priority
        self.reason = reason
        self.recipient = recipient
        self.requester = requester
        self.serviceRequested = serviceRequested
        self.specialty = specialty
        self.status = status
        self.supportingInformation = supportingInformation
        self.type = type

    def __repr__(self):
        return '<ReferralRequest %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period