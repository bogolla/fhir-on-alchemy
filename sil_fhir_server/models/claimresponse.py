#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ClaimResponse)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer
from sil_fhir_server.data_types import primitives
from . import domainresource

class ClaimResponse(domainresource.DomainResource):
    """ Remittance resource.

    This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    __tablename__ = "ClaimResponse"

    addItem = Column(ClaimResponseAddItem)
    """ Insurer added line items.
        List of `ClaimResponseAddItem` items (represented as `dict` in JSON). """

    coverage = Column(ClaimResponseCoverage)
    """ Insurance or medical plan.
        List of `ClaimResponseCoverage` items (represented as `dict` in JSON). """

    created = Column(FHIRDate)
    """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

    disposition = Column(primitives.StringField)
    """ Disposition Message.
        Type `str`. """

    error = Column(ClaimResponseError)
    """ Processing errors.
        List of `ClaimResponseError` items (represented as `dict` in JSON). """

    form = Column(Coding)
    """ Printed Form Identifier.
        Type `Coding` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Response  number.
        List of `Identifier` items (represented as `dict` in JSON). """

    item = Column(ClaimResponseItem)
    """ Line items.
        List of `ClaimResponseItem` items (represented as `dict` in JSON). """

    note = Column(ClaimResponseNote)
    """ Processing notes.
        List of `ClaimResponseNote` items (represented as `dict` in JSON). """

    organization = Column(FHIRReference)
    """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    originalRuleset = Column(Coding)
    """ Original version.
        Type `Coding` (represented as `dict` in JSON). """

    outcome = Column(primitives.StringField)
    """ complete | error.
        Type `str`. """

    payeeType = Column(Coding)
    """ Party to be paid any benefits payable.
        Type `Coding` (represented as `dict` in JSON). """

    paymentAdjustment = Column(Quantity)
    """ Payment adjustment for non-Claim issues.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    paymentAdjustmentReason = Column(Coding)
    """ Reason for Payment adjustment.
        Type `Coding` (represented as `dict` in JSON). """

    paymentAmount = Column(Quantity)
    """ Payment amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    paymentDate = Column(FHIRDate)
    """ Expected data of Payment.
        Type `FHIRDate` (represented as `str` in JSON). """

    paymentRef = Column(Identifier)
    """ Payment identifier.
        Type `Identifier` (represented as `dict` in JSON). """

    request = Column(FHIRReference)
    """ Id of resource triggering adjudication.
        Type `FHIRReference` referencing `Claim` (represented as `dict` in JSON). """

    requestOrganization = Column(FHIRReference)
    """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    requestProvider = Column(FHIRReference)
    """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    reserved = Column(Coding)
    """ Funds reserved status.
        Type `Coding` (represented as `dict` in JSON). """

    ruleset = Column(Coding)
    """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """

    totalBenefit = Column(Quantity)
    """ Total benefit payable for the Claim.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    totalCost = Column(Quantity)
    """ Total Cost of service from the Claim.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    unallocDeductable = Column(Quantity)
    """ Unallocated deductible.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    def __init__(self, addItem, coverage, created, disposition, error, form, identifier, item, note, organization, originalRuleset, outcome, payeeType, paymentAdjustment, paymentAdjustmentReason, paymentAmount, paymentDate, paymentRef, request, requestOrganization, requestProvider, reserved, ruleset, totalBenefit, totalCost, unallocDeductable,):
        """ Initialize all valid properties.
        """
        self.addItem = addItem
        self.coverage = coverage
        self.created = created
        self.disposition = disposition
        self.error = error
        self.form = form
        self.identifier = identifier
        self.item = item
        self.note = note
        self.organization = organization
        self.originalRuleset = originalRuleset
        self.outcome = outcome
        self.payeeType = payeeType
        self.paymentAdjustment = paymentAdjustment
        self.paymentAdjustmentReason = paymentAdjustmentReason
        self.paymentAmount = paymentAmount
        self.paymentDate = paymentDate
        self.paymentRef = paymentRef
        self.request = request
        self.requestOrganization = requestOrganization
        self.requestProvider = requestProvider
        self.reserved = reserved
        self.ruleset = ruleset
        self.totalBenefit = totalBenefit
        self.totalCost = totalCost
        self.unallocDeductable = unallocDeductable

    def __repr__(self):
        return '<ClaimResponse %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class ClaimResponseAddItem(backboneelement.BackboneElement):
    """ Insurer added line items.

    The first tier service adjudications for payor added services.
    """

    __tablename__ = "ClaimResponseAddItem"

    adjudication = Column(ClaimResponseAddItemAdjudication)
    """ Added items adjudication.
        List of `ClaimResponseAddItemAdjudication` items (represented as `dict` in JSON). """

    detail = Column(ClaimResponseAddItemDetail)
    """ Added items details.
        List of `ClaimResponseAddItemDetail` items (represented as `dict` in JSON). """

    fee = Column(Quantity)
    """ Professional fee or Product charge.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    noteNumberLinkId = Column(Integer)
    """ List of note numbers which apply.
        List of `int` items. """

    sequenceLinkId = Column(Integer)
    """ Service instances.
        List of `int` items. """

    service = Column(Coding)
    """ Group, Service or Product.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, adjudication, detail, fee, noteNumberLinkId, sequenceLinkId, service,):
        """ Initialize all valid properties.
        """
        self.adjudication = adjudication
        self.detail = detail
        self.fee = fee
        self.noteNumberLinkId = noteNumberLinkId
        self.sequenceLinkId = sequenceLinkId
        self.service = service

    def __repr__(self):
        return '<ClaimResponseAddItem %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ClaimResponseAddItemAdjudication(backboneelement.BackboneElement):
    """ Added items adjudication.

    The adjudications results.
    """

    __tablename__ = "ClaimResponseAddItemAdjudication"

    amount = Column(Quantity)
    """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    code = Column(Coding)
    """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """

    value = Column(float)
    """ Non-monetary value.
        Type `float`. """

    def __init__(self, amount, code, value,):
        """ Initialize all valid properties.
        """
        self.amount = amount
        self.code = code
        self.value = value

    def __repr__(self):
        return '<ClaimResponseAddItemAdjudication %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ClaimResponseAddItemDetail(backboneelement.BackboneElement):
    """ Added items details.

    The second tier service adjudications for payor added services.
    """

    __tablename__ = "ClaimResponseAddItemDetail"

    adjudication = Column(ClaimResponseAddItemDetailAdjudication)
    """ Added items detail adjudication.
        List of `ClaimResponseAddItemDetailAdjudication` items (represented as `dict` in JSON). """

    fee = Column(Quantity)
    """ Professional fee or Product charge.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    service = Column(Coding)
    """ Service or Product.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, adjudication, fee, service,):
        """ Initialize all valid properties.
        """
        self.adjudication = adjudication
        self.fee = fee
        self.service = service

    def __repr__(self):
        return '<ClaimResponseAddItemDetail %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ClaimResponseAddItemDetailAdjudication(backboneelement.BackboneElement):
    """ Added items detail adjudication.

    The adjudications results.
    """

    __tablename__ = "ClaimResponseAddItemDetailAdjudication"

    amount = Column(Quantity)
    """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    code = Column(Coding)
    """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """

    value = Column(float)
    """ Non-monetary value.
        Type `float`. """

    def __init__(self, amount, code, value,):
        """ Initialize all valid properties.
        """
        self.amount = amount
        self.code = code
        self.value = value

    def __repr__(self):
        return '<ClaimResponseAddItemDetailAdjudication %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ClaimResponseCoverage(backboneelement.BackboneElement):
    """ Insurance or medical plan.

    Financial instrument by which payment information for health care.
    """

    __tablename__ = "ClaimResponseCoverage"

    businessArrangement = Column(primitives.StringField)
    """ Business agreement.
        Type `str`. """

    claimResponse = Column(FHIRReference)
    """ Adjudication results.
        Type `FHIRReference` referencing `ClaimResponse` (represented as `dict` in JSON). """

    coverage = Column(FHIRReference)
    """ Insurance information.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """

    focal = Column(bool)
    """ Is the focal Coverage.
        Type `bool`. """

    originalRuleset = Column(Coding)
    """ Original version.
        Type `Coding` (represented as `dict` in JSON). """

    preAuthRef = Column(primitives.StringField)
    """ Pre-Authorization/Determination Reference.
        List of `str` items. """

    relationship = Column(Coding)
    """ Patient relationship to subscriber.
        Type `Coding` (represented as `dict` in JSON). """

    sequence = Column(Integer)
    """ Service instance identifier.
        Type `int`. """

    def __init__(self, businessArrangement, claimResponse, coverage, focal, originalRuleset, preAuthRef, relationship, sequence,):
        """ Initialize all valid properties.
        """
        self.businessArrangement = businessArrangement
        self.claimResponse = claimResponse
        self.coverage = coverage
        self.focal = focal
        self.originalRuleset = originalRuleset
        self.preAuthRef = preAuthRef
        self.relationship = relationship
        self.sequence = sequence

    def __repr__(self):
        return '<ClaimResponseCoverage %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ClaimResponseError(backboneelement.BackboneElement):
    """ Processing errors.

    Mutually exclusive with Services Provided (Item).
    """

    __tablename__ = "ClaimResponseError"

    code = Column(Coding)
    """ Error code detailing processing issues.
        Type `Coding` (represented as `dict` in JSON). """

    detailSequenceLinkId = Column(Integer)
    """ Detail sequence number.
        Type `int`. """

    sequenceLinkId = Column(Integer)
    """ Item sequence number.
        Type `int`. """

    subdetailSequenceLinkId = Column(Integer)
    """ Subdetail sequence number.
        Type `int`. """

    def __init__(self, code, detailSequenceLinkId, sequenceLinkId, subdetailSequenceLinkId,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.detailSequenceLinkId = detailSequenceLinkId
        self.sequenceLinkId = sequenceLinkId
        self.subdetailSequenceLinkId = subdetailSequenceLinkId

    def __repr__(self):
        return '<ClaimResponseError %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ClaimResponseItem(backboneelement.BackboneElement):
    """ Line items.

    The first tier service adjudications for submitted services.
    """

    __tablename__ = "ClaimResponseItem"

    adjudication = Column(ClaimResponseItemAdjudication)
    """ Adjudication details.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """

    detail = Column(ClaimResponseItemDetail)
    """ Detail line items.
        List of `ClaimResponseItemDetail` items (represented as `dict` in JSON). """

    noteNumber = Column(Integer)
    """ List of note numbers which apply.
        List of `int` items. """

    sequenceLinkId = Column(Integer)
    """ Service instance.
        Type `int`. """

    def __init__(self, adjudication, detail, noteNumber, sequenceLinkId,):
        """ Initialize all valid properties.
        """
        self.adjudication = adjudication
        self.detail = detail
        self.noteNumber = noteNumber
        self.sequenceLinkId = sequenceLinkId

    def __repr__(self):
        return '<ClaimResponseItem %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ClaimResponseItemAdjudication(backboneelement.BackboneElement):
    """ Adjudication details.

    The adjudications results.
    """

    __tablename__ = "ClaimResponseItemAdjudication"

    amount = Column(Quantity)
    """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    code = Column(Coding)
    """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """

    value = Column(float)
    """ Non-monetary value.
        Type `float`. """

    def __init__(self, amount, code, value,):
        """ Initialize all valid properties.
        """
        self.amount = amount
        self.code = code
        self.value = value

    def __repr__(self):
        return '<ClaimResponseItemAdjudication %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ClaimResponseItemDetail(backboneelement.BackboneElement):
    """ Detail line items.

    The second tier service adjudications for submitted services.
    """

    __tablename__ = "ClaimResponseItemDetail"

    adjudication = Column(ClaimResponseItemDetailAdjudication)
    """ Detail adjudication.
        List of `ClaimResponseItemDetailAdjudication` items (represented as `dict` in JSON). """

    sequenceLinkId = Column(Integer)
    """ Service instance.
        Type `int`. """

    subDetail = Column(ClaimResponseItemDetailSubDetail)
    """ Subdetail line items.
        List of `ClaimResponseItemDetailSubDetail` items (represented as `dict` in JSON). """

    def __init__(self, adjudication, sequenceLinkId, subDetail,):
        """ Initialize all valid properties.
        """
        self.adjudication = adjudication
        self.sequenceLinkId = sequenceLinkId
        self.subDetail = subDetail

    def __repr__(self):
        return '<ClaimResponseItemDetail %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ClaimResponseItemDetailAdjudication(backboneelement.BackboneElement):
    """ Detail adjudication.

    The adjudications results.
    """

    __tablename__ = "ClaimResponseItemDetailAdjudication"

    amount = Column(Quantity)
    """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    code = Column(Coding)
    """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """

    value = Column(float)
    """ Non-monetary value.
        Type `float`. """

    def __init__(self, amount, code, value,):
        """ Initialize all valid properties.
        """
        self.amount = amount
        self.code = code
        self.value = value

    def __repr__(self):
        return '<ClaimResponseItemDetailAdjudication %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ClaimResponseItemDetailSubDetail(backboneelement.BackboneElement):
    """ Subdetail line items.

    The third tier service adjudications for submitted services.
    """

    __tablename__ = "ClaimResponseItemDetailSubDetail"

    adjudication = Column(ClaimResponseItemDetailSubDetailAdjudication)
    """ Subdetail adjudication.
        List of `ClaimResponseItemDetailSubDetailAdjudication` items (represented as `dict` in JSON). """

    sequenceLinkId = Column(Integer)
    """ Service instance.
        Type `int`. """

    def __init__(self, adjudication, sequenceLinkId,):
        """ Initialize all valid properties.
        """
        self.adjudication = adjudication
        self.sequenceLinkId = sequenceLinkId

    def __repr__(self):
        return '<ClaimResponseItemDetailSubDetail %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ClaimResponseItemDetailSubDetailAdjudication(backboneelement.BackboneElement):
    """ Subdetail adjudication.

    The adjudications results.
    """

    __tablename__ = "ClaimResponseItemDetailSubDetailAdjudication"

    amount = Column(Quantity)
    """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    code = Column(Coding)
    """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """

    value = Column(float)
    """ Non-monetary value.
        Type `float`. """

    def __init__(self, amount, code, value,):
        """ Initialize all valid properties.
        """
        self.amount = amount
        self.code = code
        self.value = value

    def __repr__(self):
        return '<ClaimResponseItemDetailSubDetailAdjudication %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ClaimResponseNote(backboneelement.BackboneElement):
    """ Processing notes.

    Note text.
    """

    __tablename__ = "ClaimResponseNote"

    number = Column(Integer)
    """ Note Number for this note.
        Type `int`. """

    text = Column(primitives.StringField)
    """ Note explanatory text.
        Type `str`. """

    type = Column(Coding)
    """ display | print | printoper.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, number, text, type,):
        """ Initialize all valid properties.
        """
        self.number = number
        self.text = text
        self.type = type

    def __repr__(self):
        return '<ClaimResponseNote %r>' % 'self.property'  # replace self.property


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity