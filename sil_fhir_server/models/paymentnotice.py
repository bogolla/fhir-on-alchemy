#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/PaymentNotice)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource

class PaymentNotice(domainresource.DomainResource):
    """ PaymentNotice request.

    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """

    __tablename__ = "PaymentNotice"
    
    created = Column(primitives.DateTimeField)
    """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    # todo organization = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    organization = Column(primitives.StringField)
    """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
    
    originalRuleset = Column(primitives.StringField,
                             ForeignKey('Coding.id'))
    """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
    
    paymentStatus = Column(primitives.StringField,
                           ForeignKey('Coding.id'))
    """ Status of the payment.
        Type `Coding` (represented as `dict` in JSON). """
    
    # todo provider = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    provider = Column(primitives.StringField)
    """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    # todo request = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    request = Column(primitives.StringField)
    """ Request reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
    
    # todo response = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    response = Column(primitives.StringField)
    """ Response reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
    
    ruleset = Column(primitives.StringField,
                     ForeignKey('Coding.id'))
    """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
    
    # todo target = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    target = Column(primitives.StringField)
    """ Insurer or Regulatory body.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    def __init__(self, created, identifier, organization, originalRuleset,
                 paymentStatus, provider, request, response, ruleset, target,):
        """ Initialize all valid properties.
        """
        self.created = created
        self.identifier = identifier
        self.organization = organization
        self.originalRuleset = originalRuleset
        self.paymentStatus = paymentStatus
        self.provider = provider
        self.request = request
        self.response = response
        self.ruleset = ruleset
        self.target = target

    def __repr__(self):
        return '<PaymentNotice %r>' % 'self.property'  # replace self.property