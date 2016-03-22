#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Immunization)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class Immunization(domainresource.DomainResource):
    """ Immunization event information.

    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or another
    party and may include vaccine reaction information and what vaccination
    protocol was followed.
    """

    __tablename__ = "Immunization"

    date = Column(FHIRDate)
    """ Vaccination administration date.
        Type `FHIRDate` (represented as `str` in JSON). """

    doseQuantity = Column(Quantity)
    """ Amount of vaccine administered.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    encounter = Column(FHIRReference)
    """ Encounter administered as part of.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    expirationDate = Column(FHIRDate)
    """ Vaccine expiration date.
        Type `FHIRDate` (represented as `str` in JSON). """

    explanation = Column(ImmunizationExplanation)
    """ Administration/non-administration reasons.
        Type `ImmunizationExplanation` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    location = Column(FHIRReference)
    """ Where vaccination occurred.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """

    lotNumber = Column(primitives.StringField)
    """ Vaccine lot number.
        Type `str`. """

    manufacturer = Column(FHIRReference)
    """ Vaccine manufacturer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    note = Column(Annotation)
    """ Vaccination notes.
        List of `Annotation` items (represented as `dict` in JSON). """

    patient = Column(FHIRReference)
    """ Who was immunized.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    performer = Column(FHIRReference)
    """ Who administered vaccine.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    reaction = Column(ImmunizationReaction)
    """ Details of a reaction that follows immunization.
        List of `ImmunizationReaction` items (represented as `dict` in JSON). """

    reported = Column(bool)
    """ Indicates a self-reported record.
        Type `bool`. """

    requester = Column(FHIRReference)
    """ Who ordered vaccination.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    route = Column(CodeableConcept)
    """ How vaccine entered body.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    site = Column(CodeableConcept)
    """ Body site vaccine  was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ in-progress | on-hold | completed | entered-in-error | stopped.
        Type `str`. """

    vaccinationProtocol = Column(ImmunizationVaccinationProtocol)
    """ What protocol was followed.
        List of `ImmunizationVaccinationProtocol` items (represented as `dict` in JSON). """

    vaccineCode = Column(CodeableConcept)
    """ Vaccine product administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    wasNotGiven = Column(bool)
    """ Flag for whether immunization was given.
        Type `bool`. """

    def __init__(self, date, doseQuantity, encounter, expirationDate, explanation, identifier, location, lotNumber, manufacturer, note, patient, performer, reaction, reported, requester, route, site, status, vaccinationProtocol, vaccineCode, wasNotGiven,):
        """ Initialize all valid properties.
        """
        self.date = date
        self.doseQuantity = doseQuantity
        self.encounter = encounter
        self.expirationDate = expirationDate
        self.explanation = explanation
        self.identifier = identifier
        self.location = location
        self.lotNumber = lotNumber
        self.manufacturer = manufacturer
        self.note = note
        self.patient = patient
        self.performer = performer
        self.reaction = reaction
        self.reported = reported
        self.requester = requester
        self.route = route
        self.site = site
        self.status = status
        self.vaccinationProtocol = vaccinationProtocol
        self.vaccineCode = vaccineCode
        self.wasNotGiven = wasNotGiven

    def __repr__(self):
        return '<Immunization %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class ImmunizationExplanation(backboneelement.BackboneElement):
    """ Administration/non-administration reasons.

    Reasons why a vaccine was or was not administered.
    """

    __tablename__ = "ImmunizationExplanation"

    reason = Column(CodeableConcept)
    """ Why immunization occurred.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    reasonNotGiven = Column(CodeableConcept)
    """ Why immunization did not occur.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, reason, reasonNotGiven,):
        """ Initialize all valid properties.
        """
        self.reason = reason
        self.reasonNotGiven = reasonNotGiven

    def __repr__(self):
        return '<ImmunizationExplanation %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ImmunizationReaction(backboneelement.BackboneElement):
    """ Details of a reaction that follows immunization.

    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """

    __tablename__ = "ImmunizationReaction"

    date = Column(FHIRDate)
    """ When reaction started.
        Type `FHIRDate` (represented as `str` in JSON). """

    detail = Column(FHIRReference)
    """ Additional information on reaction.
        Type `FHIRReference` referencing `Observation` (represented as `dict` in JSON). """

    reported = Column(bool)
    """ Indicates self-reported reaction.
        Type `bool`. """

    def __init__(self, date, detail, reported,):
        """ Initialize all valid properties.
        """
        self.date = date
        self.detail = detail
        self.reported = reported

    def __repr__(self):
        return '<ImmunizationReaction %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ImmunizationVaccinationProtocol(backboneelement.BackboneElement):
    """ What protocol was followed.

    Contains information about the protocol(s) under which the vaccine was
    administered.
    """

    __tablename__ = "ImmunizationVaccinationProtocol"

    authority = Column(FHIRReference)
    """ Who is responsible for protocol.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    description = Column(primitives.StringField)
    """ Details of vaccine protocol.
        Type `str`. """

    doseSequence = Column(Integer)
    """ Dose number within series.
        Type `int`. """

    doseStatus = Column(CodeableConcept)
    """ Indicates if dose counts towards immunity.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    doseStatusReason = Column(CodeableConcept)
    """ Why dose does (not) count.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    series = Column(primitives.StringField)
    """ Name of vaccine series.
        Type `str`. """

    seriesDoses = Column(Integer)
    """ Recommended number of doses for immunity.
        Type `int`. """

    targetDisease = Column(CodeableConcept)
    """ Disease immunized against.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, authority, description, doseSequence, doseStatus, doseStatusReason, series, seriesDoses, targetDisease,):
        """ Initialize all valid properties.
        """
        self.authority = authority
        self.description = description
        self.doseSequence = doseSequence
        self.doseStatus = doseStatus
        self.doseStatusReason = doseStatusReason
        self.series = series
        self.seriesDoses = seriesDoses
        self.targetDisease = targetDisease

    def __repr__(self):
        return '<ImmunizationVaccinationProtocol %r>' % 'self.property'  # replace self.property


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity