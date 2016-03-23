#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/OrderResponse)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource

class OrderResponse(domainresource.DomainResource):
    """ A response to an order.
    """

    __tablename__ = "OrderResponse"
    
    date = Column(primitives.DateTimeField)
    """ When the response was made.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    description = Column(primitives.StringField)
    """ Additional description of the response.
        Type `str`. """
    
    # todo fulfillment = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    fulfillment = Column(primitives.StringField)
    """ Details of the outcome of performing the order.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Identifiers assigned to this order by the orderer or by the
        receiver.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    orderStatus = Column(primitives.StringField)
    """ pending | review | rejected | error | accepted | cancelled |
        replaced | aborted | completed.
        Type `str`. """
    
    # todo request = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    request = Column(primitives.StringField)
    """ The order that this is a response to.
        Type `FHIRReference` referencing `Order` (represented as `dict` in JSON). """

    # todo who = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    who = Column(primitives.StringField)
    """ Who made the response.
        Type `FHIRReference` referencing `Practitioner, Organization, Device`
        (represented as `dict` in JSON). """

    def __init__(self, date, description, fulfillment, identifier,
                 orderStatus, request, who,):
        """ Initialize all valid properties.
        """
        self.date = date
        self.description = description
        self.fulfillment = fulfillment
        self.identifier = identifier
        self.orderStatus = orderStatus
        self.request = request
        self.who = who

    def __repr__(self):
        return '<OrderResponse %r>' % 'self.property'  # replace self.property