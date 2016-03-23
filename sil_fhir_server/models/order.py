#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Order)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class OrderWhen(backboneelement.BackboneElement):
    """ When order should be fulfilled.
    """

    __tablename__ = "OrderWhen"

    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Code specifies when request should be done. The code may simply be
        a priority code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    schedule = Column(primitives.StringField,
                      ForeignKey('Timing.id'))
    """ A formal schedule.
        Type `Timing` (represented as `dict` in JSON). """

    def __init__(self, code, schedule,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.schedule = schedule

    def __repr__(self):
        return '<OrderWhen %r>' % 'self.property'  # replace self.property


class Order(domainresource.DomainResource):
    """ A request to perform an action.
    """

    __tablename__ = "Order"
    
    date = Column(primitives.DateTimeField)
    """ When the order was made.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    # todo detail = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    detail = Column(primitives.StringField)
    """ What action is being ordered.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Identifiers assigned to this order by the orderer or by the
        receiver.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    reasonCodeableConcept = Column(primitives.StringField,
                                   ForeignKey('CodeableConcept.id'))
    """ Text - why the order was made.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo reasonReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    reasonReference = Column(primitives.StringField)
    """ Text - why the order was made.
        Type `FHIRReference` referencing `Resource`
        (represented as `dict` in JSON). """
    
    # todo source = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    source = Column(primitives.StringField)
    """ Who initiated the order.
        Type `FHIRReference` referencing `Practitioner, Organization`
        (represented as `dict` in JSON). """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Patient this order is about.
        Type `FHIRReference` referencing `Patient, Group, Device,
        Substance` (represented as `dict` in JSON). """
    
    # todo target = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    target = Column(primitives.StringField)
    """ Who is intended to fulfill the order.
        Type `FHIRReference` referencing `Organization, Device, Practitioner`
        (represented as `dict` in JSON). """
    
    when = Column(primitives.StringField, ForeignKey('OrderWhen.id'))
    """ When order should be fulfilled.
        Type `OrderWhen` (represented as `dict` in JSON). """

    def __init__(self, date, detail, identifier, reasonCodeableConcept,
                 reasonReference, source, subject, target, when,):
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
