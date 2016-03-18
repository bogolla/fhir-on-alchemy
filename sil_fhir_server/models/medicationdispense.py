#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/MedicationDispense)
#  Date: 2016-03-18.


from . import domainresource

class MedicationDispense(domainresource.DomainResource):
    """ Dispensing a medication to a named patient.

    Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """

    __tablename__ = "MedicationDispense"

    authorizingPrescription = Column(FHIRReference)
    """ Medication order that authorizes the dispense.
        List of `FHIRReference` items referencing `MedicationOrder` (represented as `dict` in JSON). """

    daysSupply = Column()
    """ Days Supply.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    destination = Column()
    """ Where the medication was sent.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """

    dispenser = Column()
    """ Practitioner responsible for dispensing medication.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    dosageInstruction = Column(MedicationDispenseDosageInstruction)
    """ Medicine administration instructions to the patient/caregiver.
        List of `MedicationDispenseDosageInstruction` items (represented as `dict` in JSON). """

    identifier = Column()
    """ External identifier.
        Type `Identifier` (represented as `dict` in JSON). """

    medicationCodeableConcept = Column()
    """ What medication was supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    medicationReference = Column()
    """ What medication was supplied.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """

    note = Column()
    """ Information about the dispense.
        Type `str`. """

    patient = Column()
    """ Who the dispense is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    quantity = Column()
    """ Amount dispensed.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    receiver = Column(FHIRReference)
    """ Who collected the medication.
        List of `FHIRReference` items referencing `Patient, Practitioner` (represented as `dict` in JSON). """

    status = Column()
    """ in-progress | on-hold | completed | entered-in-error | stopped.
        Type `str`. """

    substitution = Column()
    """ Deals with substitution of one medicine for another.
        Type `MedicationDispenseSubstitution` (represented as `dict` in JSON). """

    type = Column()
    """ Trial fill, partial fill, emergency fill, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """

    whenHandedOver = Column()
    """ When product was given out.
        Type `FHIRDate` (represented as `str` in JSON). """

    whenPrepared = Column()
    """ Dispense processing time.
        Type `FHIRDate` (represented as `str` in JSON). """

    def __init__(self, authorizingPrescription, daysSupply, destination, dispenser, dosageInstruction, identifier, medicationCodeableConcept, medicationReference, note, patient, quantity, receiver, status, substitution, type, whenHandedOver, whenPrepared,):
        """ Initialize all valid properties.
        """
        self.authorizingPrescription = authorizingPrescription
        self.daysSupply = daysSupply
        self.destination = destination
        self.dispenser = dispenser
        self.dosageInstruction = dosageInstruction
        self.identifier = identifier
        self.medicationCodeableConcept = medicationCodeableConcept
        self.medicationReference = medicationReference
        self.note = note
        self.patient = patient
        self.quantity = quantity
        self.receiver = receiver
        self.status = status
        self.substitution = substitution
        self.type = type
        self.whenHandedOver = whenHandedOver
        self.whenPrepared = whenPrepared

    def __repr__(self):
        return '<MedicationDispense %r>' % 'self.property'  # replace self.property


from . import backboneelement

class MedicationDispenseDosageInstruction(backboneelement.BackboneElement):
    """ Medicine administration instructions to the patient/caregiver.

    Indicates how the medication is to be used by the patient.
    """

    __tablename__ = "MedicationDispenseDosageInstruction"

    additionalInstructions = Column()
    """ E.g. "Take with food".
        Type `CodeableConcept` (represented as `dict` in JSON). """

    asNeededBoolean = Column()
    """ Take "as needed" f(or x).
        Type `bool`. """

    asNeededCodeableConcept = Column()
    """ Take "as needed" f(or x).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    doseQuantity = Column()
    """ Amount of medication per dose.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    doseRange = Column()
    """ Amount of medication per dose.
        Type `Range` (represented as `dict` in JSON). """

    maxDosePerPeriod = Column()
    """ Upper limit on medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """

    method = Column()
    """ Technique for administering medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    rateRange = Column()
    """ Amount of medication per unit of time.
        Type `Range` (represented as `dict` in JSON). """

    rateRatio = Column()
    """ Amount of medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """

    route = Column()
    """ How drug should enter body.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    siteCodeableConcept = Column()
    """ Body site to administer to.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    siteReference = Column()
    """ Body site to administer to.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """

    text = Column()
    """ Dosage Instructions.
        Type `str`. """

    timing = Column()
    """ When medication should be administered.
        Type `Timing` (represented as `dict` in JSON). """

    def __init__(self, additionalInstructions, asNeededBoolean, asNeededCodeableConcept, doseQuantity, doseRange, maxDosePerPeriod, method, rateRange, rateRatio, route, siteCodeableConcept, siteReference, text, timing,):
        """ Initialize all valid properties.
        """
        self.additionalInstructions = additionalInstructions
        self.asNeededBoolean = asNeededBoolean
        self.asNeededCodeableConcept = asNeededCodeableConcept
        self.doseQuantity = doseQuantity
        self.doseRange = doseRange
        self.maxDosePerPeriod = maxDosePerPeriod
        self.method = method
        self.rateRange = rateRange
        self.rateRatio = rateRatio
        self.route = route
        self.siteCodeableConcept = siteCodeableConcept
        self.siteReference = siteReference
        self.text = text
        self.timing = timing

    def __repr__(self):
        return '<MedicationDispenseDosageInstruction %r>' % 'self.property'  # replace self.property


class MedicationDispenseSubstitution(backboneelement.BackboneElement):
    """ Deals with substitution of one medicine for another.

    Indicates whether or not substitution was made as part of the dispense.  In
    some cases substitution will be expected but does not happen, in other
    cases substitution is not expected but does happen.  This block explains
    what substitution did or did not happen and why.
    """

    __tablename__ = "MedicationDispenseSubstitution"

    reason = Column(CodeableConcept)
    """ Why was substitution made.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    responsibleParty = Column(FHIRReference)
    """ Who is responsible for the substitution.
        List of `FHIRReference` items referencing `Practitioner` (represented as `dict` in JSON). """

    type = Column()
    """ Type of substitution.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, reason, responsibleParty, type,):
        """ Initialize all valid properties.
        """
        self.reason = reason
        self.responsibleParty = responsibleParty
        self.type = type

    def __repr__(self):
        return '<MedicationDispenseSubstitution %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio
from . import timing