#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Coverage)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource


class Coverage(domainresource.DomainResource):
    """ Insurance or medical plan.

    Financial instrument which may be used to pay for or reimburse health care
    products and services.
    """

    __tablename__ = "Coverage"
    
    bin = Column(primitives.StringField,
                 ForeignKey('Identifier.id'))
    """ BIN Number.
        Type `Identifier` (represented as `dict` in JSON). """
    
    # todo contract = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    contract = Column(primitives.StringField)
    """ Contract details.
        List of `FHIRReference` items referencing `Contract` (represented as `dict` in JSON). """
    
    dependent = Column(primitives.IntegerField)
    """ The dependent number.
        Type `int`. """
    
    group = Column(primitives.StringField)
    """ An identifier for the group.
        Type `str`. """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ The primary coverage ID.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    # todo issuer = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    issuer = Column(primitives.StringField)
    """ An identifier for the plan issuer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
    
    network = Column(primitives.StringField,
                     ForeignKey('Identifier.id'))
    """ Insurer network.
        Type `Identifier` (represented as `dict` in JSON). """
    
    period = Column(primitives.StringField,
                    ForeignKey('Period.id'))
    """ Coverage start and end dates.
        Type `Period` (represented as `dict` in JSON). """
    
    plan = Column(primitives.StringField)
    """ An identifier for the plan.
        Type `str`. """
    
    sequence = Column(primitives.IntegerField)
    """ The plan instance or sequence counter.
        Type `int`. """
    
    subPlan = Column(primitives.StringField)
    """ An identifier for the subsection of the plan.
        Type `str`. """
    
    # todo subscriber = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subscriber = Column(primitives.StringField)
    """ Plan holder information.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    subscriberId = Column(primitives.StringField,
                          ForeignKey('Identifier.id'))
    """ Subscriber ID.
        Type `Identifier` (represented as `dict` in JSON). """
    
    type = Column(primitives.StringField,
                  ForeignKey('Coding.id'))
    """ Type of coverage.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, bin, contract, dependent, group, identifier,
                 issuer, network, period, plan, sequence, subPlan,
                 subscriber, subscriberId, type,):
        """ Initialize all valid properties.
        """
        self.bin = bin
        self.contract = contract
        self.dependent = dependent
        self.group = group
        self.identifier = identifier
        self.issuer = issuer
        self.network = network
        self.period = period
        self.plan = plan
        self.sequence = sequence
        self.subPlan = subPlan
        self.subscriber = subscriber
        self.subscriberId = subscriberId
        self.type = type

    def __repr__(self):
        return '<Coverage %r>' % 'self.property'  # replace self.property