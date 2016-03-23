#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Account)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource


class Account(domainresource.DomainResource):
    """ None.

    A financial tool for tracking value accrued for a particular purpose.  In
    the healthcare field, used to track charges for a patient, cost centres,
    etc.
    """

    __tablename__ = "Account"
    
    activePeriod = Column(primitives.StringField,
                          ForeignKey('Period.id'))
    """ Valid from..to.
        Type `Period` (represented as `dict` in JSON). """
    
    balance = Column(primitives.StringField,
                     ForeignKey('Quantity.id'))
    """ How much is in account?.
        Type `Quantity` referencing `Money` (represented as `dict`
        in JSON). """
    
    coveragePeriod = Column(primitives.StringField,
                            ForeignKey('Period.id'))
    """ Transaction window.
        Type `Period` (represented as `dict` in JSON). """
    
    currency = Column(primitives.StringField,
                      ForeignKey('Coding.id'))
    """ Base currency in which balance is tracked.
        Type `Coding` (represented as `dict` in JSON). """
    
    description = Column(primitives.StringField)
    """ Explanation of purpose/use.
        Type `str`. """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Account number.
        List of `Identifier` items (represented as `dict` in JSON).
        """
    
    name = Column(primitives.StringField)
    """ Human-readable label.
        Type `str`. """

    # TODO add owner field
    # owner = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Who is responsible?.
        Type `FHIRReference` referencing `Organization` (represented
        as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ active | inactive.
        Type `str`. """
    
    # subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ What is account tied to?.
        Type `FHIRReference` referencing `Patient, Device,
        Practitioner, Location, HealthcareService, Organization`
        (represented as `dict` in JSON). """
    
    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ E.g. patient, expense, depreciation.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, activePeriod, balance, coveragePeriod,
                 currency, description, identifier, name, owner,
                 status, subject, type):
        """ Initialize all valid properties.
        """
        self.activePeriod = activePeriod
        self.balance = balance
        self.coveragePeriod = coveragePeriod
        self.currency = currency
        self.description = description
        self.identifier = identifier
        self.name = name
        self.owner = owner
        self.status = status
        self.subject = subject
        self.type = type

    def __repr__(self):
        return '<Account %r>' % 'self.property'  # replace self.property