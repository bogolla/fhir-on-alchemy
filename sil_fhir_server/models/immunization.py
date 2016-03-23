#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Immunization)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class ImmunizationExplanation(backboneelement.BackboneElement):
    """ Administration/non-administration reasons.

    Reasons why a vaccine was or was not administered.
    """

    __tablename__ = "ImmunizationExplanation"

    reason = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ Why immunization occurred.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    reasonNotGiven = Column(primitives.StringField,
                            ForeignKey('CodeableConcept.id'))
    """ Why immunization did not occur.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, reason, reasonNotGiven,):
        """ Initialize all valid properties.
        """
        self.reason = reason
        self.reasonNotGiven = reasonNotGiven

    def __repr__(self):
        return '<ImmunizationExplanation %r>' % 'self.property'  # replace self.property


class ImmunizationReaction(backboneelement.BackboneElement):
    """ Details of a reaction that follows immunization.

    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """

    __tablename__ = "ImmunizationReaction"

    date = Column(primitives.DateTimeField)
    """ When reaction started.
        Type `FHIRDate` (represented as `str` in JSON). """

    # todo detail = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    detail = Column(primitives.StringField)
    """ Additional information on reaction.
        Type `FHIRReference` referencing `Observation` (represented as `dict` in JSON). """

    reported = Column(primitives.BooleanField)
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


class ImmunizationVaccinationProtocol(backboneelement.BackboneElement):
    """ What protocol was followed.

    Contains information about the protocol(s) under which the vaccine was
    administered.
    """

    __tablename__ = "ImmunizationVaccinationProtocol"

    # todo authority = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    authority = Column(primitives.StringField)
    """ Who is responsible for protocol.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    description = Column(primitives.StringField)
    """ Details of vaccine protocol.
        Type `str`. """

    doseSequence = Column(primitives.IntegerField)
    """ Dose number within series.
        Type `int`. """

    doseStatus = Column(primitives.StringField,
                        ForeignKey('CodeableConcept.id'))
    """ Indicates if dose counts towards immunity.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    doseStatusReason = Column(primitives.StringField,
                              ForeignKey('CodeableConcept.id'))
    """ Why dose does (not) count.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    series = Column(primitives.StringField)
    """ Name of vaccine series.
        Type `str`. """

    seriesDoses = Column(primitives.IntegerField)
    """ Recommended number of doses for immunity.
        Type `int`. """

    targetDisease = Column(primitives.StringField,
                           ForeignKey('CodeableConcept.id'))
    """ Disease immunized against.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, authority, description, doseSequence, doseStatus,
                 doseStatusReason, series, seriesDoses, targetDisease,):
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


class Immunization(domainresource.DomainResource):
    """ Immunization event information.

    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or another
    party and may include vaccine reaction information and what vaccination
    protocol was followed.
    """

    __tablename__ = "Immunization"
    
    date = Column(primitives.DateTimeField)
    """ Vaccination administration date.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    doseQuantity = Column(primitives.StringField,
                          ForeignKey('Quantity.id'))
    """ Amount of vaccine administered.
        Type `Quantity` referencing `SimpleQuantity`
        (represented as `dict` in JSON). """
    
    # todo encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ Encounter administered as part of.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
    
    expirationDate = Column(primitives.DateTimeField)
    """ Vaccine expiration date.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    explanation = Column(primitives.StringField,
                         ForeignKey('ImmunizationExplanation.id'))
    """ Administration/non-administration reasons.
        Type `ImmunizationExplanation` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    # todo location = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    location = Column(primitives.StringField)
    """ Where vaccination occurred.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
    
    lotNumber = Column(primitives.StringField)
    """ Vaccine lot number.
        Type `str`. """
    
    # todo manufacturer = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    manufacturer = Column(primitives.StringField)
    """ Vaccine manufacturer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
    
    note = Column(primitives.StringField,
                  ForeignKey('Annotation.id'))
    """ Vaccination notes.
        List of `Annotation` items (represented as `dict` in JSON). """
    
    # todo patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    patient = Column(primitives.StringField)
    """ Who was immunized.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    # todo performer = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    performer = Column(primitives.StringField)
    """ Who administered vaccine.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    reaction = Column(primitives.StringField,
                      ForeignKey('ImmunizationReaction.id'))
    """ Details of a reaction that follows immunization.
        List of `ImmunizationReaction` items (represented as `dict` in JSON). """
    
    reported = Column(primitives.BooleanField)
    """ Indicates a self-reported record.
        Type `bool`. """
    
    # todo requester = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    requester = Column(primitives.StringField)
    """ Who ordered vaccination.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    route = Column(primitives.StringField,
                   ForeignKey('CodeableConcept.id'))
    """ How vaccine entered body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    site = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Body site vaccine  was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ in-progress | on-hold | completed | entered-in-error | stopped.
        Type `str`. """
    
    vaccinationProtocol = Column(primitives.StringField,
                                 ForeignKey(
                                     'ImmunizationVaccinationProtocol.id'))
    """ What protocol was followed.
        List of `ImmunizationVaccinationProtocol` items
        (represented as `dict` in JSON). """
    
    vaccineCode = Column(primitives.StringField,
                         ForeignKey('CodeableConcept.id'))
    """ Vaccine product administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    wasNotGiven = Column(primitives.BooleanField)
    """ Flag for whether immunization was given.
        Type `bool`. """

    def __init__(self, date, doseQuantity, encounter, expirationDate,
                 explanation, identifier, location, lotNumber, manufacturer,
                 note, patient, performer, reaction, reported, requester,
                 route, site, status, vaccinationProtocol, vaccineCode, wasNotGiven,):
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
