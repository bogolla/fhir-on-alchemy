#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Observation)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class ObservationReferenceRange(backboneelement.BackboneElement):
    """ Provides guide for interpretation.

    Guidance on how to interpret the value by comparison to a normal or
    recommended range.
    """

    __tablename__ = "ObservationReferenceRange"

    age = Column(primitives.StringField,
                 ForeignKey('Range.id'))
    """ Applicable age range, if relevant.
        Type `Range` (represented as `dict` in JSON). """

    high = Column(primitives.StringField,
                  ForeignKey('Quantity.id'))
    """ High Range, if relevant.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    low = Column(primitives.StringField,
                 ForeignKey('Quantity.id'))
    """ Low Range, if relevant.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    meaning = Column(primitives.StringField,
                     ForeignKey('CodeableConcept.id'))
    """ Indicates the meaning/use of this range of this range.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    text = Column(primitives.StringField)
    """ Text based reference range in an observation.
        Type `str`. """

    def __init__(self, age, high, low, meaning, text,):
        """ Initialize all valid properties.
        """
        self.age = age
        self.high = high
        self.low = low
        self.meaning = meaning
        self.text = text

    def __repr__(self):
        return '<ObservationReferenceRange %r>' % 'self.property'  # replace self.property


class ObservationRelated(backboneelement.BackboneElement):
    """ Resource related to this observation.

    A  reference to another resource (usually another Observation but could
    also be a QuestionnaireAnswer) whose relationship is defined by the
    relationship type code.
    """

    __tablename__ = "ObservationRelated"

    # todo target = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    target = Column(primitives.StringField)
    """ Resource that is related to this one.
        Type `FHIRReference` referencing `Observation,
        QuestionnaireResponse` (represented as `dict` in JSON). """

    type = Column(primitives.StringField)
    """ has-member | derived-from | sequel-to | replaces | qualified-by |
        interfered-by.
        Type `str`. """

    def __init__(self, target, type,):
        """ Initialize all valid properties.
        """
        self.target = target
        self.type = type

    def __repr__(self):
        return '<ObservationRelated %r>' % 'self.property'  # replace self.property


class ObservationComponent(backboneelement.BackboneElement):
    """ Component results.

    Some observations have multiple component observations.  These component
    observations are expressed as separate code value pairs that share the same
    attributes.  Examples include systolic and diastolic component observations
    for blood pressure measurement and multiple component observations for
    genetics observations.
    """

    __tablename__ = "ObservationComponent"

    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Type of component observation (code / type).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    dataAbsentReason = Column(primitives.StringField,
                              ForeignKey('CodeableConcept.id'))
    """ Why the component result is missing.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    referenceRange = Column(primitives.StringField,
                            ForeignKey('ObservationReferenceRange.id'))
    """ Provides guide for interpretation of component result.
        List of `ObservationReferenceRange` items (represented as `dict` in JSON). """

    valueAttachment = Column(primitives.StringField,
                             ForeignKey('Attachment.id'))
    """ Actual component result.
        Type `Attachment` (represented as `dict` in JSON). """

    valueCodeableConcept = Column(primitives.StringField,
                                  ForeignKey('CodeableConcept.id'))
    """ Actual component result.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    valueDateTime = Column(primitives.DateTimeField)
    """ Actual component result.
        Type `FHIRDate` (represented as `str` in JSON). """

    valuePeriod = Column(primitives.StringField,
                         ForeignKey('Period.id'))
    """ Actual component result.
        Type `Period` (represented as `dict` in JSON). """

    valueQuantity = Column(primitives.StringField,
                           ForeignKey('Quantity.id'))
    """ Actual component result.
        Type `Quantity` (represented as `dict` in JSON). """

    valueRange = Column(primitives.StringField,
                        ForeignKey('Range.id'))
    """ Actual component result.
        Type `Range` (represented as `dict` in JSON). """

    valueRatio = Column(primitives.StringField,
                        ForeignKey('Ratio.id'))
    """ Actual component result.
        Type `Ratio` (represented as `dict` in JSON). """

    valueSampledData = Column(primitives.StringField,
                              ForeignKey('SampledData.id'))
    """ Actual component result.
        Type `SampledData` (represented as `dict` in JSON). """

    valueString = Column(primitives.StringField)
    """ Actual component result.
        Type `str`. """

    valueTime = Column(primitives.DateTimeField)
    """ Actual component result.
        Type `FHIRDate` (represented as `str` in JSON). """

    def __init__(self, code, dataAbsentReason, referenceRange,
                 valueAttachment, valueCodeableConcept, valueDateTime,
                 valuePeriod, valueQuantity, valueRange, valueRatio,
                 valueSampledData, valueString, valueTime,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.dataAbsentReason = dataAbsentReason
        self.referenceRange = referenceRange
        self.valueAttachment = valueAttachment
        self.valueCodeableConcept = valueCodeableConcept
        self.valueDateTime = valueDateTime
        self.valuePeriod = valuePeriod
        self.valueQuantity = valueQuantity
        self.valueRange = valueRange
        self.valueRatio = valueRatio
        self.valueSampledData = valueSampledData
        self.valueString = valueString
        self.valueTime = valueTime

    def __repr__(self):
        return '<ObservationComponent %r>' % 'self.property'  # replace self.property


class Observation(domainresource.DomainResource):
    """ Measurements and simple assertions.

    Measurements and simple assertions made about a patient, device or other
    subject.
    """

    __tablename__ = "Observation"
    
    bodySite = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Observed body part.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    category = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Classification of  type of observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Type of observation (code / type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    comments = Column(primitives.StringField)
    """ Comments about result.
        Type `str`. """
    
    component = Column(primitives.StringField,
                       ForeignKey('ObservationComponent.id'))
    """ Component results.
        List of `ObservationComponent` items (represented as `dict` in JSON). """
    
    dataAbsentReason = Column(primitives.StringField,
                              ForeignKey('CodeableConcept.id'))
    """ Why the result is missing.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo device = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    device = Column(primitives.StringField)
    """ (Measurement) Device.
        Type `FHIRReference` referencing `Device, DeviceMetric` (represented as `dict` in JSON). """
    
    effectiveDateTime = Column(primitives.DateTimeField)
    """ Clinically relevant time/time-period for observation.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    effectivePeriod = Column(primitives.StringField,
                             ForeignKey('Period.id'))
    """ Clinically relevant time/time-period for observation.
        Type `Period` (represented as `dict` in JSON). """
    
    # todo encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ Healthcare event during which this observation is made.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Unique Id for this particular observation.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    interpretation = Column(primitives.StringField,
                            ForeignKey('CodeableConcept.id'))
    """ High, low, normal, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    issued = Column(primitives.DateTimeField)
    """ Date/Time this was made available.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    method = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ How it was done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo performer = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    performer = Column(primitives.StringField)
    """ Who is responsible for the observation.
        List of `FHIRReference` items referencing `Practitioner,
        Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
    
    referenceRange = Column(primitives.StringField,
                            ForeignKey('ObservationReferenceRange.id'))
    """ Provides guide for interpretation.
        List of `ObservationReferenceRange` items (represented as `dict` in JSON). """
    
    related = Column(primitives.StringField,
                     ForeignKey('ObservationRelated.id'))
    """ Resource related to this observation.
        List of `ObservationRelated` items (represented as `dict` in JSON). """
    
    # todo specimen = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    specimen = Column(primitives.StringField)
    """ Specimen used for this observation.
        Type `FHIRReference` referencing `Specimen` (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ registered | preliminary | final | amended +.
        Type `str`. """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Who and/or what this is about.
        Type `FHIRReference` referencing `Patient, Group, Device,
        Location` (represented as `dict` in JSON). """
    
    valueAttachment = Column(primitives.StringField,
                             ForeignKey('Attachment.id'))
    """ Actual result.
        Type `Attachment` (represented as `dict` in JSON). """
    
    valueCodeableConcept = Column(primitives.StringField,
                                  ForeignKey('CodeableConcept.id'))
    """ Actual result.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    valueDateTime = Column(primitives.DateTimeField)
    """ Actual result.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    valuePeriod = Column(primitives.StringField,
                         ForeignKey('Period.id'))
    """ Actual result.
        Type `Period` (represented as `dict` in JSON). """
    
    valueQuantity = Column(primitives.StringField,
                           ForeignKey('Quantity.id'))
    """ Actual result.
        Type `Quantity` (represented as `dict` in JSON). """
    
    valueRange = Column(primitives.StringField,
                        ForeignKey('Range.id'))
    """ Actual result.
        Type `Range` (represented as `dict` in JSON). """
    
    valueRatio = Column(primitives.StringField,
                        ForeignKey('Ratio.id'))
    """ Actual result.
        Type `Ratio` (represented as `dict` in JSON). """
    
    valueSampledData = Column(primitives.StringField,
                              ForeignKey('SampledData.id'))
    """ Actual result.
        Type `SampledData` (represented as `dict` in JSON). """
    
    valueString = Column(primitives.StringField)
    """ Actual result.
        Type `str`. """
    
    valueTime = Column(primitives.DateTimeField)
    """ Actual result.
        Type `FHIRDate` (represented as `str` in JSON). """

    def __init__(self, bodySite, category, code, comments, component,
                 dataAbsentReason, device, effectiveDateTime, effectivePeriod,
                 encounter, identifier, interpretation, issued, method,
                 performer, referenceRange, related, specimen, status,
                 subject, valueAttachment, valueCodeableConcept, valueDateTime,
                 valuePeriod, valueQuantity, valueRange, valueRatio,
                 valueSampledData, valueString, valueTime,):
        """ Initialize all valid properties.
        """
        self.bodySite = bodySite
        self.category = category
        self.code = code
        self.comments = comments
        self.component = component
        self.dataAbsentReason = dataAbsentReason
        self.device = device
        self.effectiveDateTime = effectiveDateTime
        self.effectivePeriod = effectivePeriod
        self.encounter = encounter
        self.identifier = identifier
        self.interpretation = interpretation
        self.issued = issued
        self.method = method
        self.performer = performer
        self.referenceRange = referenceRange
        self.related = related
        self.specimen = specimen
        self.status = status
        self.subject = subject
        self.valueAttachment = valueAttachment
        self.valueCodeableConcept = valueCodeableConcept
        self.valueDateTime = valueDateTime
        self.valuePeriod = valuePeriod
        self.valueQuantity = valueQuantity
        self.valueRange = valueRange
        self.valueRatio = valueRatio
        self.valueSampledData = valueSampledData
        self.valueString = valueString
        self.valueTime = valueTime

    def __repr__(self):
        return '<Observation %r>' % 'self.property'  # replace self.property
