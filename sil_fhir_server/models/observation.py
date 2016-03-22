#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Observation)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class Observation(domainresource.DomainResource):
    """ Measurements and simple assertions.

    Measurements and simple assertions made about a patient, device or other
    subject.
    """

    __tablename__ = "Observation"

    bodySite = Column(CodeableConcept)
    """ Observed body part.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    category = Column(CodeableConcept)
    """ Classification of  type of observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    code = Column(CodeableConcept)
    """ Type of observation (code / type).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    comments = Column(primitives.StringField)
    """ Comments about result.
        Type `str`. """

    component = Column(ObservationComponent)
    """ Component results.
        List of `ObservationComponent` items (represented as `dict` in JSON). """

    dataAbsentReason = Column(CodeableConcept)
    """ Why the result is missing.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    device = Column(FHIRReference)
    """ (Measurement) Device.
        Type `FHIRReference` referencing `Device, DeviceMetric` (represented as `dict` in JSON). """

    effectiveDateTime = Column(FHIRDate)
    """ Clinically relevant time/time-period for observation.
        Type `FHIRDate` (represented as `str` in JSON). """

    effectivePeriod = Column(Period)
    """ Clinically relevant time/time-period for observation.
        Type `Period` (represented as `dict` in JSON). """

    encounter = Column(FHIRReference)
    """ Healthcare event during which this observation is made.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Unique Id for this particular observation.
        List of `Identifier` items (represented as `dict` in JSON). """

    interpretation = Column(CodeableConcept)
    """ High, low, normal, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """

    issued = Column(FHIRDate)
    """ Date/Time this was made available.
        Type `FHIRDate` (represented as `str` in JSON). """

    method = Column(CodeableConcept)
    """ How it was done.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    performer = Column(FHIRReference)
    """ Who is responsible for the observation.
        List of `FHIRReference` items referencing `Practitioner, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """

    referenceRange = Column(ObservationReferenceRange)
    """ Provides guide for interpretation.
        List of `ObservationReferenceRange` items (represented as `dict` in JSON). """

    related = Column(ObservationRelated)
    """ Resource related to this observation.
        List of `ObservationRelated` items (represented as `dict` in JSON). """

    specimen = Column(FHIRReference)
    """ Specimen used for this observation.
        Type `FHIRReference` referencing `Specimen` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ registered | preliminary | final | amended +.
        Type `str`. """

    subject = Column(FHIRReference)
    """ Who and/or what this is about.
        Type `FHIRReference` referencing `Patient, Group, Device, Location` (represented as `dict` in JSON). """

    valueAttachment = Column(Attachment)
    """ Actual result.
        Type `Attachment` (represented as `dict` in JSON). """

    valueCodeableConcept = Column(CodeableConcept)
    """ Actual result.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    valueDateTime = Column(FHIRDate)
    """ Actual result.
        Type `FHIRDate` (represented as `str` in JSON). """

    valuePeriod = Column(Period)
    """ Actual result.
        Type `Period` (represented as `dict` in JSON). """

    valueQuantity = Column(Quantity)
    """ Actual result.
        Type `Quantity` (represented as `dict` in JSON). """

    valueRange = Column(Range)
    """ Actual result.
        Type `Range` (represented as `dict` in JSON). """

    valueRatio = Column(Ratio)
    """ Actual result.
        Type `Ratio` (represented as `dict` in JSON). """

    valueSampledData = Column(SampledData)
    """ Actual result.
        Type `SampledData` (represented as `dict` in JSON). """

    valueString = Column(primitives.StringField)
    """ Actual result.
        Type `str`. """

    valueTime = Column(FHIRDate)
    """ Actual result.
        Type `FHIRDate` (represented as `str` in JSON). """

    def __init__(self, bodySite, category, code, comments, component, dataAbsentReason, device, effectiveDateTime, effectivePeriod, encounter, identifier, interpretation, issued, method, performer, referenceRange, related, specimen, status, subject, valueAttachment, valueCodeableConcept, valueDateTime, valuePeriod, valueQuantity, valueRange, valueRatio, valueSampledData, valueString, valueTime,):
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


from sqlalchemy import Column, Integer, String
from . import backboneelement

class ObservationComponent(backboneelement.BackboneElement):
    """ Component results.

    Some observations have multiple component observations.  These component
    observations are expressed as separate code value pairs that share the same
    attributes.  Examples include systolic and diastolic component observations
    for blood pressure measurement and multiple component observations for
    genetics observations.
    """

    __tablename__ = "ObservationComponent"

    code = Column(CodeableConcept)
    """ Type of component observation (code / type).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    dataAbsentReason = Column(CodeableConcept)
    """ Why the component result is missing.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    referenceRange = Column(ObservationReferenceRange)
    """ Provides guide for interpretation of component result.
        List of `ObservationReferenceRange` items (represented as `dict` in JSON). """

    valueAttachment = Column(Attachment)
    """ Actual component result.
        Type `Attachment` (represented as `dict` in JSON). """

    valueCodeableConcept = Column(CodeableConcept)
    """ Actual component result.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    valueDateTime = Column(FHIRDate)
    """ Actual component result.
        Type `FHIRDate` (represented as `str` in JSON). """

    valuePeriod = Column(Period)
    """ Actual component result.
        Type `Period` (represented as `dict` in JSON). """

    valueQuantity = Column(Quantity)
    """ Actual component result.
        Type `Quantity` (represented as `dict` in JSON). """

    valueRange = Column(Range)
    """ Actual component result.
        Type `Range` (represented as `dict` in JSON). """

    valueRatio = Column(Ratio)
    """ Actual component result.
        Type `Ratio` (represented as `dict` in JSON). """

    valueSampledData = Column(SampledData)
    """ Actual component result.
        Type `SampledData` (represented as `dict` in JSON). """

    valueString = Column(primitives.StringField)
    """ Actual component result.
        Type `str`. """

    valueTime = Column(FHIRDate)
    """ Actual component result.
        Type `FHIRDate` (represented as `str` in JSON). """

    def __init__(self, code, dataAbsentReason, referenceRange, valueAttachment, valueCodeableConcept, valueDateTime, valuePeriod, valueQuantity, valueRange, valueRatio, valueSampledData, valueString, valueTime,):
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


from sqlalchemy import Column, Integer, String
class ObservationReferenceRange(backboneelement.BackboneElement):
    """ Provides guide for interpretation.

    Guidance on how to interpret the value by comparison to a normal or
    recommended range.
    """

    __tablename__ = "ObservationReferenceRange"

    age = Column(Range)
    """ Applicable age range, if relevant.
        Type `Range` (represented as `dict` in JSON). """

    high = Column(Quantity)
    """ High Range, if relevant.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    low = Column(Quantity)
    """ Low Range, if relevant.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    meaning = Column(CodeableConcept)
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


from sqlalchemy import Column, Integer, String
class ObservationRelated(backboneelement.BackboneElement):
    """ Resource related to this observation.

    A  reference to another resource (usually another Observation but could
    also be a QuestionnaireAnswer) whose relationship is defined by the
    relationship type code.
    """

    __tablename__ = "ObservationRelated"

    target = Column(FHIRReference)
    """ Resource that is related to this one.
        Type `FHIRReference` referencing `Observation, QuestionnaireResponse` (represented as `dict` in JSON). """

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


from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import ratio
from . import sampleddata