#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/PaymentNotice)
#  Date: 2016-03-18.


from . import domainresource

class PaymentNotice(domainresource.DomainResource):
    """ PaymentNotice request.

    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """

    __tablename__ = "PaymentNotice"

    created = Column()
    """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

    identifier = Column(Identifier)
    """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    organization = Column()
    """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    originalRuleset = Column()
    """ Original version.
        Type `Coding` (represented as `dict` in JSON). """

    paymentStatus = Column()
    """ Status of the payment.
        Type `Coding` (represented as `dict` in JSON). """

    provider = Column()
    """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    request = Column()
    """ Request reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    response = Column()
    """ Response reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    ruleset = Column()
    """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """

    target = Column()
    """ Insurer or Regulatory body.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    def __init__(self, created, identifier, organization, originalRuleset, paymentStatus, provider, request, response, ruleset, target,):
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


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier