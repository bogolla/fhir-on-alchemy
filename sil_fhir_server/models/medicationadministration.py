#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/MedicationAdministration)
#  Date: 2016-03-18.


from . import domainresource

class MedicationAdministration(domainresource.DomainResource):
    """ Administration of medication to a patient.

    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """

    __tablename__ = "MedicationAdministration"

    device = Column(FHIRReference)
    """ Device used to administer.
        List of `FHIRReference` items referencing `Device` (represented as `dict` in JSON). """

    dosage = Column()
    """ Details of how medication was taken.
        Type `MedicationAdministrationDosage` (represented as `dict` in JSON). """

    effectiveTimeDateTime = Column()
    """ Start and end time of administration.
        Type `FHIRDate` (represented as `str` in JSON). """

    effectiveTimePeriod = Column()
    """ Start and end time of administration.
        Type `Period` (represented as `dict` in JSON). """

    encounter = Column()
    """ Encounter administered as part of.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    medicationCodeableConcept = Column()
    """ What was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    medicationReference = Column()
    """ What was administered.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """

    note = Column()
    """ Information about the administration.
        Type `str`. """

    patient = Column()
    """ Who received medication.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    practitioner = Column()
    """ Who administered substance.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """

    prescription = Column()
    """ Order administration performed against.
        Type `FHIRReference` referencing `MedicationOrder` (represented as `dict` in JSON). """

    reasonGiven = Column(CodeableConcept)
    """ Reason administration performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    reasonNotGiven = Column(CodeableConcept)
    """ Reason administration not performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    status = Column()
    """ in-progress | on-hold | completed | entered-in-error | stopped.
        Type `str`. """

    wasNotGiven = Column()
    """ True if medication not administered.
        Type `bool`. """

    def __init__(self, device, dosage, effectiveTimeDateTime, effectiveTimePeriod, encounter, identifier, medicationCodeableConcept, medicationReference, note, patient, practitioner, prescription, reasonGiven, reasonNotGiven, status, wasNotGiven,):
        """ Initialize all valid properties.
        """
        self.device = device
        self.dosage = dosage
        self.effectiveTimeDateTime = effectiveTimeDateTime
        self.effectiveTimePeriod = effectiveTimePeriod
        self.encounter = encounter
        self.identifier = identifier
        self.medicationCodeableConcept = medicationCodeableConcept
        self.medicationReference = medicationReference
        self.note = note
        self.patient = patient
        self.practitioner = practitioner
        self.prescription = prescription
        self.reasonGiven = reasonGiven
        self.reasonNotGiven = reasonNotGiven
        self.status = status
        self.wasNotGiven = wasNotGiven

    def __repr__(self):
        return '<MedicationAdministration %r>' % 'self.property'  # replace self.property


from . import backboneelement

class MedicationAdministrationDosage(backboneelement.BackboneElement):
    """ Details of how medication was taken.

    Describes the medication dosage information details e.g. dose, rate, site,
    route, etc.
    """

    __tablename__ = "MedicationAdministrationDosage"

    method = Column()
    """ How drug was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    quantity = Column()
    """ Amount administered in one dose.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    rateRange = Column()
    """ Dose quantity per unit of time.
        Type `Range` (represented as `dict` in JSON). """

    rateRatio = Column()
    """ Dose quantity per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """

    route = Column()
    """ Path of substance into body.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    siteCodeableConcept = Column()
    """ Body site administered to.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    siteReference = Column()
    """ Body site administered to.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """

    text = Column()
    """ Dosage Instructions.
        Type `str`. """

    def __init__(self, method, quantity, rateRange, rateRatio, route, siteCodeableConcept, siteReference, text,):
        """ Initialize all valid properties.
        """
        self.method = method
        self.quantity = quantity
        self.rateRange = rateRange
        self.rateRatio = rateRatio
        self.route = route
        self.siteCodeableConcept = siteCodeableConcept
        self.siteReference = siteReference
        self.text = text

    def __repr__(self):
        return '<MedicationAdministrationDosage %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import ratio