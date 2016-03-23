#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/MedicationAdministration)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class MedicationAdministrationDosage(backboneelement.BackboneElement):
    """ Details of how medication was taken.

    Describes the medication dosage information details e.g. dose, rate, site,
    route, etc.
    """

    __tablename__ = "MedicationAdministrationDosage"

    method = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ How drug was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    quantity = Column(primitives.StringField,
                      ForeignKey('Quantity.id'))
    """ Amount administered in one dose.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    rateRange = Column(primitives.StringField,
                       ForeignKey('Range.id'))
    """ Dose quantity per unit of time.
        Type `Range` (represented as `dict` in JSON). """

    rateRatio = Column(primitives.StringField,
                       ForeignKey('Ratio.id'))
    """ Dose quantity per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """

    route = Column(primitives.StringField,
                   ForeignKey('CodeableConcept.id'))
    """ Path of substance into body.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    siteCodeableConcept = Column(primitives.StringField,
                                 ForeignKey('CodeableConcept.id'))
    """ Body site administered to.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    # todo siteReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    siteReference = Column(primitives.StringField)
    """ Body site administered to.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """

    text = Column(primitives.StringField)
    """ Dosage Instructions.
        Type `str`. """

    def __init__(self, method, quantity, rateRange, rateRatio, route,
                 siteCodeableConcept, siteReference, text,):
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


class MedicationAdministration(domainresource.DomainResource):
    """ Administration of medication to a patient.

    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """

    __tablename__ = "MedicationAdministration"
    
    # todo device = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    device = Column(primitives.StringField)
    """ Device used to administer.
        List of `FHIRReference` items referencing `Device`
        (represented as `dict` in JSON). """
    
    dosage = Column(primitives.StringField,
                    ForeignKey('MedicationAdministrationDosage.id'))
    """ Details of how medication was taken.
        Type `MedicationAdministrationDosage` (represented as `dict` in JSON). """
    
    effectiveTimeDateTime = Column(primitives.DateTimeField)
    """ Start and end time of administration.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    effectiveTimePeriod = Column(primitives.StringField,
                                 ForeignKey('Period.id'))
    """ Start and end time of administration.
        Type `Period` (represented as `dict` in JSON). """
    
    # todo encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ Encounter administered as part of.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    medicationCodeableConcept = Column(primitives.StringField,
                                       ForeignKey('CodeableConcept.id'))
    """ What was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo medicationReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    medicationReference = Column(primitives.StringField)
    """ What was administered.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
    
    note = Column(primitives.StringField)
    """ Information about the administration.
        Type `str`. """
    
    # todo patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    patient = Column(primitives.StringField)
    """ Who received medication.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    # todo practitioner = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    practitioner = Column(primitives.StringField)
    """ Who administered substance.
        Type `FHIRReference` referencing `Practitioner, Patient,
        RelatedPerson` (represented as `dict` in JSON). """
    
    # todo prescription = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    prescription = Column(primitives.StringField)
    """ Order administration performed against.
        Type `FHIRReference` referencing `MedicationOrder` (represented as `dict` in JSON). """
    
    reasonGiven = Column(primitives.StringField,
                         ForeignKey('CodeableConcept.id'))
    """ Reason administration performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    reasonNotGiven = Column(primitives.StringField,
                            ForeignKey('CodeableConcept.id'))
    """ Reason administration not performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ in-progress | on-hold | completed | entered-in-error | stopped.
        Type `str`. """
    
    wasNotGiven = Column(primitives.BooleanField)
    """ True if medication not administered.
        Type `bool`. """

    def __init__(self, device, dosage, effectiveTimeDateTime, effectiveTimePeriod,
                 encounter, identifier, medicationCodeableConcept, medicationReference,
                 note, patient, practitioner, prescription, reasonGiven, reasonNotGiven,
                 status, wasNotGiven,):
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
