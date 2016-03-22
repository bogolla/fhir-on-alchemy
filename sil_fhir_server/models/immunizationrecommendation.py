#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class ImmunizationRecommendation(domainresource.DomainResource):
    """ Guidance or advice relating to an immunization.

    A patient's point-in-time immunization and recommendation (i.e. forecasting
    a patient's immunization eligibility according to a published schedule)
    with optional supporting justification.
    """

    __tablename__ = "ImmunizationRecommendation"

    identifier = Column(Identifier)
    """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    patient = Column(FHIRReference)
    """ Who this profile is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    recommendation = Column(ImmunizationRecommendationRecommendation)
    """ Vaccine administration recommendations.
        List of `ImmunizationRecommendationRecommendation` items (represented as `dict` in JSON). """

    def __init__(self, identifier, patient, recommendation,):
        """ Initialize all valid properties.
        """
        self.identifier = identifier
        self.patient = patient
        self.recommendation = recommendation

    def __repr__(self):
        return '<ImmunizationRecommendation %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    """ Vaccine administration recommendations.
    """

    __tablename__ = "ImmunizationRecommendationRecommendation"

    date = Column(FHIRDate)
    """ Date recommendation created.
        Type `FHIRDate` (represented as `str` in JSON). """

    dateCriterion = Column(ImmunizationRecommendationRecommendationDateCriterion)
    """ Dates governing proposed immunization.
        List of `ImmunizationRecommendationRecommendationDateCriterion` items (represented as `dict` in JSON). """

    doseNumber = Column(Integer)
    """ Recommended dose number.
        Type `int`. """

    forecastStatus = Column(CodeableConcept)
    """ Vaccine administration status.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    protocol = Column(ImmunizationRecommendationRecommendationProtocol)
    """ Protocol used by recommendation.
        Type `ImmunizationRecommendationRecommendationProtocol` (represented as `dict` in JSON). """

    supportingImmunization = Column(FHIRReference)
    """ Past immunizations supporting recommendation.
        List of `FHIRReference` items referencing `Immunization` (represented as `dict` in JSON). """

    supportingPatientInformation = Column(FHIRReference)
    """ Patient observations supporting recommendation.
        List of `FHIRReference` items referencing `Observation, AllergyIntolerance` (represented as `dict` in JSON). """

    vaccineCode = Column(CodeableConcept)
    """ Vaccine recommendation applies to.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, date, dateCriterion, doseNumber, forecastStatus, protocol, supportingImmunization, supportingPatientInformation, vaccineCode,):
        """ Initialize all valid properties.
        """
        self.date = date
        self.dateCriterion = dateCriterion
        self.doseNumber = doseNumber
        self.forecastStatus = forecastStatus
        self.protocol = protocol
        self.supportingImmunization = supportingImmunization
        self.supportingPatientInformation = supportingPatientInformation
        self.vaccineCode = vaccineCode

    def __repr__(self):
        return '<ImmunizationRecommendationRecommendation %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ImmunizationRecommendationRecommendationDateCriterion(backboneelement.BackboneElement):
    """ Dates governing proposed immunization.

    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """

    __tablename__ = "ImmunizationRecommendationRecommendationDateCriterion"

    code = Column(CodeableConcept)
    """ Type of date.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    value = Column(FHIRDate)
    """ Recommended date.
        Type `FHIRDate` (represented as `str` in JSON). """

    def __init__(self, code, value,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.value = value

    def __repr__(self):
        return '<ImmunizationRecommendationRecommendationDateCriterion %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ImmunizationRecommendationRecommendationProtocol(backboneelement.BackboneElement):
    """ Protocol used by recommendation.

    Contains information about the protocol under which the vaccine was
    administered.
    """

    __tablename__ = "ImmunizationRecommendationRecommendationProtocol"

    authority = Column(FHIRReference)
    """ Who is responsible for protocol.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    description = Column(primitives.StringField)
    """ Protocol details.
        Type `str`. """

    doseSequence = Column(Integer)
    """ Dose number within sequence.
        Type `int`. """

    series = Column(primitives.StringField)
    """ Name of vaccination series.
        Type `str`. """

    def __init__(self, authority, description, doseSequence, series,):
        """ Initialize all valid properties.
        """
        self.authority = authority
        self.description = description
        self.doseSequence = doseSequence
        self.series = series

    def __repr__(self):
        return '<ImmunizationRecommendationRecommendationProtocol %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier