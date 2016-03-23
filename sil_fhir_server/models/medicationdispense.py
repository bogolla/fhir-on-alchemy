#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/MedicationDispense)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class MedicationDispenseDosageInstruction(backboneelement.BackboneElement):
    """ Medicine administration instructions to the patient/caregiver.

    Indicates how the medication is to be used by the patient.
    """

    __tablename__ = "MedicationDispenseDosageInstruction"

    additionalInstructions = Column(primitives.StringField,
                                    ForeignKey('CodeableConcept.id'))
    """ E.g. "Take with food".
        Type `CodeableConcept` (represented as `dict` in JSON). """

    asNeededBoolean = Column(primitives.BooleanField)
    """ Take "as needed" f(or x).
        Type `bool`. """

    asNeededCodeableConcept = Column(primitives.StringField,
                                     ForeignKey('CodeableConcept.id'))
    """ Take "as needed" f(or x).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    doseQuantity = Column(primitives.StringField,
                          ForeignKey('Quantity.id'))
    """ Amount of medication per dose.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    doseRange = Column(primitives.StringField,
                       ForeignKey('Range.id'))
    """ Amount of medication per dose.
        Type `Range` (represented as `dict` in JSON). """

    maxDosePerPeriod = Column(primitives.StringField,
                              ForeignKey('Ratio.id'))
    """ Upper limit on medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """

    method = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ Technique for administering medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    rateRange = Column(primitives.StringField,
                       ForeignKey('Range.id'))
    """ Amount of medication per unit of time.
        Type `Range` (represented as `dict` in JSON). """

    rateRatio = Column(primitives.StringField,
                       ForeignKey('Ratio.id'))
    """ Amount of medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """

    route = Column(primitives.StringField,
                   ForeignKey('CodeableConcept.id'))
    """ How drug should enter body.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    siteCodeableConcept = Column(primitives.StringField,
                                 ForeignKey('CodeableConcept.id'))
    """ Body site to administer to.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    # todo siteReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    siteReference = Column(primitives.StringField)
    """ Body site to administer to.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """

    text = Column(primitives.StringField)
    """ Dosage Instructions.
        Type `str`. """

    timing = Column(primitives.StringField,
                    ForeignKey('Timing.id'))
    """ When medication should be administered.
        Type `Timing` (represented as `dict` in JSON). """

    def __init__(self, additionalInstructions, asNeededBoolean,
                 asNeededCodeableConcept, doseQuantity, doseRange,
                 maxDosePerPeriod, method, rateRange, rateRatio,
                 route, siteCodeableConcept, siteReference, text, timing,):
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

    reason = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ Why was substitution made.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    # todo responsibleParty = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    responsibleParty = Column(primitives.StringField)
    """ Who is responsible for the substitution.
        List of `FHIRReference` items referencing `Practitioner`
        (represented as `dict` in JSON). """

    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
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


class MedicationDispense(domainresource.DomainResource):
    """ Dispensing a medication to a named patient.

    Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """

    __tablename__ = "MedicationDispense"
    
    # todo authorizingPrescription = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    authorizingPrescription = Column(primitives.StringField)
    """ Medication order that authorizes the dispense.
        List of `FHIRReference` items referencing `MedicationOrder` (represented as `dict` in JSON). """
    
    daysSupply = Column(primitives.StringField,
                        ForeignKey('Quantity.id'))
    """ Days Supply.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
    
    # todo destination = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    destination = Column(primitives.StringField)
    """ Where the medication was sent.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
    
    # todo dispenser = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    dispenser = Column(primitives.StringField)
    """ Practitioner responsible for dispensing medication.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    dosageInstruction = Column(primitives.StringField,
                               ForeignKey(
                                   'MedicationDispenseDosageInstruction.id'))
    """ Medicine administration instructions to the patient/caregiver.
        List of `MedicationDispenseDosageInstruction` items (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ External identifier.
        Type `Identifier` (represented as `dict` in JSON). """
    
    medicationCodeableConcept = Column(primitives.StringField,
                                       ForeignKey('CodeableConcept.id'))
    """ What medication was supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo medicationReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    medicationReference = Column(primitives.StringField)
    """ What medication was supplied.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
    
    note = Column(primitives.StringField)
    """ Information about the dispense.
        Type `str`. """
    
    # todo patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    patient = Column(primitives.StringField)
    """ Who the dispense is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    quantity = Column(primitives.StringField,
                      ForeignKey('Quantity.id'))
    """ Amount dispensed.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
    
    # todo receiver = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    receiver = Column(primitives.StringField)
    """ Who collected the medication.
        List of `FHIRReference` items referencing `Patient, Practitioner`
        (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ in-progress | on-hold | completed | entered-in-error | stopped.
        Type `str`. """
    
    substitution = Column(primitives.StringField,
                          ForeignKey(
                              'MedicationDispenseSubstitution.id'))
    """ Deals with substitution of one medicine for another.
        Type `MedicationDispenseSubstitution` (represented as `dict` in JSON). """
    
    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Trial fill, partial fill, emergency fill, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    whenHandedOver = Column(primitives.DateTimeField)
    """ When product was given out.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    whenPrepared = Column(primitives.DateTimeField)
    """ Dispense processing time.
        Type `FHIRDate` (represented as `str` in JSON). """

    def __init__(self, authorizingPrescription, daysSupply, destination,
                 dispenser, dosageInstruction, identifier,
                 medicationCodeableConcept, medicationReference, note,
                 patient, quantity, receiver, status, substitution, type,
                 whenHandedOver, whenPrepared,):
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
