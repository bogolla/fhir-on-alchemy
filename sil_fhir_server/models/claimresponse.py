#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ClaimResponse)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class ClaimResponseAddItemAdjudication(backboneelement.BackboneElement):
    """ Added items adjudication.

    The adjudications results.
    """

    __tablename__ = "ClaimResponseAddItemAdjudication"

    amount = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    code = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """

    value = Column(primitives.DecimalField)
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


class ClaimResponseAddItemDetailAdjudication(backboneelement.BackboneElement):
    """ Added items detail adjudication.

    The adjudications results.
    """

    __tablename__ = "ClaimResponseAddItemDetailAdjudication"

    amount = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    code = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """

    value = Column(primitives.DecimalField)
    """ Non-monetary value.
        Type `float`. """

    def __init__(self, amount, code, value,):
        """ Initialize all valid properties.
        """
        self.amount = amount
        self.code = code
        self.value = value

    def __repr__(self):
        return '<ClaimResponseAddItemDetailAdjudication %r>' % 'self.property'  # replace self.propert


class ClaimResponseAddItemDetail(backboneelement.BackboneElement):
    """ Added items details.

    The second tier service adjudications for payor added services.
    """

    __tablename__ = "ClaimResponseAddItemDetail"

    adjudication = Column(primitives.StringField,
                          ForeignKey('ClaimResponseAddItemDetailAdjudication.id'))
    """ Added items detail adjudication.
        List of `ClaimResponseAddItemDetailAdjudication` items (represented as `dict` in JSON). """

    fee = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ Professional fee or Product charge.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    service = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Service or Product.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, adjudication, fee, service):
        """ Initialize all valid properties.
        """
        self.adjudication = adjudication
        self.fee = fee
        self.service = service

    def __repr__(self):
        return '<ClaimResponseAddItemDetail %r>' % 'self.property'  # replace self.property


class ClaimResponseAddItem(backboneelement.BackboneElement):
    """ Insurer added line items.

    The first tier service adjudications for payor added services.
    """

    __tablename__ = "ClaimResponseAddItem"

    adjudication = Column(primitives.StringField,
                          ForeignKey(
                              'ClaimResponseAddItemAdjudication.id'))
    """ Added items adjudication.
        List of `ClaimResponseAddItemAdjudication` items (represented as `dict` in JSON). """

    detail = Column(primitives.StringField,
                    ForeignKey('ClaimResponseAddItemDetail.id'))
    """ Added items details.
        List of `ClaimResponseAddItemDetail` items (represented as `dict` in JSON). """

    fee = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ Professional fee or Product charge.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    noteNumberLinkId = Column(primitives.IntegerField)
    """ List of note numbers which apply.
        List of `int` items. """

    sequenceLinkId = Column(primitives.IntegerField)
    """ Service instances.
        List of `int` items. """

    service = Column(primitives.StringField, ForeignKey('Coding.id'))
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


class ClaimResponseCoverage(backboneelement.BackboneElement):
    """ Insurance or medical plan.

    Financial instrument by which payment information for health care.
    """

    __tablename__ = "ClaimResponseCoverage"

    businessArrangement = Column(primitives.StringField)
    """ Business agreement.
        Type `str`. """

    # todo claimResponse = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    claimResponse = Column(primitives.StringField)
    """ Adjudication results.
        Type `FHIRReference` referencing `ClaimResponse` (represented as `dict` in JSON). """

    # todo coverage = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    coverage = Column(primitives.StringField)
    """ Insurance information.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """

    focal = Column(primitives.BooleanField)
    """ Is the focal Coverage.
        Type `bool`. """

    originalRuleset = Column(primitives.StringField,
                             ForeignKey('Coding.id'))
    """ Original version.
        Type `Coding` (represented as `dict` in JSON). """

    preAuthRef = Column(primitives.StringField)
    """ Pre-Authorization/Determination Reference.
        List of `str` items. """

    relationship = Column(primitives.StringField,
                          ForeignKey('Coding.id'))
    """ Patient relationship to subscriber.
        Type `Coding` (represented as `dict` in JSON). """

    sequence = Column(primitives.IntegerField)
    """ Service instance identifier.
        Type `int`. """

    def __init__(self, businessArrangement, claimResponse, coverage,
                 focal, originalRuleset, preAuthRef, relationship,
                 sequence,):
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


class ClaimResponseError(backboneelement.BackboneElement):
    """ Processing errors.

    Mutually exclusive with Services Provided (Item).
    """

    __tablename__ = "ClaimResponseError"

    code = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Error code detailing processing issues.
        Type `Coding` (represented as `dict` in JSON). """

    detailSequenceLinkId = Column(primitives.IntegerField)
    """ Detail sequence number.
        Type `int`. """

    sequenceLinkId = Column(primitives.IntegerField)
    """ Item sequence number.
        Type `int`. """

    subdetailSequenceLinkId = Column(primitives.IntegerField)
    """ Subdetail sequence number.
        Type `int`. """

    def __init__(self, code, detailSequenceLinkId, sequenceLinkId,
                 subdetailSequenceLinkId,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.detailSequenceLinkId = detailSequenceLinkId
        self.sequenceLinkId = sequenceLinkId
        self.subdetailSequenceLinkId = subdetailSequenceLinkId

    def __repr__(self):
        return '<ClaimResponseError %r>' % 'self.property'  # replace self.property


class ClaimResponseItemAdjudication(backboneelement.BackboneElement):
    """ Adjudication details.

    The adjudications results.
    """

    __tablename__ = "ClaimResponseItemAdjudication"

    amount = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    code = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """

    value = Column(primitives.DecimalField)
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


class ClaimResponseItemDetail(backboneelement.BackboneElement):
    """ Detail line items.

    The second tier service adjudications for submitted services.
    """

    __tablename__ = "ClaimResponseItemDetail"

    adjudication = Column(primitives.StringField,
                          ForeignKey('ClaimResponseItemDetailAdjudication.id'))
    """ Detail adjudication.
        List of `ClaimResponseItemDetailAdjudication` items (represented as `dict` in JSON). """

    sequenceLinkId = Column(primitives.IntegerField)
    """ Service instance.
        Type `int`. """

    subDetail = Column(primitives.StringField,
                       ForeignKey('ClaimResponseItemDetailSubDetail.id'))
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


class ClaimResponseItem(backboneelement.BackboneElement):
    """ Line items.

    The first tier service adjudications for submitted services.
    """

    __tablename__ = "ClaimResponseItem"

    adjudication = Column(primitives.StringField,
                          ForeignKey('ClaimResponseItemAdjudication.id'))
    """ Adjudication details.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """

    detail = Column(primitives.StringField, ForeignKey('ClaimResponseItemDetail.id'))
    """ Detail line items.
        List of `ClaimResponseItemDetail` items (represented as `dict` in JSON). """

    noteNumber = Column(primitives.IntegerField)
    """ List of note numbers which apply.
        List of `int` items. """

    sequenceLinkId = Column(primitives.IntegerField)
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


class ClaimResponseItemDetailAdjudication(backboneelement.BackboneElement):
    """ Detail adjudication.

    The adjudications results.
    """

    __tablename__ = "ClaimResponseItemDetailAdjudication"

    amount = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    code = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """

    value = Column(primitives.DecimalField)
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


class ClaimResponseItemDetailSubDetailAdjudication(backboneelement.BackboneElement):
    """ Subdetail adjudication.

    The adjudications results.
    """

    __tablename__ = "ClaimResponseItemDetailSubDetailAdjudication"

    amount = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    code = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """

    value = Column(primitives.DecimalField)
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


class ClaimResponseItemDetailSubDetail(backboneelement.BackboneElement):
    """ Subdetail line items.

    The third tier service adjudications for submitted services.
    """

    __tablename__ = "ClaimResponseItemDetailSubDetail"

    adjudication = Column(primitives.StringField,
                          ForeignKey('ClaimResponseItemDetailSubDetailAdjudication.id'))
    """ Subdetail adjudication.
        List of `ClaimResponseItemDetailSubDetailAdjudication` items
        (represented as `dict` in JSON). """

    sequenceLinkId = Column(primitives.IntegerField)
    """ Service instance.
        Type `int`. """

    def __init__(self, adjudication, sequenceLinkId,):
        """ Initialize all valid properties.
        """
        self.adjudication = adjudication
        self.sequenceLinkId = sequenceLinkId

    def __repr__(self):
        return '<ClaimResponseItemDetailSubDetail %r>' % 'self.property'  # replace self.property


class ClaimResponseNote(backboneelement.BackboneElement):
    """ Processing notes.

    Note text.
    """

    __tablename__ = "ClaimResponseNote"

    number = Column(primitives.IntegerField)
    """ Note Number for this note.
        Type `int`. """

    text = Column(primitives.StringField)
    """ Note explanatory text.
        Type `str`. """

    type = Column(primitives.StringField, ForeignKey('Coding.id'))
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


class ClaimResponse(domainresource.DomainResource):
    """ Remittance resource.

    This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    __tablename__ = "ClaimResponse"
    
    addItem = Column(primitives.StringField,
                     ForeignKey('ClaimResponseAddItem.id'))
    """ Insurer added line items.
        List of `ClaimResponseAddItem` items (represented as `dict` in JSON). """
    
    coverage = Column(primitives.StringField,
                      ForeignKey('ClaimResponseCoverage.id'))
    """ Insurance or medical plan.
        List of `ClaimResponseCoverage` items (represented as `dict` in JSON). """
    
    created = Column(primitives.DateTimeField)
    """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    disposition = Column(primitives.StringField)
    """ Disposition Message.
        Type `str`. """
    
    error = Column(primitives.StringField,
                   ForeignKey('ClaimResponseError.id'))
    """ Processing errors.
        List of `ClaimResponseError` items (represented as `dict` in JSON). """
    
    form = Column(primitives.StringField,
                  ForeignKey('Coding.id'))
    """ Printed Form Identifier.
        Type `Coding` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Response  number.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    item = Column(primitives.StringField,
                  ForeignKey('ClaimResponseItem.id'))
    """ Line items.
        List of `ClaimResponseItem` items (represented as `dict` in JSON). """
    
    note = Column(primitives.StringField,
                  ForeignKey('ClaimResponseNote.id'))
    """ Processing notes.
        List of `ClaimResponseNote` items (represented as `dict` in JSON). """
    
    # todo organization = Column(primitives.StringField,
    #                       ForeignKey('FHIRReference.id'))
    organization = Column(primitives.StringField)
    """ Insurer.
        Type `FHIRReference` referencing `Organization`
        (represented as `dict` in JSON). """
    
    originalRuleset = Column(primitives.StringField,
                             ForeignKey('Coding.id'))
    """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
    
    outcome = Column(primitives.StringField)
    """ complete | error.
        Type `str`. """
    
    payeeType = Column(primitives.StringField,
                       ForeignKey('Coding.id'))
    """ Party to be paid any benefits payable.
        Type `Coding` (represented as `dict` in JSON). """
    
    paymentAdjustment = Column(primitives.StringField,
                               ForeignKey('Quantity.id'))
    """ Payment adjustment for non-Claim issues.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
    
    paymentAdjustmentReason = Column(primitives.StringField,
                                     ForeignKey('Coding.id'))
    """ Reason for Payment adjustment.
        Type `Coding` (represented as `dict` in JSON). """
    
    paymentAmount = Column(primitives.StringField,
                           ForeignKey('Quantity.id'))
    """ Payment amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
    
    paymentDate = Column(primitives.DateTimeField)
    """ Expected data of Payment.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    paymentRef = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Payment identifier.
        Type `Identifier` (represented as `dict` in JSON). """

    # todo request = Column(primitives.StringField,
    #                  ForeignKey('FHIRReference.id'))
    request = Column(primitives.StringField)
    """ Id of resource triggering adjudication.
        Type `FHIRReference` referencing `Claim`
        (represented as `dict` in JSON). """
    
    # todo requestOrganization = Column(primitives.StringField,
    #                              ForeignKey('FHIRReference.id'))
    requestOrganization = Column(primitives.StringField)
    """ Responsible organization.
        Type `FHIRReference` referencing `Organization`
        (represented as `dict` in JSON). """
    
    # todo requestProvider = Column(primitives.StringField,
    #                               ForeignKey('FHIRReference.id'))
    requestProvider = Column(primitives.StringField)
    """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    reserved = Column(primitives.StringField,
                      ForeignKey('Coding.id'))
    """ Funds reserved status.
        Type `Coding` (represented as `dict` in JSON). """
    
    ruleset = Column(primitives.StringField,
                     ForeignKey('Coding.id'))
    """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
    
    totalBenefit = Column(primitives.StringField,
                          ForeignKey('Quantity.id'))
    """ Total benefit payable for the Claim.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
    
    totalCost = Column(primitives.StringField,
                       ForeignKey('Quantity.id'))
    """ Total Cost of service from the Claim.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
    
    unallocDeductable = Column(primitives.StringField,
                               ForeignKey('Quantity.id'))
    """ Unallocated deductible.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    def __init__(self, addItem, coverage, created, disposition,
                 error, form, identifier, item, note, organization,
                 originalRuleset, outcome, payeeType,
                 paymentAdjustment, paymentAdjustmentReason,
                 paymentAmount, paymentDate, paymentRef, request,
                 requestOrganization, requestProvider, reserved,
                 ruleset, totalBenefit, totalCost, unallocDeductable,):
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
