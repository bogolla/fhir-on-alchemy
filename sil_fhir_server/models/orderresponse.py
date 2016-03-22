#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/OrderResponse)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class OrderResponse(domainresource.DomainResource):
    """ A response to an order.
    """

    __tablename__ = "OrderResponse"

    date = Column(FHIRDate)
    """ When the response was made.
        Type `FHIRDate` (represented as `str` in JSON). """

    description = Column(primitives.StringField)
    """ Additional description of the response.
        Type `str`. """

    fulfillment = Column(FHIRReference)
    """ Details of the outcome of performing the order.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Identifiers assigned to this order by the orderer or by the
        receiver.
        List of `Identifier` items (represented as `dict` in JSON). """

    orderStatus = Column(primitives.StringField)
    """ pending | review | rejected | error | accepted | cancelled |
        replaced | aborted | completed.
        Type `str`. """

    request = Column(FHIRReference)
    """ The order that this is a response to.
        Type `FHIRReference` referencing `Order` (represented as `dict` in JSON). """

    who = Column(FHIRReference)
    """ Who made the response.
        Type `FHIRReference` referencing `Practitioner, Organization, Device` (represented as `dict` in JSON). """

    def __init__(self, date, description, fulfillment, identifier, orderStatus, request, who,):
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


from . import fhirdate
from . import fhirreference
from . import identifier