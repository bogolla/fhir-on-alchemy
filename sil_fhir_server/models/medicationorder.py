#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/MedicationOrder)
#  Date: 2016-03-18.


from . import domainresource

class MedicationOrder(domainresource.DomainResource):
    """ Prescription of medication to for patient.

    An order for both supply of the medication and the instructions for
    administration of the medication to a patient. The resource is called
    "MedicationOrder" rather than "MedicationPrescription" to generalize the
    use across inpatient and outpatient settings as well as for care plans,
    etc.
    """

    __tablename__ = "MedicationOrder"

    dateEnded = Column()
    """ When prescription was stopped.
        Type `FHIRDate` (represented as `str` in JSON). """

    dateWritten = Column()
    """ When prescription was authorized.
        Type `FHIRDate` (represented as `str` in JSON). """

    dispenseRequest = Column()
    """ Medication supply authorization.
        Type `MedicationOrderDispenseRequest` (represented as `dict` in JSON). """

    dosageInstruction = Column(MedicationOrderDosageInstruction)
    """ How medication should be taken.
        List of `MedicationOrderDosageInstruction` items (represented as `dict` in JSON). """

    encounter = Column()
    """ Created during encounter/admission/stay.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    medicationCodeableConcept = Column()
    """ Medication to be taken.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    medicationReference = Column()
    """ Medication to be taken.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """

    note = Column()
    """ Information about the prescription.
        Type `str`. """

    patient = Column()
    """ Who prescription is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    prescriber = Column()
    """ Who ordered the medication(s).
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    priorPrescription = Column()
    """ An order/prescription that this supersedes.
        Type `FHIRReference` referencing `MedicationOrder` (represented as `dict` in JSON). """

    reasonCodeableConcept = Column()
    """ Reason or indication for writing the prescription.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    reasonEnded = Column()
    """ Why prescription was stopped.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    reasonReference = Column()
    """ Reason or indication for writing the prescription.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """

    status = Column()
    """ active | on-hold | completed | entered-in-error | stopped | draft.
        Type `str`. """

    substitution = Column()
    """ Any restrictions on medication substitution.
        Type `MedicationOrderSubstitution` (represented as `dict` in JSON). """

    def __init__(self, dateEnded, dateWritten, dispenseRequest, dosageInstruction, encounter, identifier, medicationCodeableConcept, medicationReference, note, patient, prescriber, priorPrescription, reasonCodeableConcept, reasonEnded, reasonReference, status, substitution,):
        """ Initialize all valid properties.
        """
        self.dateEnded = dateEnded
        self.dateWritten = dateWritten
        self.dispenseRequest = dispenseRequest
        self.dosageInstruction = dosageInstruction
        self.encounter = encounter
        self.identifier = identifier
        self.medicationCodeableConcept = medicationCodeableConcept
        self.medicationReference = medicationReference
        self.note = note
        self.patient = patient
        self.prescriber = prescriber
        self.priorPrescription = priorPrescription
        self.reasonCodeableConcept = reasonCodeableConcept
        self.reasonEnded = reasonEnded
        self.reasonReference = reasonReference
        self.status = status
        self.substitution = substitution

    def __repr__(self):
        return '<MedicationOrder %r>' % 'self.property'  # replace self.property


from . import backboneelement

class MedicationOrderDispenseRequest(backboneelement.BackboneElement):
    """ Medication supply authorization.

    Indicates the specific details for the dispense or medication supply part
    of a medication order (also known as a Medication Prescription).  Note that
    this information is NOT always sent with the order.  There may be in some
    settings (e.g. hospitals) institutional or system support for completing
    the dispense details in the pharmacy department.
    """

    __tablename__ = "MedicationOrderDispenseRequest"

    expectedSupplyDuration = Column()
    """ Number of days supply per dispense.
        Type `Quantity` referencing `Duration` (represented as `dict` in JSON). """

    medicationCodeableConcept = Column()
    """ Product to be supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    medicationReference = Column()
    """ Product to be supplied.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """

    numberOfRepeatsAllowed = Column()
    """ Number of refills authorized.
        Type `int`. """

    quantity = Column()
    """ Amount of medication to supply per dispense.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    validityPeriod = Column()
    """ Time period supply is authorized for.
        Type `Period` (represented as `dict` in JSON). """

    def __init__(self, expectedSupplyDuration, medicationCodeableConcept, medicationReference, numberOfRepeatsAllowed, quantity, validityPeriod,):
        """ Initialize all valid properties.
        """
        self.expectedSupplyDuration = expectedSupplyDuration
        self.medicationCodeableConcept = medicationCodeableConcept
        self.medicationReference = medicationReference
        self.numberOfRepeatsAllowed = numberOfRepeatsAllowed
        self.quantity = quantity
        self.validityPeriod = validityPeriod

    def __repr__(self):
        return '<MedicationOrderDispenseRequest %r>' % 'self.property'  # replace self.property


class MedicationOrderDosageInstruction(backboneelement.BackboneElement):
    """ How medication should be taken.

    Indicates how the medication is to be used by the patient.
    """

    __tablename__ = "MedicationOrderDosageInstruction"

    additionalInstructions = Column()
    """ Supplemental instructions - e.g. "with meals".
        Type `CodeableConcept` (represented as `dict` in JSON). """

    asNeededBoolean = Column()
    """ Take "as needed" (for x).
        Type `bool`. """

    asNeededCodeableConcept = Column()
    """ Take "as needed" (for x).
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
    """ Dosage instructions expressed as text.
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
        return '<MedicationOrderDosageInstruction %r>' % 'self.property'  # replace self.property


class MedicationOrderSubstitution(backboneelement.BackboneElement):
    """ Any restrictions on medication substitution.

    Indicates whether or not substitution can or should be part of the
    dispense. In some cases substitution must happen, in other cases
    substitution must not happen, and in others it does not matter. This block
    explains the prescriber's intent. If nothing is specified substitution may
    be done.
    """

    __tablename__ = "MedicationOrderSubstitution"

    reason = Column()
    """ Why should (not) substitution be made.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    type = Column()
    """ generic | formulary +.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, reason, type,):
        """ Initialize all valid properties.
        """
        self.reason = reason
        self.type = type

    def __repr__(self):
        return '<MedicationOrderSubstitution %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import ratio
from . import timing