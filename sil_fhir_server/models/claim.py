#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Claim)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class ClaimCoverage(backboneelement.BackboneElement):
    """ Insurance or medical plan.

    Financial instrument by which payment information for health care.
    """

    __tablename__ = "ClaimCoverage"

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
    """ The focal Coverage.
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
        return '<ClaimCoverage %r>' % 'self.property'  # replace self.property


class ClaimDiagnosis(backboneelement.BackboneElement):
    """ Diagnosis.

    Ordered list of patient diagnosis for which care is sought.
    """

    __tablename__ = "ClaimDiagnosis"

    diagnosis = Column(primitives.StringField,
                       ForeignKey('Coding.id'))
    """ Patient's list of diagnosis.
        Type `Coding` (represented as `dict` in JSON). """

    sequence = Column(primitives.IntegerField)
    """ Sequence of diagnosis.
        Type `int`. """

    def __init__(self, diagnosis, sequence,):
        """ Initialize all valid properties.
        """
        self.diagnosis = diagnosis
        self.sequence = sequence

    def __repr__(self):
        return '<ClaimDiagnosis %r>' % 'self.property'  # replace self.property


class ClaimItem(backboneelement.BackboneElement):
    """ Goods and Services.

    First tier of goods and services.
    """

    __tablename__ = "ClaimItem"

    bodySite = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Service Location.
        Type `Coding` (represented as `dict` in JSON). """

    detail = Column(primitives.StringField,
                    ForeignKey('ClaimItemDetail.id'))
    """ Additional items.
        List of `ClaimItemDetail` items (represented as `dict` in JSON). """

    diagnosisLinkId = Column(primitives.IntegerField)
    """ Diagnosis Link.
        List of `int` items. """

    factor = Column(primitives.DecimalField)
    """ Price scaling factor.
        Type `float`. """

    modifier = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Service/Product billing modifiers.
        List of `Coding` items (represented as `dict` in JSON). """

    net = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ Total item cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    points = Column(primitives.DecimalField)
    """ Difficulty scaling factor.
        Type `float`. """

    prosthesis = Column(primitives.StringField,
                        ForeignKey('ClaimItemProsthesis.id'))
    """ Prosthetic details.
        Type `ClaimItemProsthesis` (represented as `dict` in JSON). """

    # todo provider = Column(primitives.StringField,
    #                   ForeignKey('FHIRReference.id'))
    provider = Column(primitives.StringField)
    """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    quantity = Column(primitives.StringField,
                      ForeignKey('Quantity.id'))
    """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    sequence = Column(primitives.IntegerField)
    """ Service instance.
        Type `int`. """

    service = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Item Code.
        Type `Coding` (represented as `dict` in JSON). """

    serviceDate = Column(primitives.DateTimeField)
    """ Date of Service.
        Type `FHIRDate` (represented as `str` in JSON). """

    subSite = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Service Sub-location.
        List of `Coding` items (represented as `dict` in JSON). """

    type = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Group or type of product or service.
        Type `Coding` (represented as `dict` in JSON). """

    udi = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Unique Device Identifier.
        Type `Coding` (represented as `dict` in JSON). """

    unitPrice = Column(primitives.StringField,
                       ForeignKey('Quantity.id'))
    """ Fee, charge or cost per point.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    def __init__(self, bodySite, detail, diagnosisLinkId, factor,
                 modifier, net, points, prosthesis, provider,
                 quantity, sequence, service, serviceDate, subSite,
                 type, udi, unitPrice,):
        """ Initialize all valid properties.
        """
        self.bodySite = bodySite
        self.detail = detail
        self.diagnosisLinkId = diagnosisLinkId
        self.factor = factor
        self.modifier = modifier
        self.net = net
        self.points = points
        self.prosthesis = prosthesis
        self.provider = provider
        self.quantity = quantity
        self.sequence = sequence
        self.service = service
        self.serviceDate = serviceDate
        self.subSite = subSite
        self.type = type
        self.udi = udi
        self.unitPrice = unitPrice

    def __repr__(self):
        return '<ClaimItem %r>' % 'self.property'  # replace self.property


class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    """ Additional items.

    Third tier of goods and services.
    """

    __tablename__ = "ClaimItemDetailSubDetail"

    factor = Column(primitives.DecimalField)
    """ Price scaling factor.
        Type `float`. """

    net = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ Net additional item cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    points = Column(primitives.DecimalField)
    """ Difficulty scaling factor.
        Type `float`. """

    quantity = Column(primitives.StringField,
                      ForeignKey('Quantity.id'))
    """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    sequence = Column(primitives.IntegerField)
    """ Service instance.
        Type `int`. """

    service = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Additional item codes.
        Type `Coding` (represented as `dict` in JSON). """

    type = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Type of product or service.
        Type `Coding` (represented as `dict` in JSON). """

    udi = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Unique Device Identifier.
        Type `Coding` (represented as `dict` in JSON). """

    unitPrice = Column(primitives.StringField,
                       ForeignKey('Quantity.id'))
    """ Fee, charge or cost per point.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    def __init__(self, factor, net, points, quantity, sequence,
                 service, type, udi, unitPrice,):
        """ Initialize all valid properties.
        """
        self.factor = factor
        self.net = net
        self.points = points
        self.quantity = quantity
        self.sequence = sequence
        self.service = service
        self.type = type
        self.udi = udi
        self.unitPrice = unitPrice

    def __repr__(self):
        return '<ClaimItemDetailSubDetail %r>' % 'self.property'  # replace self.property


class ClaimItemDetail(backboneelement.BackboneElement):
    """ Additional items.

    Second tier of goods and services.
    """

    __tablename__ = "ClaimItemDetail"

    factor = Column(primitives.DecimalField)
    """ Price scaling factor.
        Type `float`. """

    net = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ Total additional item cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    points = Column(primitives.DecimalField)
    """ Difficulty scaling factor.
        Type `float`. """

    quantity = Column(primitives.StringField,
                      ForeignKey('Quantity.id'))
    """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    sequence = Column(primitives.IntegerField)
    """ Service instance.
        Type `int`. """

    service = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Additional item codes.
        Type `Coding` (represented as `dict` in JSON). """

    subDetail = Column(primitives.StringField,
                       ForeignKey('ClaimItemDetailSubDetail.id'))
    """ Additional items.
        List of `ClaimItemDetailSubDetail` items (represented as `dict` in JSON). """

    type = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Group or type of product or service.
        Type `Coding` (represented as `dict` in JSON). """

    udi = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Unique Device Identifier.
        Type `Coding` (represented as `dict` in JSON). """

    unitPrice = Column(primitives.StringField,
                       ForeignKey('Quantity.id'))
    """ Fee, charge or cost per point.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    def __init__(self, factor, net, points, quantity, sequence,
                 service, subDetail, type, udi, unitPrice,):
        """ Initialize all valid properties.
        """
        self.factor = factor
        self.net = net
        self.points = points
        self.quantity = quantity
        self.sequence = sequence
        self.service = service
        self.subDetail = subDetail
        self.type = type
        self.udi = udi
        self.unitPrice = unitPrice

    def __repr__(self):
        return '<ClaimItemDetail %r>' % 'self.property'  # replace self.property


class ClaimItemProsthesis(backboneelement.BackboneElement):
    """ Prosthetic details.

    The materials and placement date of prior fixed prosthesis.
    """

    __tablename__ = "ClaimItemProsthesis"

    initial = Column(primitives.BooleanField)
    """ Is this the initial service.
        Type `bool`. """

    priorDate = Column(primitives.DateTimeField)
    """ Initial service Date.
        Type `FHIRDate` (represented as `str` in JSON). """

    priorMaterial = Column(primitives.StringField,
                           ForeignKey('Coding.id'))
    """ Prosthetic Material.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, initial, priorDate, priorMaterial,):
        """ Initialize all valid properties.
        """
        self.initial = initial
        self.priorDate = priorDate
        self.priorMaterial = priorMaterial

    def __repr__(self):
        return '<ClaimItemProsthesis %r>' % 'self.property'  # replace self.property


class ClaimMissingTeeth(backboneelement.BackboneElement):
    """ Only if type = oral.

    A list of teeth which would be expected but are not found due to having
    been previously  extracted or for other reasons.
    """

    __tablename__ = "ClaimMissingTeeth"

    extractionDate = Column(primitives.DateTimeField)
    """ Date of Extraction.
        Type `FHIRDate` (represented as `str` in JSON). """

    reason = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Reason for missing.
        Type `Coding` (represented as `dict` in JSON). """

    tooth = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Tooth Code.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, extractionDate, reason, tooth,):
        """ Initialize all valid properties.
        """
        self.extractionDate = extractionDate
        self.reason = reason
        self.tooth = tooth

    def __repr__(self):
        return '<ClaimMissingTeeth %r>' % 'self.property'  # replace self.property


class ClaimPayee(backboneelement.BackboneElement):
    """ Payee.

    The party to be reimbursed for the services.
    """

    __tablename__ = "ClaimPayee"

    # todo organization = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    organization = Column(primitives.StringField)
    """ Organization who is the payee.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    # todo person = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    person = Column(primitives.StringField)
    """ Other person who is the payee.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    # todo provider = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    provider = Column(primitives.StringField)
    """ Provider who is the payee.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    type = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Party to be paid any benefits payable.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, organization, person, provider, type,):
        """ Initialize all valid properties.
        """
        self.organization = organization
        self.person = person
        self.provider = provider
        self.type = type

    def __repr__(self):
        return '<ClaimPayee %r>' % 'self.property'  # replace self.property


class Claim(domainresource.DomainResource):
    """ Claim, Pre-determination or Pre-authorization.

    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    __tablename__ = "Claim"
    
    accident = Column(primitives.DateTimeField)
    """ Accident Date.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    accidentType = Column(primitives.StringField,
                          ForeignKey('Coding.id'))
    """ Accident Type.
        Type `Coding` (represented as `dict` in JSON). """
    
    additionalMaterials = Column(primitives.StringField,
                                 ForeignKey('Coding.id'))
    """ Additional materials, documents, etc..
        List of `Coding` items (represented as `dict` in JSON). """
    
    condition = Column(primitives.StringField,
                       ForeignKey('Coding.id'))
    """ List of presenting Conditions.
        List of `Coding` items (represented as `dict` in JSON). """
    
    coverage = Column(primitives.StringField,
                      ForeignKey('ClaimCoverage.id'))
    """ Insurance or medical plan.
        List of `ClaimCoverage` items (represented as `dict` in JSON). """
    
    created = Column(primitives.DateTimeField)
    """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    diagnosis = Column(primitives.StringField,
                       ForeignKey('ClaimDiagnosis.id'))
    """ Diagnosis.
        List of `ClaimDiagnosis` items (represented as `dict` in JSON). """
    
    # todo enterer = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    enterer = Column(primitives.StringField)
    """ Author.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    exception = Column(primitives.StringField,
                       ForeignKey('Coding.id'))
    """ Eligibility exceptions.
        List of `Coding` items (represented as `dict` in JSON). """
    
    # todo facility = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    facility = Column(primitives.StringField)
    """ Servicing Facility.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
    
    fundsReserve = Column(primitives.StringField,
                          ForeignKey('Coding.id'))
    """ Funds requested to be reserved.
        Type `Coding` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Claim number.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    interventionException = Column(primitives.StringField,
                                   ForeignKey('Coding.id'))
    """ Intervention and exception code (Pharma).
        List of `Coding` items (represented as `dict` in JSON). """
    
    item = Column(primitives.StringField,
                  ForeignKey('ClaimItem.id'))
    """ Goods and Services.
        List of `ClaimItem` items (represented as `dict` in JSON). """
    
    missingTeeth = Column(primitives.StringField,
                          ForeignKey('ClaimMissingTeeth.id'))
    """ Only if type = oral.
        List of `ClaimMissingTeeth` items (represented as `dict` in JSON). """
    
    # todo organization = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    organization = Column(primitives.StringField)
    """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
    
    # todo originalPrescription = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    originalPrescription = Column(primitives.StringField)
    """ Original Prescription.
        Type `FHIRReference` referencing `MedicationOrder` (represented as `dict` in JSON). """
    
    originalRuleset = Column(primitives.StringField,
                             ForeignKey('Coding.id'))
    """ Original specification followed.
        Type `Coding` (represented as `dict` in JSON). """
    
    # todo patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    patient = Column(primitives.StringField)
    """ The subject of the Products and Services.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    payee = Column(primitives.StringField,
                   ForeignKey('ClaimPayee.id'))
    """ Payee.
        Type `ClaimPayee` (represented as `dict` in JSON). """
    
    # todo prescription = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    prescription = Column(primitives.StringField)
    """ Prescription.
        Type `FHIRReference` referencing `MedicationOrder, VisionPrescription` (represented as `dict` in JSON). """
    
    priority = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Desired processing priority.
        Type `Coding` (represented as `dict` in JSON). """
    
    # todo provider = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    provider = Column(primitives.StringField)
    """ Responsible provider.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    # todo referral = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    referral = Column(primitives.StringField)
    """ Treatment Referral.
        Type `FHIRReference` referencing `ReferralRequest` (represented as `dict` in JSON). """
    
    ruleset = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Current specification followed.
        Type `Coding` (represented as `dict` in JSON). """
    
    school = Column(primitives.StringField)
    """ Name of School.
        Type `str`. """
    
    # todo target = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    target = Column(primitives.StringField)
    """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
    
    type = Column(primitives.StringField)
    """ institutional | oral | pharmacy | professional | vision.
        Type `str`. """
    
    use = Column(primitives.StringField)
    """ complete | proposed | exploratory | other.
        Type `str`. """

    def __init__(self, accident, accidentType, additionalMaterials,
                 condition, coverage, created, diagnosis, enterer,
                 exception, facility, fundsReserve, identifier,
                 interventionException, item, missingTeeth,
                 organization, originalPrescription, originalRuleset,
                 patient, payee, prescription, priority, provider,
                 referral, ruleset, school, target, type, use,):
        """ Initialize all valid properties.
        """
        self.accident = accident
        self.accidentType = accidentType
        self.additionalMaterials = additionalMaterials
        self.condition = condition
        self.coverage = coverage
        self.created = created
        self.diagnosis = diagnosis
        self.enterer = enterer
        self.exception = exception
        self.facility = facility
        self.fundsReserve = fundsReserve
        self.identifier = identifier
        self.interventionException = interventionException
        self.item = item
        self.missingTeeth = missingTeeth
        self.organization = organization
        self.originalPrescription = originalPrescription
        self.originalRuleset = originalRuleset
        self.patient = patient
        self.payee = payee
        self.prescription = prescription
        self.priority = priority
        self.provider = provider
        self.referral = referral
        self.ruleset = ruleset
        self.school = school
        self.target = target
        self.type = type
        self.use = use

    def __repr__(self):
        return '<Claim %r>' % 'self.property'  # replace self.property
