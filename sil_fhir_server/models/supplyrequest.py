#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/SupplyRequest)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class SupplyRequestWhen(backboneelement.BackboneElement):
    """ When the request should be fulfilled.
    """

    __tablename__ = "SupplyRequestWhen"

    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Fulfilment code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    schedule = Column(primitives.StringField,
                      ForeignKey('Timing.id'))
    """ Formal fulfillment schedule.
        Type `Timing` (represented as `dict` in JSON). """

    def __init__(self, code, schedule,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.schedule = schedule

    def __repr__(self):
        return '<SupplyRequestWhen %r>' % 'self.property'  # replace self.property


class SupplyRequest(domainresource.DomainResource):
    """ Request for a medication, substance or device.

    A record of a request for a medication, substance or device used in the
    healthcare setting.
    """

    __tablename__ = "SupplyRequest"
    
    date = Column(primitives.DateTimeField)
    """ When the request was made.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Unique identifier.
        Type `Identifier` (represented as `dict` in JSON). """
    
    kind = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ The kind of supply (central, non-stock, etc.).
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo orderedItem = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    orderedItem = Column(primitives.StringField)
    """ Medication, Substance, or Device requested to be supplied.
        Type `FHIRReference` referencing `Medication, Substance,
        Device` (represented as `dict` in JSON). """
    
    # todo patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    patient = Column(primitives.StringField)
    """ Patient for whom the item is supplied.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    reasonCodeableConcept = Column(primitives.StringField,
                                   ForeignKey('CodeableConcept.id'))
    """ Why the supply item was requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo reasonReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    reasonReference = Column(primitives.StringField)
    """ Why the supply item was requested.
        Type `FHIRReference` referencing `Resource`
        (represented as `dict` in JSON). """
    
    # todo source = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    source = Column(primitives.StringField)
    """ Who initiated this order.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient`
        (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ requested | completed | failed | cancelled.
        Type `str`. """
    
    # todo supplier = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    supplier = Column(primitives.StringField)
    """ Who is intended to fulfill the request.
        List of `FHIRReference` items referencing `Organization`
        (represented as `dict` in JSON). """
    
    when = Column(primitives.StringField,
                  ForeignKey('SupplyRequestWhen.id'))
    """ When the request should be fulfilled.
        Type `SupplyRequestWhen` (represented as `dict` in JSON). """

    def __init__(self, date, identifier, kind, orderedItem, patient,
                 reasonCodeableConcept, reasonReference, source, status,
                 supplier, when,):
        """ Initialize all valid properties.
        """
        self.date = date
        self.identifier = identifier
        self.kind = kind
        self.orderedItem = orderedItem
        self.patient = patient
        self.reasonCodeableConcept = reasonCodeableConcept
        self.reasonReference = reasonReference
        self.source = source
        self.status = status
        self.supplier = supplier
        self.when = when

    def __repr__(self):
        return '<SupplyRequest %r>' % 'self.property'  # replace self.property
