#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Coverage)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class Coverage(domainresource.DomainResource):
    """ Insurance or medical plan.

    Financial instrument which may be used to pay for or reimburse health care
    products and services.
    """

    __tablename__ = "Coverage"

    bin = Column(Identifier)
    """ BIN Number.
        Type `Identifier` (represented as `dict` in JSON). """

    contract = Column(FHIRReference)
    """ Contract details.
        List of `FHIRReference` items referencing `Contract` (represented as `dict` in JSON). """

    dependent = Column(Integer)
    """ The dependent number.
        Type `int`. """

    group = Column(primitives.StringField)
    """ An identifier for the group.
        Type `str`. """

    identifier = Column(Identifier)
    """ The primary coverage ID.
        List of `Identifier` items (represented as `dict` in JSON). """

    issuer = Column(FHIRReference)
    """ An identifier for the plan issuer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    network = Column(Identifier)
    """ Insurer network.
        Type `Identifier` (represented as `dict` in JSON). """

    period = Column(Period)
    """ Coverage start and end dates.
        Type `Period` (represented as `dict` in JSON). """

    plan = Column(primitives.StringField)
    """ An identifier for the plan.
        Type `str`. """

    sequence = Column(Integer)
    """ The plan instance or sequence counter.
        Type `int`. """

    subPlan = Column(primitives.StringField)
    """ An identifier for the subsection of the plan.
        Type `str`. """

    subscriber = Column(FHIRReference)
    """ Plan holder information.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    subscriberId = Column(Identifier)
    """ Subscriber ID.
        Type `Identifier` (represented as `dict` in JSON). """

    type = Column(Coding)
    """ Type of coverage.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, bin, contract, dependent, group, identifier, issuer, network, period, plan, sequence, subPlan, subscriber, subscriberId, type,):
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


from . import coding
from . import fhirreference
from . import identifier
from . import period