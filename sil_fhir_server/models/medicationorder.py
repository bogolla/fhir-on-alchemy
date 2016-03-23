#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/MedicationOrder)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
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
    
    dateEnded = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ When prescription was stopped.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    dateWritten = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ When prescription was authorized.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    dispenseRequest = Column(primitives.StringField, ForeignKey('MedicationOrderDispenseRequest.id'))
    """ Medication supply authorization.
        Type `MedicationOrderDispenseRequest` (represented as `dict` in JSON). """
    
    dosageInstruction = Column(primitives.StringField, ForeignKey('MedicationOrderDosageInstruction.id'))
    """ How medication should be taken.
        List of `MedicationOrderDosageInstruction` items (represented as `dict` in JSON). """
    
    encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Created during encounter/admission/stay.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField, ForeignKey('Identifier.id'))
    """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    medicationCodeableConcept = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ Medication to be taken.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    medicationReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Medication to be taken.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
    
    note = Column(primitives.StringField)
    """ Information about the prescription.
        Type `str`. """
    
    patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Who prescription is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    prescriber = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Who ordered the medication(s).
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    priorPrescription = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ An order/prescription that this supersedes.
        Type `FHIRReference` referencing `MedicationOrder` (represented as `dict` in JSON). """
    
    reasonCodeableConcept = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ Reason or indication for writing the prescription.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    reasonEnded = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ Why prescription was stopped.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    reasonReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Reason or indication for writing the prescription.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ active | on-hold | completed | entered-in-error | stopped | draft.
        Type `str`. """
    
    substitution = Column(primitives.StringField, ForeignKey('MedicationOrderSubstitution.id'))
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


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
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
    
    expectedSupplyDuration = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ Number of days supply per dispense.
        Type `Quantity` referencing `Duration` (represented as `dict` in JSON). """
    
    medicationCodeableConcept = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ Product to be supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    medicationReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Product to be supplied.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
    
    numberOfRepeatsAllowed = Column(primitives.IntegerField)
    """ Number of refills authorized.
        Type `int`. """
    
    quantity = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ Amount of medication to supply per dispense.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
    
    validityPeriod = Column(primitives.StringField, ForeignKey('Period.id'))
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


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
class MedicationOrderDosageInstruction(backboneelement.BackboneElement):
    """ How medication should be taken.

    Indicates how the medication is to be used by the patient.
    """

    __tablename__ = "MedicationOrderDosageInstruction"
    
    additionalInstructions = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ Supplemental instructions - e.g. "with meals".
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    asNeededBoolean = Column(primitives.BooleanField)
    """ Take "as needed" (for x).
        Type `bool`. """
    
    asNeededCodeableConcept = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ Take "as needed" (for x).
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    doseQuantity = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ Amount of medication per dose.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
    
    doseRange = Column(primitives.StringField, ForeignKey('Range.id'))
    """ Amount of medication per dose.
        Type `Range` (represented as `dict` in JSON). """
    
    maxDosePerPeriod = Column(primitives.StringField, ForeignKey('Ratio.id'))
    """ Upper limit on medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
    
    method = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ Technique for administering medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    rateRange = Column(primitives.StringField, ForeignKey('Range.id'))
    """ Amount of medication per unit of time.
        Type `Range` (represented as `dict` in JSON). """
    
    rateRatio = Column(primitives.StringField, ForeignKey('Ratio.id'))
    """ Amount of medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
    
    route = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ How drug should enter body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    siteCodeableConcept = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ Body site to administer to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    siteReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Body site to administer to.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """
    
    text = Column(primitives.StringField)
    """ Dosage instructions expressed as text.
        Type `str`. """
    
    timing = Column(primitives.StringField, ForeignKey('Timing.id'))
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


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
class MedicationOrderSubstitution(backboneelement.BackboneElement):
    """ Any restrictions on medication substitution.

    Indicates whether or not substitution can or should be part of the
    dispense. In some cases substitution must happen, in other cases
    substitution must not happen, and in others it does not matter. This block
    explains the prescriber's intent. If nothing is specified substitution may
    be done.
    """

    __tablename__ = "MedicationOrderSubstitution"
    
    reason = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ Why should (not) substitution be made.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    type = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ generic | formulary +.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, reason, type,):
        """ Initialize all valid properties.
        """
        self.reason = reason
        self.type = type

    def __repr__(self):
        return '<MedicationOrderSubstitution %r>' % 'self.property'  # replace self.property