#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/PaymentReconciliation)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class PaymentReconciliation(domainresource.DomainResource):
    """ PaymentReconciliation resource.

    This resource provides payment details and claim references supporting a
    bulk payment.
    """

    __tablename__ = "PaymentReconciliation"

    created = Column(FHIRDate)
    """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

    detail = Column(PaymentReconciliationDetail)
    """ Details.
        List of `PaymentReconciliationDetail` items (represented as `dict` in JSON). """

    disposition = Column(primitives.StringField)
    """ Disposition Message.
        Type `str`. """

    form = Column(Coding)
    """ Printed Form Identifier.
        Type `Coding` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    note = Column(PaymentReconciliationNote)
    """ Note text.
        List of `PaymentReconciliationNote` items (represented as `dict` in JSON). """

    organization = Column(FHIRReference)
    """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    originalRuleset = Column(Coding)
    """ Original version.
        Type `Coding` (represented as `dict` in JSON). """

    outcome = Column(primitives.StringField)
    """ complete | error.
        Type `str`. """

    period = Column(Period)
    """ Period covered.
        Type `Period` (represented as `dict` in JSON). """

    request = Column(FHIRReference)
    """ Claim reference.
        Type `FHIRReference` referencing `ProcessRequest` (represented as `dict` in JSON). """

    requestOrganization = Column(FHIRReference)
    """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    requestProvider = Column(FHIRReference)
    """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    ruleset = Column(Coding)
    """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """

    total = Column(Quantity)
    """ Total amount of Payment.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    def __init__(self, created, detail, disposition, form, identifier, note, organization, originalRuleset, outcome, period, request, requestOrganization, requestProvider, ruleset, total,):
        """ Initialize all valid properties.
        """
        self.created = created
        self.detail = detail
        self.disposition = disposition
        self.form = form
        self.identifier = identifier
        self.note = note
        self.organization = organization
        self.originalRuleset = originalRuleset
        self.outcome = outcome
        self.period = period
        self.request = request
        self.requestOrganization = requestOrganization
        self.requestProvider = requestProvider
        self.ruleset = ruleset
        self.total = total

    def __repr__(self):
        return '<PaymentReconciliation %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class PaymentReconciliationDetail(backboneelement.BackboneElement):
    """ Details.

    List of individual settlement amounts and the corresponding transaction.
    """

    __tablename__ = "PaymentReconciliationDetail"

    amount = Column(Quantity)
    """ Detail amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    date = Column(FHIRDate)
    """ Invoice date.
        Type `FHIRDate` (represented as `str` in JSON). """

    payee = Column(FHIRReference)
    """ Payee.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    request = Column(FHIRReference)
    """ Claim.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    responce = Column(FHIRReference)
    """ Claim Response.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    submitter = Column(FHIRReference)
    """ Submitter.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    type = Column(Coding)
    """ Type code.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, amount, date, payee, request, responce, submitter, type,):
        """ Initialize all valid properties.
        """
        self.amount = amount
        self.date = date
        self.payee = payee
        self.request = request
        self.responce = responce
        self.submitter = submitter
        self.type = type

    def __repr__(self):
        return '<PaymentReconciliationDetail %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class PaymentReconciliationNote(backboneelement.BackboneElement):
    """ Note text.

    Suite of notes.
    """

    __tablename__ = "PaymentReconciliationNote"

    text = Column(primitives.StringField)
    """ Notes text.
        Type `str`. """

    type = Column(Coding)
    """ display | print | printoper.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, text, type,):
        """ Initialize all valid properties.
        """
        self.text = text
        self.type = type

    def __repr__(self):
        return '<PaymentReconciliationNote %r>' % 'self.property'  # replace self.property


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity