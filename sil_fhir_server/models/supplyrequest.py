#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/SupplyRequest)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class SupplyRequest(domainresource.DomainResource):
    """ Request for a medication, substance or device.

    A record of a request for a medication, substance or device used in the
    healthcare setting.
    """

    __tablename__ = "SupplyRequest"

    date = Column(FHIRDate)
    """ When the request was made.
        Type `FHIRDate` (represented as `str` in JSON). """

    identifier = Column(Identifier)
    """ Unique identifier.
        Type `Identifier` (represented as `dict` in JSON). """

    kind = Column(CodeableConcept)
    """ The kind of supply (central, non-stock, etc.).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    orderedItem = Column(FHIRReference)
    """ Medication, Substance, or Device requested to be supplied.
        Type `FHIRReference` referencing `Medication, Substance, Device` (represented as `dict` in JSON). """

    patient = Column(FHIRReference)
    """ Patient for whom the item is supplied.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    reasonCodeableConcept = Column(CodeableConcept)
    """ Why the supply item was requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    reasonReference = Column(FHIRReference)
    """ Why the supply item was requested.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    source = Column(FHIRReference)
    """ Who initiated this order.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ requested | completed | failed | cancelled.
        Type `str`. """

    supplier = Column(FHIRReference)
    """ Who is intended to fulfill the request.
        List of `FHIRReference` items referencing `Organization` (represented as `dict` in JSON). """

    when = Column(SupplyRequestWhen)
    """ When the request should be fulfilled.
        Type `SupplyRequestWhen` (represented as `dict` in JSON). """

    def __init__(self, date, identifier, kind, orderedItem, patient, reasonCodeableConcept, reasonReference, source, status, supplier, when,):
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


from sqlalchemy import Column, Integer, String
from . import backboneelement

class SupplyRequestWhen(backboneelement.BackboneElement):
    """ When the request should be fulfilled.
    """

    __tablename__ = "SupplyRequestWhen"

    code = Column(CodeableConcept)
    """ Fulfilment code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    schedule = Column(Timing)
    """ Formal fulfillment schedule.
        Type `Timing` (represented as `dict` in JSON). """

    def __init__(self, code, schedule,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.schedule = schedule

    def __repr__(self):
        return '<SupplyRequestWhen %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import timing