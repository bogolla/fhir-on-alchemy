#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Contract)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer
from sil_fhir_server.data_types import primitives
from . import domainresource

class Contract(domainresource.DomainResource):
    """ Contract.

    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    __tablename__ = "Contract"

    action = Column(CodeableConcept)
    """ Contract Action.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    actionReason = Column(CodeableConcept)
    """ Contract Action Reason.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    actor = Column(ContractActor)
    """ Contract Actor.
        List of `ContractActor` items (represented as `dict` in JSON). """

    applies = Column(Period)
    """ Effective time.
        Type `Period` (represented as `dict` in JSON). """

    authority = Column(FHIRReference)
    """ Authority under which this Contract has standing.
        List of `FHIRReference` items referencing `Organization` (represented as `dict` in JSON). """

    bindingAttachment = Column(Attachment)
    """ Binding Contract.
        Type `Attachment` (represented as `dict` in JSON). """

    bindingReference = Column(FHIRReference)
    """ Binding Contract.
        Type `FHIRReference` referencing `Composition, DocumentReference, QuestionnaireResponse` (represented as `dict` in JSON). """

    domain = Column(FHIRReference)
    """ Domain in which this Contract applies.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """

    friendly = Column(ContractFriendly)
    """ Contract Friendly Language.
        List of `ContractFriendly` items (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Contract identifier.
        Type `Identifier` (represented as `dict` in JSON). """

    issued = Column(FHIRDate)
    """ When this Contract was issued.
        Type `FHIRDate` (represented as `str` in JSON). """

    legal = Column(ContractLegal)
    """ Contract Legal Language.
        List of `ContractLegal` items (represented as `dict` in JSON). """

    rule = Column(ContractRule)
    """ Computable Contract Language.
        List of `ContractRule` items (represented as `dict` in JSON). """

    signer = Column(ContractSigner)
    """ Contract Signer.
        List of `ContractSigner` items (represented as `dict` in JSON). """

    subType = Column(CodeableConcept)
    """ Contract Subtype.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    subject = Column(FHIRReference)
    """ Subject of this Contract.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """

    term = Column(ContractTerm)
    """ Contract Term List.
        List of `ContractTerm` items (represented as `dict` in JSON). """

    type = Column(CodeableConcept)
    """ Contract Tyoe.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    valuedItem = Column(ContractValuedItem)
    """ Contract Valued Item.
        List of `ContractValuedItem` items (represented as `dict` in JSON). """

    def __init__(self, action, actionReason, actor, applies, authority, bindingAttachment, bindingReference, domain, friendly, identifier, issued, legal, rule, signer, subType, subject, term, type, valuedItem,):
        """ Initialize all valid properties.
        """
        self.action = action
        self.actionReason = actionReason
        self.actor = actor
        self.applies = applies
        self.authority = authority
        self.bindingAttachment = bindingAttachment
        self.bindingReference = bindingReference
        self.domain = domain
        self.friendly = friendly
        self.identifier = identifier
        self.issued = issued
        self.legal = legal
        self.rule = rule
        self.signer = signer
        self.subType = subType
        self.subject = subject
        self.term = term
        self.type = type
        self.valuedItem = valuedItem

    def __repr__(self):
        return '<Contract %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class ContractActor(backboneelement.BackboneElement):
    """ Contract Actor.

    List of Contract actors.
    """

    __tablename__ = "ContractActor"

    entity = Column(FHIRReference)
    """ Contract Actor Type.
        Type `FHIRReference` referencing `Contract, Device, Group, Location, Organization, Patient, Practitioner, RelatedPerson, Substance` (represented as `dict` in JSON). """

    role = Column(CodeableConcept)
    """ Contract  Actor Role.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, entity, role,):
        """ Initialize all valid properties.
        """
        self.entity = entity
        self.role = role

    def __repr__(self):
        return '<ContractActor %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ContractFriendly(backboneelement.BackboneElement):
    """ Contract Friendly Language.

    The "patient friendly language" versionof the Contract in whole or in
    parts. "Patient friendly language" means the representation of the Contract
    and Contract Provisions in a manner that is readily accessible and
    understandable by a layperson in accordance with best practices for
    communication styles that ensure that those agreeing to or signing the
    Contract understand the roles, actions, obligations, responsibilities, and
    implication of the agreement.
    """

    __tablename__ = "ContractFriendly"

    contentAttachment = Column(Attachment)
    """ Easily comprehended representation of this Contract.
        Type `Attachment` (represented as `dict` in JSON). """

    contentReference = Column(FHIRReference)
    """ Easily comprehended representation of this Contract.
        Type `FHIRReference` referencing `Composition, DocumentReference, QuestionnaireResponse` (represented as `dict` in JSON). """

    def __init__(self, contentAttachment, contentReference,):
        """ Initialize all valid properties.
        """
        self.contentAttachment = contentAttachment
        self.contentReference = contentReference

    def __repr__(self):
        return '<ContractFriendly %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ContractLegal(backboneelement.BackboneElement):
    """ Contract Legal Language.

    List of Legal expressions or representations of this Contract.
    """

    __tablename__ = "ContractLegal"

    contentAttachment = Column(Attachment)
    """ Contract Legal Text.
        Type `Attachment` (represented as `dict` in JSON). """

    contentReference = Column(FHIRReference)
    """ Contract Legal Text.
        Type `FHIRReference` referencing `Composition, DocumentReference, QuestionnaireResponse` (represented as `dict` in JSON). """

    def __init__(self, contentAttachment, contentReference,):
        """ Initialize all valid properties.
        """
        self.contentAttachment = contentAttachment
        self.contentReference = contentReference

    def __repr__(self):
        return '<ContractLegal %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ContractRule(backboneelement.BackboneElement):
    """ Computable Contract Language.

    List of Computable Policy Rule Language Representations of this Contract.
    """

    __tablename__ = "ContractRule"

    contentAttachment = Column(Attachment)
    """ Computable Contract Rules.
        Type `Attachment` (represented as `dict` in JSON). """

    contentReference = Column(FHIRReference)
    """ Computable Contract Rules.
        Type `FHIRReference` referencing `DocumentReference` (represented as `dict` in JSON). """

    def __init__(self, contentAttachment, contentReference,):
        """ Initialize all valid properties.
        """
        self.contentAttachment = contentAttachment
        self.contentReference = contentReference

    def __repr__(self):
        return '<ContractRule %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ContractSigner(backboneelement.BackboneElement):
    """ Contract Signer.

    Party signing this Contract.
    """

    __tablename__ = "ContractSigner"

    party = Column(FHIRReference)
    """ Contract Signatory Party.
        Type `FHIRReference` referencing `Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """

    signature = Column(primitives.StringField)
    """ Contract Documentation Signature.
        Type `str`. """

    type = Column(Coding)
    """ Contract Signer Type.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, party, signature, type,):
        """ Initialize all valid properties.
        """
        self.party = party
        self.signature = signature
        self.type = type

    def __repr__(self):
        return '<ContractSigner %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ContractTerm(backboneelement.BackboneElement):
    """ Contract Term List.

    One or more Contract Provisions, which may be related and conveyed as a
    group, and may contain nested groups.
    """

    __tablename__ = "ContractTerm"

    action = Column(CodeableConcept)
    """ Contract Term Action.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    actionReason = Column(CodeableConcept)
    """ Contract Term Action Reason.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    actor = Column(ContractTermActor)
    """ Contract Term Actor List.
        List of `ContractTermActor` items (represented as `dict` in JSON). """

    applies = Column(Period)
    """ Contract Term Effective Time.
        Type `Period` (represented as `dict` in JSON). """

    group = Column(ContractTerm)
    """ Nested Contract Term Group.
        List of `ContractTerm` items (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Contract Term identifier.
        Type `Identifier` (represented as `dict` in JSON). """

    issued = Column(FHIRDate)
    """ Contract Term Issue Date Time.
        Type `FHIRDate` (represented as `str` in JSON). """

    subType = Column(CodeableConcept)
    """ Contract Term Subtype.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    subject = Column(FHIRReference)
    """ Subject of this Contract Term.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    text = Column(primitives.StringField)
    """ Human readable Contract term text.
        Type `str`. """

    type = Column(CodeableConcept)
    """ Contract Term Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    valuedItem = Column(ContractTermValuedItem)
    """ Contract Term Valued Item.
        List of `ContractTermValuedItem` items (represented as `dict` in JSON). """

    def __init__(self, action, actionReason, actor, applies, group, identifier, issued, subType, subject, text, type, valuedItem,):
        """ Initialize all valid properties.
        """
        self.action = action
        self.actionReason = actionReason
        self.actor = actor
        self.applies = applies
        self.group = group
        self.identifier = identifier
        self.issued = issued
        self.subType = subType
        self.subject = subject
        self.text = text
        self.type = type
        self.valuedItem = valuedItem

    def __repr__(self):
        return '<ContractTerm %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ContractTermActor(backboneelement.BackboneElement):
    """ Contract Term Actor List.

    List of actors participating in this Contract Provision.
    """

    __tablename__ = "ContractTermActor"

    entity = Column(FHIRReference)
    """ Contract Term Actor.
        Type `FHIRReference` referencing `Contract, Device, Group, Location, Organization, Patient, Practitioner, RelatedPerson, Substance` (represented as `dict` in JSON). """

    role = Column(CodeableConcept)
    """ Contract Term Actor Role.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, entity, role,):
        """ Initialize all valid properties.
        """
        self.entity = entity
        self.role = role

    def __repr__(self):
        return '<ContractTermActor %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ContractTermValuedItem(backboneelement.BackboneElement):
    """ Contract Term Valued Item.

    Contract Provision Valued Item List.
    """

    __tablename__ = "ContractTermValuedItem"

    effectiveTime = Column(FHIRDate)
    """ Contract Term Valued Item Effective Tiem.
        Type `FHIRDate` (represented as `str` in JSON). """

    entityCodeableConcept = Column(CodeableConcept)
    """ Contract Term Valued Item Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    entityReference = Column(FHIRReference)
    """ Contract Term Valued Item Type.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    factor = Column(float)
    """ Contract Term Valued Item Price Scaling Factor.
        Type `float`. """

    identifier = Column(Identifier)
    """ Contract Term Valued Item Identifier.
        Type `Identifier` (represented as `dict` in JSON). """

    net = Column(Quantity)
    """ Total Contract Term Valued Item Value.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    points = Column(float)
    """ Contract Term Valued Item Difficulty Scaling Factor.
        Type `float`. """

    quantity = Column(Quantity)
    """ Contract Term Valued Item Count.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    unitPrice = Column(Quantity)
    """ Contract Term Valued Item fee, charge, or cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    def __init__(self, effectiveTime, entityCodeableConcept, entityReference, factor, identifier, net, points, quantity, unitPrice,):
        """ Initialize all valid properties.
        """
        self.effectiveTime = effectiveTime
        self.entityCodeableConcept = entityCodeableConcept
        self.entityReference = entityReference
        self.factor = factor
        self.identifier = identifier
        self.net = net
        self.points = points
        self.quantity = quantity
        self.unitPrice = unitPrice

    def __repr__(self):
        return '<ContractTermValuedItem %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ContractValuedItem(backboneelement.BackboneElement):
    """ Contract Valued Item.

    Contract Valued Item List.
    """

    __tablename__ = "ContractValuedItem"

    effectiveTime = Column(FHIRDate)
    """ Contract Valued Item Effective Tiem.
        Type `FHIRDate` (represented as `str` in JSON). """

    entityCodeableConcept = Column(CodeableConcept)
    """ Contract Valued Item Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    entityReference = Column(FHIRReference)
    """ Contract Valued Item Type.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    factor = Column(float)
    """ Contract Valued Item Price Scaling Factor.
        Type `float`. """

    identifier = Column(Identifier)
    """ Contract Valued Item Identifier.
        Type `Identifier` (represented as `dict` in JSON). """

    net = Column(Quantity)
    """ Total Contract Valued Item Value.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    points = Column(float)
    """ Contract Valued Item Difficulty Scaling Factor.
        Type `float`. """

    quantity = Column(Quantity)
    """ Count of Contract Valued Items.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    unitPrice = Column(Quantity)
    """ Contract Valued Item fee, charge, or cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    def __init__(self, effectiveTime, entityCodeableConcept, entityReference, factor, identifier, net, points, quantity, unitPrice,):
        """ Initialize all valid properties.
        """
        self.effectiveTime = effectiveTime
        self.entityCodeableConcept = entityCodeableConcept
        self.entityReference = entityReference
        self.factor = factor
        self.identifier = identifier
        self.net = net
        self.points = points
        self.quantity = quantity
        self.unitPrice = unitPrice

    def __repr__(self):
        return '<ContractValuedItem %r>' % 'self.property'  # replace self.property


from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity