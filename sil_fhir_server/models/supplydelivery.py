#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/SupplyDelivery)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource

class SupplyDelivery(domainresource.DomainResource):
    """ Delivery of Supply.

    Record of delivery of what is supplied.
    """

    __tablename__ = "SupplyDelivery"
    
    # todo destination = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    destination = Column(primitives.StringField)
    """ Where the Supply was sent.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ External identifier.
        Type `Identifier` (represented as `dict` in JSON). """
    
    # todo patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    patient = Column(primitives.StringField)
    """ Patient for whom the item is supplied.
        Type `FHIRReference` referencing `Patient`
        (represented as `dict` in JSON). """
    
    quantity = Column(primitives.StringField,
                      ForeignKey('Quantity.id'))
    """ Amount dispensed.
        Type `Quantity` referencing `SimpleQuantity`
        (represented as `dict` in JSON). """
    
    # todo receiver = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    receiver = Column(primitives.StringField)
    """ Who collected the Supply.
        List of `FHIRReference` items referencing `Practitioner`
        (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ in-progress | completed | abandoned.
        Type `str`. """
    
    # todo suppliedItem = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    suppliedItem = Column(primitives.StringField)
    """ Medication, Substance, or Device supplied.
        Type `FHIRReference` referencing `Medication, Substance, Device`
        (represented as `dict` in JSON). """
    
    # todo supplier = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    supplier = Column(primitives.StringField)
    """ Dispenser.
        Type `FHIRReference` referencing `Practitioner`
        (represented as `dict` in JSON). """
    
    time = Column(primitives.DateTimeField)
    """ Handover time.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Category of dispense event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    whenPrepared = Column(primitives.StringField,
                          ForeignKey('Period.id'))
    """ Dispensing time.
        Type `Period` (represented as `dict` in JSON). """

    def __init__(self, destination, identifier, patient, quantity, receiver,
                 status, suppliedItem, supplier, time, type, whenPrepared,):
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