#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Flag)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class Flag(domainresource.DomainResource):
    """ Key information to flag to healthcare providers.

    Prospective warnings of potential issues when providing care to the
    patient.
    """

    __tablename__ = "Flag"

    author = Column(FHIRReference)
    """ Flag creator.
        Type `FHIRReference` referencing `Device, Organization, Patient, Practitioner` (represented as `dict` in JSON). """

    category = Column(CodeableConcept)
    """ Clinical, administrative, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """

    code = Column(CodeableConcept)
    """ Partially deaf, Requires easy open caps, No permanent address, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """

    encounter = Column(FHIRReference)
    """ Alert relevant during encounter.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    period = Column(Period)
    """ Time period when flag is active.
        Type `Period` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ active | inactive | entered-in-error.
        Type `str`. """

    subject = Column(FHIRReference)
    """ Who/What is flag about?.
        Type `FHIRReference` referencing `Patient, Location, Group, Organization, Practitioner` (represented as `dict` in JSON). """

    def __init__(self, author, category, code, encounter, identifier, period, status, subject,):
        """ Initialize all valid properties.
        """
        self.author = author
        self.category = category
        self.code = code
        self.encounter = encounter
        self.identifier = identifier
        self.period = period
        self.status = status
        self.subject = subject

    def __repr__(self):
        return '<Flag %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import period