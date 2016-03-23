#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Encounter)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class EncounterHospitalization(backboneelement.BackboneElement):
    """ Details about the admission to a healthcare service.
    """

    __tablename__ = "EncounterHospitalization"

    admitSource = Column(primitives.StringField,
                         ForeignKey('CodeableConcept.id'))
    """ From where patient was admitted (physician referral, transfer).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    # todo admittingDiagnosis = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    admittingDiagnosis = Column(primitives.StringField)
    """ The admitting diagnosis as reported by admitting practitioner.
        List of `FHIRReference` items referencing `Condition`
        (represented as `dict` in JSON). """

    # todo destination = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    destination = Column(primitives.StringField)
    """ Location to which the patient is discharged.
        Type `FHIRReference` referencing `Location`
        (represented as `dict` in JSON). """

    dietPreference = Column(primitives.StringField,
                            ForeignKey('CodeableConcept.id'))
    """ Diet preferences reported by the patient.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    # todo dischargeDiagnosis = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    dischargeDiagnosis = Column(primitives.StringField)
    """ The final diagnosis given a patient before release from the
        hospital after all testing, surgery, and workup are complete.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """

    dischargeDisposition = Column(primitives.StringField,
                                  ForeignKey('CodeableConcept.id'))
    """ Category or kind of location after discharge.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    # todo origin = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    origin = Column(primitives.StringField)
    """ The location from which the patient came before admission.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """

    preAdmissionIdentifier = Column(primitives.StringField,
                                    ForeignKey('Identifier.id'))
    """ Pre-admission identifier.
        Type `Identifier` (represented as `dict` in JSON). """

    reAdmission = Column(primitives.StringField,
                         ForeignKey('CodeableConcept.id'))
    """ The type of hospital re-admission that has occurred (if any). If
        the value is absent, then this is not identified as a readmission.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    specialArrangement = Column(primitives.StringField,
                                ForeignKey('CodeableConcept.id'))
    """ Wheelchair, translator, stretcher, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    specialCourtesy = Column(primitives.StringField,
                             ForeignKey('CodeableConcept.id'))
    """ Special courtesies (VIP, board member).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, admitSource, admittingDiagnosis, destination,
                 dietPreference, dischargeDiagnosis, dischargeDisposition,
                 origin, preAdmissionIdentifier, reAdmission,
                 specialArrangement, specialCourtesy,):
        """ Initialize all valid properties.
        """
        self.admitSource = admitSource
        self.admittingDiagnosis = admittingDiagnosis
        self.destination = destination
        self.dietPreference = dietPreference
        self.dischargeDiagnosis = dischargeDiagnosis
        self.dischargeDisposition = dischargeDisposition
        self.origin = origin
        self.preAdmissionIdentifier = preAdmissionIdentifier
        self.reAdmission = reAdmission
        self.specialArrangement = specialArrangement
        self.specialCourtesy = specialCourtesy

    def __repr__(self):
        return '<EncounterHospitalization %r>' % 'self.property'  # replace self.property


class EncounterLocation(backboneelement.BackboneElement):
    """ List of locations where the patient has been.

    List of locations where  the patient has been during this encounter.
    """

    __tablename__ = "EncounterLocation"

    # todo location = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    location = Column(primitives.StringField)
    """ Location the encounter takes place.
        Type `FHIRReference` referencing `Location`
        (represented as `dict` in JSON). """

    period = Column(primitives.StringField,
                    ForeignKey('Period.id'))
    """ Time period during which the patient was present at the location.
        Type `Period` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ planned | active | reserved | completed.
        Type `str`. """

    def __init__(self, location, period, status,):
        """ Initialize all valid properties.
        """
        self.location = location
        self.period = period
        self.status = status

    def __repr__(self):
        return '<EncounterLocation %r>' % 'self.property'  # replace self.property


class EncounterParticipant(backboneelement.BackboneElement):
    """ List of participants involved in the encounter.

    The list of people responsible for providing the service.
    """

    __tablename__ = "EncounterParticipant"

    # todo individual = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    individual = Column(primitives.StringField)
    """ Persons involved in the encounter other than the patient.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson`
        (represented as `dict` in JSON). """

    period = Column(primitives.StringField,
                    ForeignKey('Period.id'))
    """ Period of time during the encounter participant was present.
        Type `Period` (represented as `dict` in JSON). """

    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Role of participant in encounter.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, individual, period, type,):
        """ Initialize all valid properties.
        """
        self.individual = individual
        self.period = period
        self.type = type

    def __repr__(self):
        return '<EncounterParticipant %r>' % 'self.property'  # replace self.property


class EncounterStatusHistory(backboneelement.BackboneElement):
    """ List of past encounter statuses.

    The status history permits the encounter resource to contain the status
    history without needing to read through the historical versions of the
    resource, or even have the server store them.
    """

    __tablename__ = "EncounterStatusHistory"

    period = Column(primitives.StringField,
                    ForeignKey('Period.id'))
    """ The time that the episode was in the specified status.
        Type `Period` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ planned | arrived | in-progress | onleave | finished | cancelled.
        Type `str`. """

    def __init__(self, period, status,):
        """ Initialize all valid properties.
        """
        self.period = period
        self.status = status

    def __repr__(self):
        return '<EncounterStatusHistory %r>' % 'self.property'  # replace self.property


class Encounter(domainresource.DomainResource):
    """ An interaction during which services are provided to the patient.

    An interaction between a patient and healthcare provider(s) for the purpose
    of providing healthcare service(s) or assessing the health status of a
    patient.
    """

    __tablename__ = "Encounter"
    
    # todo appointment = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    appointment = Column(primitives.StringField)
    """ The appointment that scheduled this encounter.
        Type `FHIRReference` referencing `Appointment` (represented as `dict` in JSON). """
    
    class_fhir = Column(primitives.StringField)
    """ inpatient | outpatient | ambulatory | emergency +.
        Type `str`. """
    
    # todo episodeOfCare = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    episodeOfCare = Column(primitives.StringField)
    """ Episode(s) of care that this encounter should be recorded against.
        List of `FHIRReference` items referencing
        `EpisodeOfCare` (represented as `dict` in JSON). """
    
    hospitalization = Column(primitives.StringField,
                             ForeignKey('EncounterHospitalization.id'))
    """ Details about the admission to a healthcare service.
        Type `EncounterHospitalization` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Identifier(s) by which this encounter is known.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    # todo incomingReferral = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    incomingReferral = Column(primitives.StringField)
    """ The ReferralRequest that initiated this encounter.
        List of `FHIRReference` items referencing `ReferralRequest`
         (represented as `dict` in JSON). """
    
    # todo indication = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    indication = Column(primitives.StringField)
    """ Reason the encounter takes place (resource).
        List of `FHIRReference` items referencing `Condition,
        Procedure` (represented as `dict` in JSON). """
    
    length = Column(primitives.StringField,
                    ForeignKey('Quantity.id'))
    """ Quantity of time the encounter lasted (less time absent).
        Type `Quantity` referencing `Duration`
        (represented as `dict` in JSON). """
    
    location = Column(primitives.StringField,
                      ForeignKey('EncounterLocation.id'))
    """ List of locations where the patient has been.
        List of `EncounterLocation` items (represented as `dict` in JSON). """
    
    # todo partOf = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    partOf = Column(primitives.StringField)
    """ Another Encounter this encounter is part of.
        Type `FHIRReference` referencing `Encounter`
        (represented as `dict` in JSON). """
    
    participant = Column(primitives.StringField,
                         ForeignKey('EncounterParticipant.id'))
    """ List of participants involved in the encounter.
        List of `EncounterParticipant` items (represented as `dict` in JSON). """
    
    # todo patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    patient = Column(primitives.StringField)
    """ The patient present at the encounter.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    period = Column(primitives.StringField,
                    ForeignKey('Period.id'))
    """ The start and end time of the encounter.
        Type `Period` (represented as `dict` in JSON). """
    
    priority = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Indicates the urgency of the encounter.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    reason = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ Reason the encounter takes place (code).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    # todo serviceProvider = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    serviceProvider = Column(primitives.StringField)
    """ The custodian organization of this Encounter record.
        Type `FHIRReference` referencing `Organization`
        (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ planned | arrived | in-progress | onleave | finished | cancelled.
        Type `str`. """
    
    statusHistory = Column(primitives.StringField,
                           ForeignKey('EncounterStatusHistory.id'))
    """ List of past encounter statuses.
        List of `EncounterStatusHistory` items (represented as `dict` in JSON). """
    
    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Specific type of encounter.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, appointment, class_fhir, episodeOfCare,
                 hospitalization, identifier, incomingReferral,
                 indication, length, location, partOf, participant,
                 patient, period, priority, reason, serviceProvider,
                 status, statusHistory, type,):
        """ Initialize all valid properties.
        """
        self.appointment = appointment
        self.class_fhir = class_fhir
        self.episodeOfCare = episodeOfCare
        self.hospitalization = hospitalization
        self.identifier = identifier
        self.incomingReferral = incomingReferral
        self.indication = indication
        self.length = length
        self.location = location
        self.partOf = partOf
        self.participant = participant
        self.patient = patient
        self.period = period
        self.priority = priority
        self.reason = reason
        self.serviceProvider = serviceProvider
        self.status = status
        self.statusHistory = statusHistory
        self.type = type

    def __repr__(self):
        return '<Encounter %r>' % 'self.property'  # replace self.property
