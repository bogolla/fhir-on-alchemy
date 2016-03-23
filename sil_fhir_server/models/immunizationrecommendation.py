#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class ImmunizationRecommendationRecommendationDateCriterion(backboneelement.BackboneElement):
    """ Dates governing proposed immunization.

    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """

    __tablename__ = "ImmunizationRecommendationRecommendationDateCriterion"

    code = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ Type of date.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    value = Column(primitives.DateTimeField)
    """ Recommended date.
        Type `FHIRDate` (represented as `str` in JSON). """

    def __init__(self, code, value,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.value = value

    def __repr__(self):
        return '<ImmunizationRecommendationRecommendationDateCriterion %r>' % 'self.property'  # replace self.property


class ImmunizationRecommendationRecommendationProtocol(backboneelement.BackboneElement):
    """ Protocol used by recommendation.

    Contains information about the protocol under which the vaccine was
    administered.
    """

    __tablename__ = "ImmunizationRecommendationRecommendationProtocol"

    # todo authority = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    authority = Column(primitives.StringField)
    """ Who is responsible for protocol.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    description = Column(primitives.StringField)
    """ Protocol details.
        Type `str`. """

    doseSequence = Column(primitives.IntegerField)
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


class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    """ Vaccine administration recommendations.
    """

    __tablename__ = "ImmunizationRecommendationRecommendation"

    date = Column(primitives.DateTimeField)
    """ Date recommendation created.
        Type `FHIRDate` (represented as `str` in JSON). """

    dateCriterion = Column(primitives.StringField,
                           ForeignKey(
                               'ImmunizationRecommendationRecommendationDateCriterion.id'))
    """ Dates governing proposed immunization.
        List of `ImmunizationRecommendationRecommendationDateCriterion`
        items (represented as `dict` in JSON). """

    doseNumber = Column(primitives.IntegerField)
    """ Recommended dose number.
        Type `int`. """

    forecastStatus = Column(primitives.StringField,
                            ForeignKey('CodeableConcept.id'))
    """ Vaccine administration status.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    protocol = Column(primitives.StringField,
                      ForeignKey(
                          'ImmunizationRecommendationRecommendationProtocol.id'))
    """ Protocol used by recommendation.
        Type `ImmunizationRecommendationRecommendationProtocol` (represented as `dict` in JSON). """

    # todo supportingImmunization = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    supportingImmunization = Column(primitives.StringField)
    """ Past immunizations supporting recommendation.
        List of `FHIRReference` items referencing `Immunization` (represented as `dict` in JSON). """

    # todo supportingPatientInformation = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    supportingPatientInformation = Column(primitives.StringField)
    """ Patient observations supporting recommendation.
        List of `FHIRReference` items referencing `Observation, AllergyIntolerance`
        (represented as `dict` in JSON). """

    vaccineCode = Column(primitives.StringField,
                         ForeignKey('CodeableConcept.id'))
    """ Vaccine recommendation applies to.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, date, dateCriterion, doseNumber, forecastStatus, protocol,
                 supportingImmunization, supportingPatientInformation, vaccineCode,):
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


class ImmunizationRecommendation(domainresource.DomainResource):
    """ Guidance or advice relating to an immunization.

    A patient's point-in-time immunization and recommendation (i.e. forecasting
    a patient's immunization eligibility according to a published schedule)
    with optional supporting justification.
    """

    __tablename__ = "ImmunizationRecommendation"
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    # todo patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    patient = Column(primitives.StringField)
    """ Who this profile is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    recommendation = Column(primitives.StringField,
                            ForeignKey(
                                'ImmunizationRecommendationRecommendation.id'))
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
