#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/MedicationStatement)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class MedicationStatement(domainresource.DomainResource):
    """ Record of medication being taken by a patient.

    A record of a medication that is being consumed by a patient.   A
    MedicationStatement may indicate that the patient may be taking the
    medication now, or has taken the medication in the past or will be taking
    the medication in the future.  The source of this information can be the
    patient, significant other (such as a family member or spouse), or a
    clinician.  A common scenario where this information is captured is during
    the history taking process during a patient visit or stay.   The medication
    information may come from e.g. the patient's memory, from a prescription
    bottle,  or from a list of medications the patient, clinician or other
    party maintains

The primary difference between a medication statement and
    a medication administration is that the medication administration has
    complete administration information and is based on actual administration
    information from the person who administered the medication.  A medication
    statement is often, if not always, less specific.  There is no required
    date/time when the medication was administered, in fact we only know that a
    source has reported the patient is taking this medication, where details
    such as time, quantity, or rate or even medication product may be
    incomplete or missing or less precise.  As stated earlier, the medication
    statement information may come from the patient's memory, from a
    prescription bottle or from a list of medications the patient, clinician or
    other party maintains.  Medication administration is more formal and is not
    missing detailed information.
    """

    __tablename__ = "MedicationStatement"

    dateAsserted = Column(FHIRDate)
    """ When the statement was asserted?.
        Type `FHIRDate` (represented as `str` in JSON). """

    dosage = Column(MedicationStatementDosage)
    """ Details of how medication was taken.
        List of `MedicationStatementDosage` items (represented as `dict` in JSON). """

    effectiveDateTime = Column(FHIRDate)
    """ Over what period was medication consumed?.
        Type `FHIRDate` (represented as `str` in JSON). """

    effectivePeriod = Column(Period)
    """ Over what period was medication consumed?.
        Type `Period` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    informationSource = Column(FHIRReference)
    """ None.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """

    medicationCodeableConcept = Column(CodeableConcept)
    """ What medication was taken.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    medicationReference = Column(FHIRReference)
    """ What medication was taken.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """

    note = Column(primitives.StringField)
    """ Further information about the statement.
        Type `str`. """

    patient = Column(FHIRReference)
    """ Who is/was taking  the medication.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    reasonForUseCodeableConcept = Column(CodeableConcept)
    """ None.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    reasonForUseReference = Column(FHIRReference)
    """ None.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """

    reasonNotTaken = Column(CodeableConcept)
    """ True if asserting medication was not given.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ active | completed | entered-in-error | intended.
        Type `str`. """

    supportingInformation = Column(FHIRReference)
    """ Additional supporting information.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """

    wasNotTaken = Column(bool)
    """ True if medication is/was not being taken.
        Type `bool`. """

    def __init__(self, dateAsserted, dosage, effectiveDateTime, effectivePeriod, identifier, informationSource, medicationCodeableConcept, medicationReference, note, patient, reasonForUseCodeableConcept, reasonForUseReference, reasonNotTaken, status, supportingInformation, wasNotTaken,):
        """ Initialize all valid properties.
        """
        self.dateAsserted = dateAsserted
        self.dosage = dosage
        self.effectiveDateTime = effectiveDateTime
        self.effectivePeriod = effectivePeriod
        self.identifier = identifier
        self.informationSource = informationSource
        self.medicationCodeableConcept = medicationCodeableConcept
        self.medicationReference = medicationReference
        self.note = note
        self.patient = patient
        self.reasonForUseCodeableConcept = reasonForUseCodeableConcept
        self.reasonForUseReference = reasonForUseReference
        self.reasonNotTaken = reasonNotTaken
        self.status = status
        self.supportingInformation = supportingInformation
        self.wasNotTaken = wasNotTaken

    def __repr__(self):
        return '<MedicationStatement %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class MedicationStatementDosage(backboneelement.BackboneElement):
    """ Details of how medication was taken.

    Indicates how the medication is/was used by the patient.
    """

    __tablename__ = "MedicationStatementDosage"

    asNeededBoolean = Column(bool)
    """ Take "as needed" (for x).
        Type `bool`. """

    asNeededCodeableConcept = Column(CodeableConcept)
    """ Take "as needed" (for x).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    maxDosePerPeriod = Column(Ratio)
    """ Maximum dose that was consumed per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """

    method = Column(CodeableConcept)
    """ Technique used to administer medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    quantityQuantity = Column(Quantity)
    """ Amount administered in one dose.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    quantityRange = Column(Range)
    """ Amount administered in one dose.
        Type `Range` (represented as `dict` in JSON). """

    rateRange = Column(Range)
    """ Dose quantity per unit of time.
        Type `Range` (represented as `dict` in JSON). """

    rateRatio = Column(Ratio)
    """ Dose quantity per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """

    route = Column(CodeableConcept)
    """ How the medication entered the body.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    siteCodeableConcept = Column(CodeableConcept)
    """ Where (on body) medication is/was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    siteReference = Column(FHIRReference)
    """ Where (on body) medication is/was administered.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """

    text = Column(primitives.StringField)
    """ Reported dosage information.
        Type `str`. """

    timing = Column(Timing)
    """ When/how often was medication taken.
        Type `Timing` (represented as `dict` in JSON). """

    def __init__(self, asNeededBoolean, asNeededCodeableConcept, maxDosePerPeriod, method, quantityQuantity, quantityRange, rateRange, rateRatio, route, siteCodeableConcept, siteReference, text, timing,):
        """ Initialize all valid properties.
        """
        self.asNeededBoolean = asNeededBoolean
        self.asNeededCodeableConcept = asNeededCodeableConcept
        self.maxDosePerPeriod = maxDosePerPeriod
        self.method = method
        self.quantityQuantity = quantityQuantity
        self.quantityRange = quantityRange
        self.rateRange = rateRange
        self.rateRatio = rateRatio
        self.route = route
        self.siteCodeableConcept = siteCodeableConcept
        self.siteReference = siteReference
        self.text = text
        self.timing = timing

    def __repr__(self):
        return '<MedicationStatementDosage %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import ratio
from . import timing