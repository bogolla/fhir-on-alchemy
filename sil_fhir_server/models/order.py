#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Order)
#  Date: 2016-03-18.


from . import domainresource

class Order(domainresource.DomainResource):
    """ A request to perform an action.
    """

    __tablename__ = "Order"

    date = Column()
    """ When the order was made.
        Type `FHIRDate` (represented as `str` in JSON). """

    detail = Column(FHIRReference)
    """ What action is being ordered.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Identifiers assigned to this order by the orderer or by the
        receiver.
        List of `Identifier` items (represented as `dict` in JSON). """

    reasonCodeableConcept = Column()
    """ Text - why the order was made.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    reasonReference = Column()
    """ Text - why the order was made.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    source = Column()
    """ Who initiated the order.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """

    subject = Column()
    """ Patient this order is about.
        Type `FHIRReference` referencing `Patient, Group, Device, Substance` (represented as `dict` in JSON). """

    target = Column()
    """ Who is intended to fulfill the order.
        Type `FHIRReference` referencing `Organization, Device, Practitioner` (represented as `dict` in JSON). """

    when = Column()
    """ When order should be fulfilled.
        Type `OrderWhen` (represented as `dict` in JSON). """

    def __init__(self, date, detail, identifier, reasonCodeableConcept, reasonReference, source, subject, target, when,):
        """ Initialize all valid properties.
        """
        self.date = date
        self.detail = detail
        self.identifier = identifier
        self.reasonCodeableConcept = reasonCodeableConcept
        self.reasonReference = reasonReference
        self.source = source
        self.subject = subject
        self.target = target
        self.when = when

    def __repr__(self):
        return '<Order %r>' % 'self.property'  # replace self.property


from . import backboneelement

class OrderWhen(backboneelement.BackboneElement):
    """ When order should be fulfilled.
    """

    __tablename__ = "OrderWhen"

    code = Column()
    """ Code specifies when request should be done. The code may simply be
        a priority code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    schedule = Column()
    """ A formal schedule.
        Type `Timing` (represented as `dict` in JSON). """

    def __init__(self, code, schedule,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.schedule = schedule

    def __repr__(self):
        return '<OrderWhen %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import timing