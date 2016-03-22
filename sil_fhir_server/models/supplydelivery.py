#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/SupplyDelivery)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class SupplyDelivery(domainresource.DomainResource):
    """ Delivery of Supply.

    Record of delivery of what is supplied.
    """

    __tablename__ = "SupplyDelivery"

    destination = Column(FHIRReference)
    """ Where the Supply was sent.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ External identifier.
        Type `Identifier` (represented as `dict` in JSON). """

    patient = Column(FHIRReference)
    """ Patient for whom the item is supplied.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    quantity = Column(Quantity)
    """ Amount dispensed.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    receiver = Column(FHIRReference)
    """ Who collected the Supply.
        List of `FHIRReference` items referencing `Practitioner` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ in-progress | completed | abandoned.
        Type `str`. """

    suppliedItem = Column(FHIRReference)
    """ Medication, Substance, or Device supplied.
        Type `FHIRReference` referencing `Medication, Substance, Device` (represented as `dict` in JSON). """

    supplier = Column(FHIRReference)
    """ Dispenser.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    time = Column(FHIRDate)
    """ Handover time.
        Type `FHIRDate` (represented as `str` in JSON). """

    type = Column(CodeableConcept)
    """ Category of dispense event.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    whenPrepared = Column(Period)
    """ Dispensing time.
        Type `Period` (represented as `dict` in JSON). """

    def __init__(self, destination, identifier, patient, quantity, receiver, status, suppliedItem, supplier, time, type, whenPrepared,):
        """ Initialize all valid properties.
        """
        self.destination = destination
        self.identifier = identifier
        self.patient = patient
        self.quantity = quantity
        self.receiver = receiver
        self.status = status
        self.suppliedItem = suppliedItem
        self.supplier = supplier
        self.time = time
        self.type = type
        self.whenPrepared = whenPrepared

    def __repr__(self):
        return '<SupplyDelivery %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity