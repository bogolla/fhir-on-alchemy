#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Flag)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource


class Flag(domainresource.DomainResource):
    """ Key information to flag to healthcare providers.

    Prospective warnings of potential issues when providing care to the
    patient.
    """

    __tablename__ = "Flag"
    
    # todo author = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    author = Column(primitives.StringField)
    """ Flag creator.
        Type `FHIRReference` referencing `Device, Organization,
        Patient, Practitioner` (represented as `dict` in JSON). """
    
    category = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Clinical, administrative, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Partially deaf, Requires easy open caps, No permanent address, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ Alert relevant during encounter.
        Type `FHIRReference` referencing `Encounter`
        (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    period = Column(primitives.StringField,
                    ForeignKey('Period.id'))
    """ Time period when flag is active.
        Type `Period` (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ active | inactive | entered-in-error.
        Type `str`. """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Who/What is flag about?.
        Type `FHIRReference` referencing `Patient, Location, Group, Organization,
        Practitioner` (represented as `dict` in JSON). """

    def __init__(self, author, category, code, encounter, identifier,
                 period, status, subject,):
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
