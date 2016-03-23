#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Contract)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class ContractActor(backboneelement.BackboneElement):
    """ Contract Actor.

    List of Contract actors.
    """

    __tablename__ = "ContractActor"

    # todo entity = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    entity = Column(primitives.StringField)
    """ Contract Actor Type.
        Type `FHIRReference` referencing `Contract, Device,
        Group, Location, Organization, Patient, Practitioner,
        RelatedPerson, Substance` (represented as `dict` in JSON). """

    role = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Contract  Actor Role.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, entity, role,):
        """ Initialize all valid properties.
        """
        self.entity = entity
        self.role = role

    def __repr__(self):
        return '<ContractActor %r>' % 'self.property'  # replace self.property


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

    contentAttachment = Column(primitives.StringField,
                               ForeignKey('Attachment.id'))
    """ Easily comprehended representation of this Contract.
        Type `Attachment` (represented as `dict` in JSON). """

    # todo contentReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    contentReference = Column(primitives.StringField)
    """ Easily comprehended representation of this Contract.
        Type `FHIRReference` referencing `Composition,
        DocumentReference, QuestionnaireResponse` (represented as `dict` in JSON). """

    def __init__(self, contentAttachment, contentReference,):
        """ Initialize all valid properties.
        """
        self.contentAttachment = contentAttachment
        self.contentReference = contentReference

    def __repr__(self):
        return '<ContractFriendly %r>' % 'self.property'  # replace self.property


class ContractLegal(backboneelement.BackboneElement):
    """ Contract Legal Language.

    List of Legal expressions or representations of this Contract.
    """

    __tablename__ = "ContractLegal"

    contentAttachment = Column(primitives.StringField,
                               ForeignKey('Attachment.id'))
    """ Contract Legal Text.
        Type `Attachment` (represented as `dict` in JSON). """

    # todo contentReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    contentReference = Column(primitives.StringField)
    """ Contract Legal Text.
        Type `FHIRReference` referencing `Composition, DocumentReference,
        QuestionnaireResponse` (represented as `dict` in JSON). """

    def __init__(self, contentAttachment, contentReference,):
        """ Initialize all valid properties.
        """
        self.contentAttachment = contentAttachment
        self.contentReference = contentReference

    def __repr__(self):
        return '<ContractLegal %r>' % 'self.property'  # replace self.property


class ContractRule(backboneelement.BackboneElement):
    """ Computable Contract Language.

    List of Computable Policy Rule Language Representations of this Contract.
    """

    __tablename__ = "ContractRule"

    contentAttachment = Column(primitives.StringField,
                               ForeignKey('Attachment.id'))
    """ Computable Contract Rules.
        Type `Attachment` (represented as `dict` in JSON). """

    # todo contentReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    contentReference = Column(primitives.StringField)
    """ Computable Contract Rules.
        Type `FHIRReference` referencing `DocumentReference` (represented as `dict` in JSON). """

    def __init__(self, contentAttachment, contentReference,):
        """ Initialize all valid properties.
        """
        self.contentAttachment = contentAttachment
        self.contentReference = contentReference

    def __repr__(self):
        return '<ContractRule %r>' % 'self.property'  # replace self.property


class ContractSigner(backboneelement.BackboneElement):
    """ Contract Signer.

    Party signing this Contract.
    """

    __tablename__ = "ContractSigner"

    # todo party = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    party = Column(primitives.StringField)
    """ Contract Signatory Party.
        Type `FHIRReference` referencing `Organization, Patient,
        Practitioner, RelatedPerson` (represented as `dict` in JSON). """

    signature = Column(primitives.StringField)
    """ Contract Documentation Signature.
        Type `str`. """

    type = Column(primitives.StringField,
                  ForeignKey('Coding.id'))
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


class ContractTermActor(backboneelement.BackboneElement):
    """ Contract Term Actor List.

    List of actors participating in this Contract Provision.
    """

    __tablename__ = "ContractTermActor"

    # todo entity = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    entity = Column(primitives.StringField)
    """ Contract Term Actor.
        Type `FHIRReference` referencing `Contract, Device, Group,
        Location, Organization, Patient, Practitioner, RelatedPerson,
        Substance` (represented as `dict` in JSON). """

    role = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Contract Term Actor Role.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, entity, role,):
        """ Initialize all valid properties.
        """
        self.entity = entity
        self.role = role

    def __repr__(self):
        return '<ContractTermActor %r>' % 'self.property'  # replace self.property


class ContractTermValuedItem(backboneelement.BackboneElement):
    """ Contract Term Valued Item.

    Contract Provision Valued Item List.
    """

    __tablename__ = "ContractTermValuedItem"

    effectiveTime = Column(primitives.DateTimeField)
    """ Contract Term Valued Item Effective Tiem.
        Type `FHIRDate` (represented as `str` in JSON). """

    entityCodeableConcept = Column(primitives.StringField,
                                   ForeignKey('CodeableConcept.id'))
    """ Contract Term Valued Item Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    # todo entityReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    entityReference = Column(primitives.StringField)
    """ Contract Term Valued Item Type.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    factor = Column(primitives.DecimalField)
    """ Contract Term Valued Item Price Scaling Factor.
        Type `float`. """

    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Contract Term Valued Item Identifier.
        Type `Identifier` (represented as `dict` in JSON). """

    net = Column(primitives.StringField,
                 ForeignKey('Quantity.id'))
    """ Total Contract Term Valued Item Value.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    points = Column(primitives.DecimalField)
    """ Contract Term Valued Item Difficulty Scaling Factor.
        Type `float`. """

    quantity = Column(primitives.StringField,
                      ForeignKey('Quantity.id'))
    """ Contract Term Valued Item Count.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    unitPrice = Column(primitives.StringField,
                       ForeignKey('Quantity.id'))
    """ Contract Term Valued Item fee, charge, or cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    def __init__(self, effectiveTime, entityCodeableConcept, entityReference,
                 factor, identifier, net, points, quantity, unitPrice,):
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


class ContractValuedItem(backboneelement.BackboneElement):
    """ Contract Valued Item.

    Contract Valued Item List.
    """

    __tablename__ = "ContractValuedItem"

    effectiveTime = Column(primitives.DateTimeField)
    """ Contract Valued Item Effective Tiem.
        Type `FHIRDate` (represented as `str` in JSON). """

    entityCodeableConcept = Column(primitives.StringField,
                                   ForeignKey('CodeableConcept.id'))
    """ Contract Valued Item Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    # todo entityReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    entityReference = Column(primitives.StringField)
    """ Contract Valued Item Type.
        Type `FHIRReference` referencing `Resource`
        (represented as `dict` in JSON). """

    factor = Column(primitives.DecimalField)
    """ Contract Valued Item Price Scaling Factor.
        Type `float`. """

    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Contract Valued Item Identifier.
        Type `Identifier` (represented as `dict` in JSON). """

    net = Column(primitives.StringField,
                 ForeignKey('Money.id'))
    """ Total Contract Valued Item Value.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    points = Column(primitives.DecimalField)
    """ Contract Valued Item Difficulty Scaling Factor.
        Type `float`. """

    quantity = Column(primitives.StringField,
                      ForeignKey('SimpleQuantity.id'))
    """ Count of Contract Valued Items.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    unitPrice = Column(primitives.StringField,
                       ForeignKey('Money.id'))
    """ Contract Valued Item fee, charge, or cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    def __init__(self, effectiveTime, entityCodeableConcept,
                 entityReference, factor, identifier, net, points,
                 quantity, unitPrice):
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


class ContractTerm(backboneelement.BackboneElement):
    """ Contract Term List.

    One or more Contract Provisions, which may be related and conveyed as a
    group, and may contain nested groups.
    """

    __tablename__ = "ContractTerm"

    action = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ Contract Term Action.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    actionReason = Column(primitives.StringField,
                          ForeignKey('CodeableConcept.id'))
    """ Contract Term Action Reason.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    actor = Column(primitives.StringField,
                   ForeignKey('ContractTermActor.id'))
    """ Contract Term Actor List.
        List of `ContractTermActor` items (represented as `dict` in JSON). """

    applies = Column(primitives.StringField,
                     ForeignKey('Period.id'))
    """ Contract Term Effective Time.
        Type `Period` (represented as `dict` in JSON). """

    group = Column(primitives.StringField,
                   ForeignKey('ContractTerm.id'))
    """ Nested Contract Term Group.
        List of `ContractTerm` items (represented as `dict` in JSON). """

    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Contract Term identifier.
        Type `Identifier` (represented as `dict` in JSON). """

    issued = Column(primitives.DateTimeField)
    """ Contract Term Issue Date Time.
        Type `FHIRDate` (represented as `str` in JSON). """

    subType = Column(primitives.StringField,
                     ForeignKey('CodeableConcept.id'))
    """ Contract Term Subtype.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Subject of this Contract Term.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    text = Column(primitives.StringField)
    """ Human readable Contract term text.
        Type `str`. """

    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Contract Term Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    valuedItem = Column(primitives.StringField,
                        ForeignKey('ContractTermValuedItem.id'))
    """ Contract Term Valued Item.
        List of `ContractTermValuedItem` items (represented as `dict` in JSON). """

    def __init__(self, action, actionReason, actor, applies, group,
                 identifier, issued, subType, subject, text, type,
                 valuedItem,):
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


class Contract(domainresource.DomainResource):
    """ Contract.

    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    __tablename__ = "Contract"
    
    action = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ Contract Action.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    actionReason = Column(primitives.StringField,
                          ForeignKey('CodeableConcept.id'))
    """ Contract Action Reason.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    actor = Column(primitives.StringField,
                   ForeignKey('ContractActor.id'))
    """ Contract Actor.
        List of `ContractActor` items (represented as `dict` in JSON). """
    
    applies = Column(primitives.StringField,
                     ForeignKey('Period.id'))
    """ Effective time.
        Type `Period` (represented as `dict` in JSON). """
    
    # todo authority = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    authority = Column(primitives.StringField)
    """ Authority under which this Contract has standing.
        List of `FHIRReference` items referencing `Organization`
        (represented as `dict` in JSON). """
    
    bindingAttachment = Column(primitives.StringField,
                               ForeignKey('Attachment.id'))
    """ Binding Contract.
        Type `Attachment` (represented as `dict` in JSON). """
    
    # todo bindingReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    bindingReference = Column(primitives.StringField)
    """ Binding Contract.
        Type `FHIRReference` referencing `Composition, DocumentReference,
        QuestionnaireResponse` (represented as `dict` in JSON). """
    
    # todo domain = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    domain = Column(primitives.StringField)
    """ Domain in which this Contract applies.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """
    
    friendly = Column(primitives.StringField,
                      ForeignKey('ContractFriendly.id'))
    """ Contract Friendly Language.
        List of `ContractFriendly` items (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Contract identifier.
        Type `Identifier` (represented as `dict` in JSON). """
    
    issued = Column(primitives.DateTimeField)
    """ When this Contract was issued.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    legal = Column(primitives.StringField,
                   ForeignKey('ContractLegal.id'))
    """ Contract Legal Language.
        List of `ContractLegal` items (represented as `dict` in JSON). """
    
    rule = Column(primitives.StringField,
                  ForeignKey('ContractRule.id'))
    """ Computable Contract Language.
        List of `ContractRule` items (represented as `dict` in JSON). """
    
    signer = Column(primitives.StringField,
                    ForeignKey('ContractSigner.id'))
    """ Contract Signer.
        List of `ContractSigner` items (represented as `dict` in JSON). """
    
    subType = Column(primitives.StringField,
                     ForeignKey('CodeableConcept.id'))
    """ Contract Subtype.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Subject of this Contract.
        List of `FHIRReference` items referencing `Resource`
        (represented as `dict` in JSON). """
    
    term = Column(primitives.StringField,
                  ForeignKey('ContractTerm.id'))
    """ Contract Term List.
        List of `ContractTerm` items (represented as `dict` in JSON). """
    
    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Contract Tyoe.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    valuedItem = Column(primitives.StringField,
                        ForeignKey('ContractValuedItem.id'))
    """ Contract Valued Item.
        List of `ContractValuedItem` items (represented as `dict` in JSON). """

    def __init__(self, action, actionReason, actor, applies, authority,
                 bindingAttachment, bindingReference, domain, friendly,
                 identifier, issued, legal, rule, signer, subType,
                 subject, term, type, valuedItem,):
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
