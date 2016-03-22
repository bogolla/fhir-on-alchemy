#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/AllergyIntolerance)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer
from sil_fhir_server.data_types import primitives
from . import domainresource

class AllergyIntolerance(domainresource.DomainResource):
    """ Allergy or Intolerance (generally: Risk Of Adverse reaction to a substance).

    Risk of harmful or undesirable, physiological response which is unique to
    an individual and associated with exposure to a substance.
    """

    __tablename__ = "AllergyIntolerance"

    category = Column(primitives.StringField)
    """ food | medication | environment | other - Category of Substance.
        Type `str`. """

    criticality = Column(primitives.StringField)
    """ CRITL | CRITH | CRITU.
        Type `str`. """

    identifier = Column(Identifier)
    """ External ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """

    lastOccurence = Column(FHIRDate)
    """ Date(/time) of last known occurrence of a reaction.
        Type `FHIRDate` (represented as `str` in JSON). """

    note = Column(Annotation)
    """ Additional text not captured in other fields.
        Type `Annotation` (represented as `dict` in JSON). """

    onset = Column(FHIRDate)
    """ Date(/time) when manifestations showed.
        Type `FHIRDate` (represented as `str` in JSON). """

    patient = Column(FHIRReference)
    """ Who the sensitivity is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    reaction = Column(AllergyIntoleranceReaction)
    """ Adverse Reaction Events linked to exposure to substance.
        List of `AllergyIntoleranceReaction` items (represented as `dict` in JSON). """

    recordedDate = Column(FHIRDate)
    """ When recorded.
        Type `FHIRDate` (represented as `str` in JSON). """

    recorder = Column(FHIRReference)
    """ Who recorded the sensitivity.
        Type `FHIRReference` referencing `Practitioner, Patient` (represented as `dict` in JSON). """

    reporter = Column(FHIRReference)
    """ Source of the information about the allergy.
        Type `FHIRReference` referencing `Patient, RelatedPerson, Practitioner` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ active | unconfirmed | confirmed | inactive | resolved | refuted |
        entered-in-error.
        Type `str`. """

    substance = Column(CodeableConcept)
    """ Substance, (or class) considered to be responsible for risk.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    type = Column(primitives.StringField)
    """ allergy | intolerance - Underlying mechanism (if known).
        Type `str`. """

    def __init__(self, category, criticality, identifier, lastOccurence, note, onset, patient, reaction, recordedDate, recorder, reporter, status, substance, type,):
        """ Initialize all valid properties.
        """
        self.category = category
        self.criticality = criticality
        self.identifier = identifier
        self.lastOccurence = lastOccurence
        self.note = note
        self.onset = onset
        self.patient = patient
        self.reaction = reaction
        self.recordedDate = recordedDate
        self.recorder = recorder
        self.reporter = reporter
        self.status = status
        self.substance = substance
        self.type = type

    def __repr__(self):
        return '<AllergyIntolerance %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class AllergyIntoleranceReaction(backboneelement.BackboneElement):
    """ Adverse Reaction Events linked to exposure to substance.

    Details about each adverse reaction event linked to exposure to the
    identified Substance.
    """

    __tablename__ = "AllergyIntoleranceReaction"

    certainty = Column(primitives.StringField)
    """ unlikely | likely | confirmed - clinical certainty about the
        specific substance.
        Type `str`. """

    description = Column(primitives.StringField)
    """ Description of the event as a whole.
        Type `str`. """

    exposureRoute = Column(CodeableConcept)
    """ How the subject was exposed to the substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    manifestation = Column(CodeableConcept)
    """ Clinical symptoms/signs associated with the Event.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    note = Column(Annotation)
    """ Text about event not captured in other fields.
        Type `Annotation` (represented as `dict` in JSON). """

    onset = Column(FHIRDate)
    """ Date(/time) when manifestations showed.
        Type `FHIRDate` (represented as `str` in JSON). """

    severity = Column(primitives.StringField)
    """ mild | moderate | severe (of event as a whole).
        Type `str`. """

    substance = Column(CodeableConcept)
    """ Specific substance considered to be responsible for event.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, certainty, description, exposureRoute, manifestation, note, onset, severity, substance,):
        """ Initialize all valid properties.
        """
        self.certainty = certainty
        self.description = description
        self.exposureRoute = exposureRoute
        self.manifestation = manifestation
        self.note = note
        self.onset = onset
        self.severity = severity
        self.substance = substance

    def __repr__(self):
        return '<AllergyIntoleranceReaction %r>' % 'self.property'  # replace self.property


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier