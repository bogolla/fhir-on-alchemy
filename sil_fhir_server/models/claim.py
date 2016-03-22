#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Claim)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer
from sil_fhir_server.data_types import primitives
from . import domainresource

class Claim(domainresource.DomainResource):
    """ Claim, Pre-determination or Pre-authorization.

    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    __tablename__ = "Claim"

    accident = Column(FHIRDate)
    """ Accident Date.
        Type `FHIRDate` (represented as `str` in JSON). """

    accidentType = Column(Coding)
    """ Accident Type.
        Type `Coding` (represented as `dict` in JSON). """

    additionalMaterials = Column(Coding)
    """ Additional materials, documents, etc..
        List of `Coding` items (represented as `dict` in JSON). """

    condition = Column(Coding)
    """ List of presenting Conditions.
        List of `Coding` items (represented as `dict` in JSON). """

    coverage = Column(ClaimCoverage)
    """ Insurance or medical plan.
        List of `ClaimCoverage` items (represented as `dict` in JSON). """

    created = Column(FHIRDate)
    """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

    diagnosis = Column(ClaimDiagnosis)
    """ Diagnosis.
        List of `ClaimDiagnosis` items (represented as `dict` in JSON). """

    enterer = Column(FHIRReference)
    """ Author.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    exception = Column(Coding)
    """ Eligibility exceptions.
        List of `Coding` items (represented as `dict` in JSON). """

    facility = Column(FHIRReference)
    """ Servicing Facility.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """

    fundsReserve = Column(Coding)
    """ Funds requested to be reserved.
        Type `Coding` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Claim number.
        List of `Identifier` items (represented as `dict` in JSON). """

    interventionException = Column(Coding)
    """ Intervention and exception code (Pharma).
        List of `Coding` items (represented as `dict` in JSON). """

    item = Column(ClaimItem)
    """ Goods and Services.
        List of `ClaimItem` items (represented as `dict` in JSON). """

    missingTeeth = Column(ClaimMissingTeeth)
    """ Only if type = oral.
        List of `ClaimMissingTeeth` items (represented as `dict` in JSON). """

    organization = Column(FHIRReference)
    """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    originalPrescription = Column(FHIRReference)
    """ Original Prescription.
        Type `FHIRReference` referencing `MedicationOrder` (represented as `dict` in JSON). """

    originalRuleset = Column(Coding)
    """ Original specification followed.
        Type `Coding` (represented as `dict` in JSON). """

    patient = Column(FHIRReference)
    """ The subject of the Products and Services.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    payee = Column(ClaimPayee)
    """ Payee.
        Type `ClaimPayee` (represented as `dict` in JSON). """

    prescription = Column(FHIRReference)
    """ Prescription.
        Type `FHIRReference` referencing `MedicationOrder, VisionPrescription` (represented as `dict` in JSON). """

    priority = Column(Coding)
    """ Desired processing priority.
        Type `Coding` (represented as `dict` in JSON). """

    provider = Column(FHIRReference)
    """ Responsible provider.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    referral = Column(FHIRReference)
    """ Treatment Referral.
        Type `FHIRReference` referencing `ReferralRequest` (represented as `dict` in JSON). """

    ruleset = Column(Coding)
    """ Current specification followed.
        Type `Coding` (represented as `dict` in JSON). """

    school = Column(primitives.StringField)
    """ Name of School.
        Type `str`. """

    target = Column(FHIRReference)
    """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    type = Column(primitives.StringField)
    """ institutional | oral | pharmacy | professional | vision.
        Type `str`. """

    use = Column(primitives.StringField)
    """ complete | proposed | exploratory | other.
        Type `str`. """

    def __init__(self, accident, accidentType, additionalMaterials, condition, coverage, created, diagnosis, enterer, exception, facility, fundsReserve, identifier, interventionException, item, missingTeeth, organization, originalPrescription, originalRuleset, patient, payee, prescription, priority, provider, referral, ruleset, school, target, type, use,):
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


from sqlalchemy import Column, Integer, String
from . import backboneelement

class ClaimCoverage(backboneelement.BackboneElement):
    """ Insurance or medical plan.

    Financial instrument by which payment information for health care.
    """

    __tablename__ = "ClaimCoverage"

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
    """ The focal Coverage.
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
        return '<ClaimCoverage %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ClaimDiagnosis(backboneelement.BackboneElement):
    """ Diagnosis.

    Ordered list of patient diagnosis for which care is sought.
    """

    __tablename__ = "ClaimDiagnosis"

    diagnosis = Column(Coding)
    """ Patient's list of diagnosis.
        Type `Coding` (represented as `dict` in JSON). """

    sequence = Column(Integer)
    """ Sequence of diagnosis.
        Type `int`. """

    def __init__(self, diagnosis, sequence,):
        """ Initialize all valid properties.
        """
        self.diagnosis = diagnosis
        self.sequence = sequence

    def __repr__(self):
        return '<ClaimDiagnosis %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ClaimItem(backboneelement.BackboneElement):
    """ Goods and Services.

    First tier of goods and services.
    """

    __tablename__ = "ClaimItem"

    bodySite = Column(Coding)
    """ Service Location.
        Type `Coding` (represented as `dict` in JSON). """

    detail = Column(ClaimItemDetail)
    """ Additional items.
        List of `ClaimItemDetail` items (represented as `dict` in JSON). """

    diagnosisLinkId = Column(Integer)
    """ Diagnosis Link.
        List of `int` items. """

    factor = Column(float)
    """ Price scaling factor.
        Type `float`. """

    modifier = Column(Coding)
    """ Service/Product billing modifiers.
        List of `Coding` items (represented as `dict` in JSON). """

    net = Column(Quantity)
    """ Total item cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    points = Column(float)
    """ Difficulty scaling factor.
        Type `float`. """

    prosthesis = Column(ClaimItemProsthesis)
    """ Prosthetic details.
        Type `ClaimItemProsthesis` (represented as `dict` in JSON). """

    provider = Column(FHIRReference)
    """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    quantity = Column(Quantity)
    """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    sequence = Column(Integer)
    """ Service instance.
        Type `int`. """

    service = Column(Coding)
    """ Item Code.
        Type `Coding` (represented as `dict` in JSON). """

    serviceDate = Column(FHIRDate)
    """ Date of Service.
        Type `FHIRDate` (represented as `str` in JSON). """

    subSite = Column(Coding)
    """ Service Sub-location.
        List of `Coding` items (represented as `dict` in JSON). """

    type = Column(Coding)
    """ Group or type of product or service.
        Type `Coding` (represented as `dict` in JSON). """

    udi = Column(Coding)
    """ Unique Device Identifier.
        Type `Coding` (represented as `dict` in JSON). """

    unitPrice = Column(Quantity)
    """ Fee, charge or cost per point.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    def __init__(self, bodySite, detail, diagnosisLinkId, factor, modifier, net, points, prosthesis, provider, quantity, sequence, service, serviceDate, subSite, type, udi, unitPrice,):
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


from sqlalchemy import Column, Integer, String
class ClaimItemDetail(backboneelement.BackboneElement):
    """ Additional items.

    Second tier of goods and services.
    """

    __tablename__ = "ClaimItemDetail"

    factor = Column(float)
    """ Price scaling factor.
        Type `float`. """

    net = Column(Quantity)
    """ Total additional item cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    points = Column(float)
    """ Difficulty scaling factor.
        Type `float`. """

    quantity = Column(Quantity)
    """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    sequence = Column(Integer)
    """ Service instance.
        Type `int`. """

    service = Column(Coding)
    """ Additional item codes.
        Type `Coding` (represented as `dict` in JSON). """

    subDetail = Column(ClaimItemDetailSubDetail)
    """ Additional items.
        List of `ClaimItemDetailSubDetail` items (represented as `dict` in JSON). """

    type = Column(Coding)
    """ Group or type of product or service.
        Type `Coding` (represented as `dict` in JSON). """

    udi = Column(Coding)
    """ Unique Device Identifier.
        Type `Coding` (represented as `dict` in JSON). """

    unitPrice = Column(Quantity)
    """ Fee, charge or cost per point.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    def __init__(self, factor, net, points, quantity, sequence, service, subDetail, type, udi, unitPrice,):
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


from sqlalchemy import Column, Integer, String
class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    """ Additional items.

    Third tier of goods and services.
    """

    __tablename__ = "ClaimItemDetailSubDetail"

    factor = Column(float)
    """ Price scaling factor.
        Type `float`. """

    net = Column(Quantity)
    """ Net additional item cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    points = Column(float)
    """ Difficulty scaling factor.
        Type `float`. """

    quantity = Column(Quantity)
    """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    sequence = Column(Integer)
    """ Service instance.
        Type `int`. """

    service = Column(Coding)
    """ Additional item codes.
        Type `Coding` (represented as `dict` in JSON). """

    type = Column(Coding)
    """ Type of product or service.
        Type `Coding` (represented as `dict` in JSON). """

    udi = Column(Coding)
    """ Unique Device Identifier.
        Type `Coding` (represented as `dict` in JSON). """

    unitPrice = Column(Quantity)
    """ Fee, charge or cost per point.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """

    def __init__(self, factor, net, points, quantity, sequence, service, type, udi, unitPrice,):
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


from sqlalchemy import Column, Integer, String
class ClaimItemProsthesis(backboneelement.BackboneElement):
    """ Prosthetic details.

    The materials and placement date of prior fixed prosthesis.
    """

    __tablename__ = "ClaimItemProsthesis"

    initial = Column(bool)
    """ Is this the initial service.
        Type `bool`. """

    priorDate = Column(FHIRDate)
    """ Initial service Date.
        Type `FHIRDate` (represented as `str` in JSON). """

    priorMaterial = Column(Coding)
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


from sqlalchemy import Column, Integer, String
class ClaimMissingTeeth(backboneelement.BackboneElement):
    """ Only if type = oral.

    A list of teeth which would be expected but are not found due to having
    been previously  extracted or for other reasons.
    """

    __tablename__ = "ClaimMissingTeeth"

    extractionDate = Column(FHIRDate)
    """ Date of Extraction.
        Type `FHIRDate` (represented as `str` in JSON). """

    reason = Column(Coding)
    """ Reason for missing.
        Type `Coding` (represented as `dict` in JSON). """

    tooth = Column(Coding)
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


from sqlalchemy import Column, Integer, String
class ClaimPayee(backboneelement.BackboneElement):
    """ Payee.

    The party to be reimbursed for the services.
    """

    __tablename__ = "ClaimPayee"

    organization = Column(FHIRReference)
    """ Organization who is the payee.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    person = Column(FHIRReference)
    """ Other person who is the payee.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    provider = Column(FHIRReference)
    """ Provider who is the payee.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    type = Column(Coding)
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


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity