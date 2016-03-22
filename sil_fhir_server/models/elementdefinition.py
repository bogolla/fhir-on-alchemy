#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ElementDefinition)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import element

class ElementDefinition(element.Element):
    """ Definition of an element in a resource or extension.

    Captures constraints on each element within the resource, profile, or
    extension.
    """

    __tablename__ = "ElementDefinition"

    alias = Column(primitives.StringField)
    """ Other names.
        List of `str` items. """

    base = Column(ElementDefinitionBase)
    """ Base definition information for tools.
        Type `ElementDefinitionBase` (represented as `dict` in JSON). """

    binding = Column(ElementDefinitionBinding)
    """ ValueSet details if this is coded.
        Type `ElementDefinitionBinding` (represented as `dict` in JSON). """

    code = Column(Coding)
    """ Defining code.
        List of `Coding` items (represented as `dict` in JSON). """

    comments = Column(primitives.StringField)
    """ Comments about the use of this element.
        Type `str`. """

    condition = Column(primitives.StringField)
    """ Reference to invariant about presence.
        List of `str` items. """

    constraint = Column(ElementDefinitionConstraint)
    """ Condition that must evaluate to true.
        List of `ElementDefinitionConstraint` items (represented as `dict` in JSON). """

    defaultValueAddress = Column(Address)
    """ Specified value it missing from instance.
        Type `Address` (represented as `dict` in JSON). """

    defaultValueAnnotation = Column(Annotation)
    """ Specified value it missing from instance.
        Type `Annotation` (represented as `dict` in JSON). """

    defaultValueAttachment = Column(Attachment)
    """ Specified value it missing from instance.
        Type `Attachment` (represented as `dict` in JSON). """

    defaultValueBase64Binary = Column(primitives.StringField)
    """ Specified value it missing from instance.
        Type `str`. """

    defaultValueBoolean = Column(bool)
    """ Specified value it missing from instance.
        Type `bool`. """

    defaultValueCode = Column(primitives.StringField)
    """ Specified value it missing from instance.
        Type `str`. """

    defaultValueCodeableConcept = Column(CodeableConcept)
    """ Specified value it missing from instance.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    defaultValueCoding = Column(Coding)
    """ Specified value it missing from instance.
        Type `Coding` (represented as `dict` in JSON). """

    defaultValueContactPoint = Column(ContactPoint)
    """ Specified value it missing from instance.
        Type `ContactPoint` (represented as `dict` in JSON). """

    defaultValueDate = Column(FHIRDate)
    """ Specified value it missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """

    defaultValueDateTime = Column(FHIRDate)
    """ Specified value it missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """

    defaultValueDecimal = Column(float)
    """ Specified value it missing from instance.
        Type `float`. """

    defaultValueHumanName = Column(HumanName)
    """ Specified value it missing from instance.
        Type `HumanName` (represented as `dict` in JSON). """

    defaultValueId = Column(primitives.StringField)
    """ Specified value it missing from instance.
        Type `str`. """

    defaultValueIdentifier = Column(Identifier)
    """ Specified value it missing from instance.
        Type `Identifier` (represented as `dict` in JSON). """

    defaultValueInstant = Column(FHIRDate)
    """ Specified value it missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """

    defaultValueInteger = Column(Integer)
    """ Specified value it missing from instance.
        Type `int`. """

    defaultValueMarkdown = Column(primitives.StringField)
    """ Specified value it missing from instance.
        Type `str`. """

    defaultValueMeta = Column(Meta)
    """ Specified value it missing from instance.
        Type `Meta` (represented as `dict` in JSON). """

    defaultValueOid = Column(primitives.StringField)
    """ Specified value it missing from instance.
        Type `str`. """

    defaultValuePeriod = Column(Period)
    """ Specified value it missing from instance.
        Type `Period` (represented as `dict` in JSON). """

    defaultValuePositiveInt = Column(Integer)
    """ Specified value it missing from instance.
        Type `int`. """

    defaultValueQuantity = Column(Quantity)
    """ Specified value it missing from instance.
        Type `Quantity` (represented as `dict` in JSON). """

    defaultValueRange = Column(Range)
    """ Specified value it missing from instance.
        Type `Range` (represented as `dict` in JSON). """

    defaultValueRatio = Column(Ratio)
    """ Specified value it missing from instance.
        Type `Ratio` (represented as `dict` in JSON). """

    defaultValueReference = Column(FHIRReference)
    """ Specified value it missing from instance.
        Type `FHIRReference` (represented as `dict` in JSON). """

    defaultValueSampledData = Column(SampledData)
    """ Specified value it missing from instance.
        Type `SampledData` (represented as `dict` in JSON). """

    defaultValueSignature = Column(Signature)
    """ Specified value it missing from instance.
        Type `Signature` (represented as `dict` in JSON). """

    defaultValueString = Column(primitives.StringField)
    """ Specified value it missing from instance.
        Type `str`. """

    defaultValueTime = Column(FHIRDate)
    """ Specified value it missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """

    defaultValueTiming = Column(Timing)
    """ Specified value it missing from instance.
        Type `Timing` (represented as `dict` in JSON). """

    defaultValueUnsignedInt = Column(Integer)
    """ Specified value it missing from instance.
        Type `int`. """

    defaultValueUri = Column(primitives.StringField)
    """ Specified value it missing from instance.
        Type `str`. """

    definition = Column(primitives.StringField)
    """ Full formal definition as narrative text.
        Type `str`. """

    exampleAddress = Column(Address)
    """ Example value: [as defined for type].
        Type `Address` (represented as `dict` in JSON). """

    exampleAnnotation = Column(Annotation)
    """ Example value: [as defined for type].
        Type `Annotation` (represented as `dict` in JSON). """

    exampleAttachment = Column(Attachment)
    """ Example value: [as defined for type].
        Type `Attachment` (represented as `dict` in JSON). """

    exampleBase64Binary = Column(primitives.StringField)
    """ Example value: [as defined for type].
        Type `str`. """

    exampleBoolean = Column(bool)
    """ Example value: [as defined for type].
        Type `bool`. """

    exampleCode = Column(primitives.StringField)
    """ Example value: [as defined for type].
        Type `str`. """

    exampleCodeableConcept = Column(CodeableConcept)
    """ Example value: [as defined for type].
        Type `CodeableConcept` (represented as `dict` in JSON). """

    exampleCoding = Column(Coding)
    """ Example value: [as defined for type].
        Type `Coding` (represented as `dict` in JSON). """

    exampleContactPoint = Column(ContactPoint)
    """ Example value: [as defined for type].
        Type `ContactPoint` (represented as `dict` in JSON). """

    exampleDate = Column(FHIRDate)
    """ Example value: [as defined for type].
        Type `FHIRDate` (represented as `str` in JSON). """

    exampleDateTime = Column(FHIRDate)
    """ Example value: [as defined for type].
        Type `FHIRDate` (represented as `str` in JSON). """

    exampleDecimal = Column(float)
    """ Example value: [as defined for type].
        Type `float`. """

    exampleHumanName = Column(HumanName)
    """ Example value: [as defined for type].
        Type `HumanName` (represented as `dict` in JSON). """

    exampleId = Column(primitives.StringField)
    """ Example value: [as defined for type].
        Type `str`. """

    exampleIdentifier = Column(Identifier)
    """ Example value: [as defined for type].
        Type `Identifier` (represented as `dict` in JSON). """

    exampleInstant = Column(FHIRDate)
    """ Example value: [as defined for type].
        Type `FHIRDate` (represented as `str` in JSON). """

    exampleInteger = Column(Integer)
    """ Example value: [as defined for type].
        Type `int`. """

    exampleMarkdown = Column(primitives.StringField)
    """ Example value: [as defined for type].
        Type `str`. """

    exampleMeta = Column(Meta)
    """ Example value: [as defined for type].
        Type `Meta` (represented as `dict` in JSON). """

    exampleOid = Column(primitives.StringField)
    """ Example value: [as defined for type].
        Type `str`. """

    examplePeriod = Column(Period)
    """ Example value: [as defined for type].
        Type `Period` (represented as `dict` in JSON). """

    examplePositiveInt = Column(Integer)
    """ Example value: [as defined for type].
        Type `int`. """

    exampleQuantity = Column(Quantity)
    """ Example value: [as defined for type].
        Type `Quantity` (represented as `dict` in JSON). """

    exampleRange = Column(Range)
    """ Example value: [as defined for type].
        Type `Range` (represented as `dict` in JSON). """

    exampleRatio = Column(Ratio)
    """ Example value: [as defined for type].
        Type `Ratio` (represented as `dict` in JSON). """

    exampleReference = Column(FHIRReference)
    """ Example value: [as defined for type].
        Type `FHIRReference` (represented as `dict` in JSON). """

    exampleSampledData = Column(SampledData)
    """ Example value: [as defined for type].
        Type `SampledData` (represented as `dict` in JSON). """

    exampleSignature = Column(Signature)
    """ Example value: [as defined for type].
        Type `Signature` (represented as `dict` in JSON). """

    exampleString = Column(primitives.StringField)
    """ Example value: [as defined for type].
        Type `str`. """

    exampleTime = Column(FHIRDate)
    """ Example value: [as defined for type].
        Type `FHIRDate` (represented as `str` in JSON). """

    exampleTiming = Column(Timing)
    """ Example value: [as defined for type].
        Type `Timing` (represented as `dict` in JSON). """

    exampleUnsignedInt = Column(Integer)
    """ Example value: [as defined for type].
        Type `int`. """

    exampleUri = Column(primitives.StringField)
    """ Example value: [as defined for type].
        Type `str`. """

    fixedAddress = Column(Address)
    """ Value must be exactly this.
        Type `Address` (represented as `dict` in JSON). """

    fixedAnnotation = Column(Annotation)
    """ Value must be exactly this.
        Type `Annotation` (represented as `dict` in JSON). """

    fixedAttachment = Column(Attachment)
    """ Value must be exactly this.
        Type `Attachment` (represented as `dict` in JSON). """

    fixedBase64Binary = Column(primitives.StringField)
    """ Value must be exactly this.
        Type `str`. """

    fixedBoolean = Column(bool)
    """ Value must be exactly this.
        Type `bool`. """

    fixedCode = Column(primitives.StringField)
    """ Value must be exactly this.
        Type `str`. """

    fixedCodeableConcept = Column(CodeableConcept)
    """ Value must be exactly this.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    fixedCoding = Column(Coding)
    """ Value must be exactly this.
        Type `Coding` (represented as `dict` in JSON). """

    fixedContactPoint = Column(ContactPoint)
    """ Value must be exactly this.
        Type `ContactPoint` (represented as `dict` in JSON). """

    fixedDate = Column(FHIRDate)
    """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """

    fixedDateTime = Column(FHIRDate)
    """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """

    fixedDecimal = Column(float)
    """ Value must be exactly this.
        Type `float`. """

    fixedHumanName = Column(HumanName)
    """ Value must be exactly this.
        Type `HumanName` (represented as `dict` in JSON). """

    fixedId = Column(primitives.StringField)
    """ Value must be exactly this.
        Type `str`. """

    fixedIdentifier = Column(Identifier)
    """ Value must be exactly this.
        Type `Identifier` (represented as `dict` in JSON). """

    fixedInstant = Column(FHIRDate)
    """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """

    fixedInteger = Column(Integer)
    """ Value must be exactly this.
        Type `int`. """

    fixedMarkdown = Column(primitives.StringField)
    """ Value must be exactly this.
        Type `str`. """

    fixedMeta = Column(Meta)
    """ Value must be exactly this.
        Type `Meta` (represented as `dict` in JSON). """

    fixedOid = Column(primitives.StringField)
    """ Value must be exactly this.
        Type `str`. """

    fixedPeriod = Column(Period)
    """ Value must be exactly this.
        Type `Period` (represented as `dict` in JSON). """

    fixedPositiveInt = Column(Integer)
    """ Value must be exactly this.
        Type `int`. """

    fixedQuantity = Column(Quantity)
    """ Value must be exactly this.
        Type `Quantity` (represented as `dict` in JSON). """

    fixedRange = Column(Range)
    """ Value must be exactly this.
        Type `Range` (represented as `dict` in JSON). """

    fixedRatio = Column(Ratio)
    """ Value must be exactly this.
        Type `Ratio` (represented as `dict` in JSON). """

    fixedReference = Column(FHIRReference)
    """ Value must be exactly this.
        Type `FHIRReference` (represented as `dict` in JSON). """

    fixedSampledData = Column(SampledData)
    """ Value must be exactly this.
        Type `SampledData` (represented as `dict` in JSON). """

    fixedSignature = Column(Signature)
    """ Value must be exactly this.
        Type `Signature` (represented as `dict` in JSON). """

    fixedString = Column(primitives.StringField)
    """ Value must be exactly this.
        Type `str`. """

    fixedTime = Column(FHIRDate)
    """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """

    fixedTiming = Column(Timing)
    """ Value must be exactly this.
        Type `Timing` (represented as `dict` in JSON). """

    fixedUnsignedInt = Column(Integer)
    """ Value must be exactly this.
        Type `int`. """

    fixedUri = Column(primitives.StringField)
    """ Value must be exactly this.
        Type `str`. """

    isModifier = Column(bool)
    """ If this modifies the meaning of other elements.
        Type `bool`. """

    isSummary = Column(bool)
    """ Include when _summary = true?.
        Type `bool`. """

    label = Column(primitives.StringField)
    """ Name for element to display with or prompt for element.
        Type `str`. """

    mapping = Column(ElementDefinitionMapping)
    """ Map element to another set of definitions.
        List of `ElementDefinitionMapping` items (represented as `dict` in JSON). """

    max = Column(primitives.StringField)
    """ Maximum Cardinality (a number or *).
        Type `str`. """

    maxLength = Column(Integer)
    """ Max length for strings.
        Type `int`. """

    maxValueAddress = Column(Address)
    """ Maximum Allowed Value (for some types).
        Type `Address` (represented as `dict` in JSON). """

    maxValueAnnotation = Column(Annotation)
    """ Maximum Allowed Value (for some types).
        Type `Annotation` (represented as `dict` in JSON). """

    maxValueAttachment = Column(Attachment)
    """ Maximum Allowed Value (for some types).
        Type `Attachment` (represented as `dict` in JSON). """

    maxValueBase64Binary = Column(primitives.StringField)
    """ Maximum Allowed Value (for some types).
        Type `str`. """

    maxValueBoolean = Column(bool)
    """ Maximum Allowed Value (for some types).
        Type `bool`. """

    maxValueCode = Column(primitives.StringField)
    """ Maximum Allowed Value (for some types).
        Type `str`. """

    maxValueCodeableConcept = Column(CodeableConcept)
    """ Maximum Allowed Value (for some types).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    maxValueCoding = Column(Coding)
    """ Maximum Allowed Value (for some types).
        Type `Coding` (represented as `dict` in JSON). """

    maxValueContactPoint = Column(ContactPoint)
    """ Maximum Allowed Value (for some types).
        Type `ContactPoint` (represented as `dict` in JSON). """

    maxValueDate = Column(FHIRDate)
    """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """

    maxValueDateTime = Column(FHIRDate)
    """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """

    maxValueDecimal = Column(float)
    """ Maximum Allowed Value (for some types).
        Type `float`. """

    maxValueHumanName = Column(HumanName)
    """ Maximum Allowed Value (for some types).
        Type `HumanName` (represented as `dict` in JSON). """

    maxValueId = Column(primitives.StringField)
    """ Maximum Allowed Value (for some types).
        Type `str`. """

    maxValueIdentifier = Column(Identifier)
    """ Maximum Allowed Value (for some types).
        Type `Identifier` (represented as `dict` in JSON). """

    maxValueInstant = Column(FHIRDate)
    """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """

    maxValueInteger = Column(Integer)
    """ Maximum Allowed Value (for some types).
        Type `int`. """

    maxValueMarkdown = Column(primitives.StringField)
    """ Maximum Allowed Value (for some types).
        Type `str`. """

    maxValueMeta = Column(Meta)
    """ Maximum Allowed Value (for some types).
        Type `Meta` (represented as `dict` in JSON). """

    maxValueOid = Column(primitives.StringField)
    """ Maximum Allowed Value (for some types).
        Type `str`. """

    maxValuePeriod = Column(Period)
    """ Maximum Allowed Value (for some types).
        Type `Period` (represented as `dict` in JSON). """

    maxValuePositiveInt = Column(Integer)
    """ Maximum Allowed Value (for some types).
        Type `int`. """

    maxValueQuantity = Column(Quantity)
    """ Maximum Allowed Value (for some types).
        Type `Quantity` (represented as `dict` in JSON). """

    maxValueRange = Column(Range)
    """ Maximum Allowed Value (for some types).
        Type `Range` (represented as `dict` in JSON). """

    maxValueRatio = Column(Ratio)
    """ Maximum Allowed Value (for some types).
        Type `Ratio` (represented as `dict` in JSON). """

    maxValueReference = Column(FHIRReference)
    """ Maximum Allowed Value (for some types).
        Type `FHIRReference` (represented as `dict` in JSON). """

    maxValueSampledData = Column(SampledData)
    """ Maximum Allowed Value (for some types).
        Type `SampledData` (represented as `dict` in JSON). """

    maxValueSignature = Column(Signature)
    """ Maximum Allowed Value (for some types).
        Type `Signature` (represented as `dict` in JSON). """

    maxValueString = Column(primitives.StringField)
    """ Maximum Allowed Value (for some types).
        Type `str`. """

    maxValueTime = Column(FHIRDate)
    """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """

    maxValueTiming = Column(Timing)
    """ Maximum Allowed Value (for some types).
        Type `Timing` (represented as `dict` in JSON). """

    maxValueUnsignedInt = Column(Integer)
    """ Maximum Allowed Value (for some types).
        Type `int`. """

    maxValueUri = Column(primitives.StringField)
    """ Maximum Allowed Value (for some types).
        Type `str`. """

    meaningWhenMissing = Column(primitives.StringField)
    """ Implicit meaning when this element is missing.
        Type `str`. """

    min = Column(Integer)
    """ Minimum Cardinality.
        Type `int`. """

    minValueAddress = Column(Address)
    """ Minimum Allowed Value (for some types).
        Type `Address` (represented as `dict` in JSON). """

    minValueAnnotation = Column(Annotation)
    """ Minimum Allowed Value (for some types).
        Type `Annotation` (represented as `dict` in JSON). """

    minValueAttachment = Column(Attachment)
    """ Minimum Allowed Value (for some types).
        Type `Attachment` (represented as `dict` in JSON). """

    minValueBase64Binary = Column(primitives.StringField)
    """ Minimum Allowed Value (for some types).
        Type `str`. """

    minValueBoolean = Column(bool)
    """ Minimum Allowed Value (for some types).
        Type `bool`. """

    minValueCode = Column(primitives.StringField)
    """ Minimum Allowed Value (for some types).
        Type `str`. """

    minValueCodeableConcept = Column(CodeableConcept)
    """ Minimum Allowed Value (for some types).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    minValueCoding = Column(Coding)
    """ Minimum Allowed Value (for some types).
        Type `Coding` (represented as `dict` in JSON). """

    minValueContactPoint = Column(ContactPoint)
    """ Minimum Allowed Value (for some types).
        Type `ContactPoint` (represented as `dict` in JSON). """

    minValueDate = Column(FHIRDate)
    """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """

    minValueDateTime = Column(FHIRDate)
    """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """

    minValueDecimal = Column(float)
    """ Minimum Allowed Value (for some types).
        Type `float`. """

    minValueHumanName = Column(HumanName)
    """ Minimum Allowed Value (for some types).
        Type `HumanName` (represented as `dict` in JSON). """

    minValueId = Column(primitives.StringField)
    """ Minimum Allowed Value (for some types).
        Type `str`. """

    minValueIdentifier = Column(Identifier)
    """ Minimum Allowed Value (for some types).
        Type `Identifier` (represented as `dict` in JSON). """

    minValueInstant = Column(FHIRDate)
    """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """

    minValueInteger = Column(Integer)
    """ Minimum Allowed Value (for some types).
        Type `int`. """

    minValueMarkdown = Column(primitives.StringField)
    """ Minimum Allowed Value (for some types).
        Type `str`. """

    minValueMeta = Column(Meta)
    """ Minimum Allowed Value (for some types).
        Type `Meta` (represented as `dict` in JSON). """

    minValueOid = Column(primitives.StringField)
    """ Minimum Allowed Value (for some types).
        Type `str`. """

    minValuePeriod = Column(Period)
    """ Minimum Allowed Value (for some types).
        Type `Period` (represented as `dict` in JSON). """

    minValuePositiveInt = Column(Integer)
    """ Minimum Allowed Value (for some types).
        Type `int`. """

    minValueQuantity = Column(Quantity)
    """ Minimum Allowed Value (for some types).
        Type `Quantity` (represented as `dict` in JSON). """

    minValueRange = Column(Range)
    """ Minimum Allowed Value (for some types).
        Type `Range` (represented as `dict` in JSON). """

    minValueRatio = Column(Ratio)
    """ Minimum Allowed Value (for some types).
        Type `Ratio` (represented as `dict` in JSON). """

    minValueReference = Column(FHIRReference)
    """ Minimum Allowed Value (for some types).
        Type `FHIRReference` (represented as `dict` in JSON). """

    minValueSampledData = Column(SampledData)
    """ Minimum Allowed Value (for some types).
        Type `SampledData` (represented as `dict` in JSON). """

    minValueSignature = Column(Signature)
    """ Minimum Allowed Value (for some types).
        Type `Signature` (represented as `dict` in JSON). """

    minValueString = Column(primitives.StringField)
    """ Minimum Allowed Value (for some types).
        Type `str`. """

    minValueTime = Column(FHIRDate)
    """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """

    minValueTiming = Column(Timing)
    """ Minimum Allowed Value (for some types).
        Type `Timing` (represented as `dict` in JSON). """

    minValueUnsignedInt = Column(Integer)
    """ Minimum Allowed Value (for some types).
        Type `int`. """

    minValueUri = Column(primitives.StringField)
    """ Minimum Allowed Value (for some types).
        Type `str`. """

    mustSupport = Column(bool)
    """ If the element must supported.
        Type `bool`. """

    name = Column(primitives.StringField)
    """ Name for this particular element definition (reference target).
        Type `str`. """

    nameReference = Column(primitives.StringField)
    """ To another element constraint (by element.name).
        Type `str`. """

    path = Column(primitives.StringField)
    """ The path of the element (see the Detailed Descriptions).
        Type `str`. """

    patternAddress = Column(Address)
    """ Value must have at least these property values.
        Type `Address` (represented as `dict` in JSON). """

    patternAnnotation = Column(Annotation)
    """ Value must have at least these property values.
        Type `Annotation` (represented as `dict` in JSON). """

    patternAttachment = Column(Attachment)
    """ Value must have at least these property values.
        Type `Attachment` (represented as `dict` in JSON). """

    patternBase64Binary = Column(primitives.StringField)
    """ Value must have at least these property values.
        Type `str`. """

    patternBoolean = Column(bool)
    """ Value must have at least these property values.
        Type `bool`. """

    patternCode = Column(primitives.StringField)
    """ Value must have at least these property values.
        Type `str`. """

    patternCodeableConcept = Column(CodeableConcept)
    """ Value must have at least these property values.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    patternCoding = Column(Coding)
    """ Value must have at least these property values.
        Type `Coding` (represented as `dict` in JSON). """

    patternContactPoint = Column(ContactPoint)
    """ Value must have at least these property values.
        Type `ContactPoint` (represented as `dict` in JSON). """

    patternDate = Column(FHIRDate)
    """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """

    patternDateTime = Column(FHIRDate)
    """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """

    patternDecimal = Column(float)
    """ Value must have at least these property values.
        Type `float`. """

    patternHumanName = Column(HumanName)
    """ Value must have at least these property values.
        Type `HumanName` (represented as `dict` in JSON). """

    patternId = Column(primitives.StringField)
    """ Value must have at least these property values.
        Type `str`. """

    patternIdentifier = Column(Identifier)
    """ Value must have at least these property values.
        Type `Identifier` (represented as `dict` in JSON). """

    patternInstant = Column(FHIRDate)
    """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """

    patternInteger = Column(Integer)
    """ Value must have at least these property values.
        Type `int`. """

    patternMarkdown = Column(primitives.StringField)
    """ Value must have at least these property values.
        Type `str`. """

    patternMeta = Column(Meta)
    """ Value must have at least these property values.
        Type `Meta` (represented as `dict` in JSON). """

    patternOid = Column(primitives.StringField)
    """ Value must have at least these property values.
        Type `str`. """

    patternPeriod = Column(Period)
    """ Value must have at least these property values.
        Type `Period` (represented as `dict` in JSON). """

    patternPositiveInt = Column(Integer)
    """ Value must have at least these property values.
        Type `int`. """

    patternQuantity = Column(Quantity)
    """ Value must have at least these property values.
        Type `Quantity` (represented as `dict` in JSON). """

    patternRange = Column(Range)
    """ Value must have at least these property values.
        Type `Range` (represented as `dict` in JSON). """

    patternRatio = Column(Ratio)
    """ Value must have at least these property values.
        Type `Ratio` (represented as `dict` in JSON). """

    patternReference = Column(FHIRReference)
    """ Value must have at least these property values.
        Type `FHIRReference` (represented as `dict` in JSON). """

    patternSampledData = Column(SampledData)
    """ Value must have at least these property values.
        Type `SampledData` (represented as `dict` in JSON). """

    patternSignature = Column(Signature)
    """ Value must have at least these property values.
        Type `Signature` (represented as `dict` in JSON). """

    patternString = Column(primitives.StringField)
    """ Value must have at least these property values.
        Type `str`. """

    patternTime = Column(FHIRDate)
    """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """

    patternTiming = Column(Timing)
    """ Value must have at least these property values.
        Type `Timing` (represented as `dict` in JSON). """

    patternUnsignedInt = Column(Integer)
    """ Value must have at least these property values.
        Type `int`. """

    patternUri = Column(primitives.StringField)
    """ Value must have at least these property values.
        Type `str`. """

    representation = Column(primitives.StringField)
    """ How this element is represented in instances.
        List of `str` items. """

    requirements = Column(primitives.StringField)
    """ Why is this needed?.
        Type `str`. """

    short = Column(primitives.StringField)
    """ Concise definition for xml presentation.
        Type `str`. """

    slicing = Column(ElementDefinitionSlicing)
    """ This element is sliced - slices follow.
        Type `ElementDefinitionSlicing` (represented as `dict` in JSON). """

    type = Column(ElementDefinitionType)
    """ Data type and Profile for this element.
        List of `ElementDefinitionType` items (represented as `dict` in JSON). """

    def __init__(self, alias, base, binding, code, comments, condition, constraint, defaultValueAddress, defaultValueAnnotation, defaultValueAttachment, defaultValueBase64Binary, defaultValueBoolean, defaultValueCode, defaultValueCodeableConcept, defaultValueCoding, defaultValueContactPoint, defaultValueDate, defaultValueDateTime, defaultValueDecimal, defaultValueHumanName, defaultValueId, defaultValueIdentifier, defaultValueInstant, defaultValueInteger, defaultValueMarkdown, defaultValueMeta, defaultValueOid, defaultValuePeriod, defaultValuePositiveInt, defaultValueQuantity, defaultValueRange, defaultValueRatio, defaultValueReference, defaultValueSampledData, defaultValueSignature, defaultValueString, defaultValueTime, defaultValueTiming, defaultValueUnsignedInt, defaultValueUri, definition, exampleAddress, exampleAnnotation, exampleAttachment, exampleBase64Binary, exampleBoolean, exampleCode, exampleCodeableConcept, exampleCoding, exampleContactPoint, exampleDate, exampleDateTime, exampleDecimal, exampleHumanName, exampleId, exampleIdentifier, exampleInstant, exampleInteger, exampleMarkdown, exampleMeta, exampleOid, examplePeriod, examplePositiveInt, exampleQuantity, exampleRange, exampleRatio, exampleReference, exampleSampledData, exampleSignature, exampleString, exampleTime, exampleTiming, exampleUnsignedInt, exampleUri, fixedAddress, fixedAnnotation, fixedAttachment, fixedBase64Binary, fixedBoolean, fixedCode, fixedCodeableConcept, fixedCoding, fixedContactPoint, fixedDate, fixedDateTime, fixedDecimal, fixedHumanName, fixedId, fixedIdentifier, fixedInstant, fixedInteger, fixedMarkdown, fixedMeta, fixedOid, fixedPeriod, fixedPositiveInt, fixedQuantity, fixedRange, fixedRatio, fixedReference, fixedSampledData, fixedSignature, fixedString, fixedTime, fixedTiming, fixedUnsignedInt, fixedUri, isModifier, isSummary, label, mapping, max, maxLength, maxValueAddress, maxValueAnnotation, maxValueAttachment, maxValueBase64Binary, maxValueBoolean, maxValueCode, maxValueCodeableConcept, maxValueCoding, maxValueContactPoint, maxValueDate, maxValueDateTime, maxValueDecimal, maxValueHumanName, maxValueId, maxValueIdentifier, maxValueInstant, maxValueInteger, maxValueMarkdown, maxValueMeta, maxValueOid, maxValuePeriod, maxValuePositiveInt, maxValueQuantity, maxValueRange, maxValueRatio, maxValueReference, maxValueSampledData, maxValueSignature, maxValueString, maxValueTime, maxValueTiming, maxValueUnsignedInt, maxValueUri, meaningWhenMissing, min, minValueAddress, minValueAnnotation, minValueAttachment, minValueBase64Binary, minValueBoolean, minValueCode, minValueCodeableConcept, minValueCoding, minValueContactPoint, minValueDate, minValueDateTime, minValueDecimal, minValueHumanName, minValueId, minValueIdentifier, minValueInstant, minValueInteger, minValueMarkdown, minValueMeta, minValueOid, minValuePeriod, minValuePositiveInt, minValueQuantity, minValueRange, minValueRatio, minValueReference, minValueSampledData, minValueSignature, minValueString, minValueTime, minValueTiming, minValueUnsignedInt, minValueUri, mustSupport, name, nameReference, path, patternAddress, patternAnnotation, patternAttachment, patternBase64Binary, patternBoolean, patternCode, patternCodeableConcept, patternCoding, patternContactPoint, patternDate, patternDateTime, patternDecimal, patternHumanName, patternId, patternIdentifier, patternInstant, patternInteger, patternMarkdown, patternMeta, patternOid, patternPeriod, patternPositiveInt, patternQuantity, patternRange, patternRatio, patternReference, patternSampledData, patternSignature, patternString, patternTime, patternTiming, patternUnsignedInt, patternUri, representation, requirements, short, slicing, type,):
        """ Initialize all valid properties.
        """
        self.alias = alias
        self.base = base
        self.binding = binding
        self.code = code
        self.comments = comments
        self.condition = condition
        self.constraint = constraint
        self.defaultValueAddress = defaultValueAddress
        self.defaultValueAnnotation = defaultValueAnnotation
        self.defaultValueAttachment = defaultValueAttachment
        self.defaultValueBase64Binary = defaultValueBase64Binary
        self.defaultValueBoolean = defaultValueBoolean
        self.defaultValueCode = defaultValueCode
        self.defaultValueCodeableConcept = defaultValueCodeableConcept
        self.defaultValueCoding = defaultValueCoding
        self.defaultValueContactPoint = defaultValueContactPoint
        self.defaultValueDate = defaultValueDate
        self.defaultValueDateTime = defaultValueDateTime
        self.defaultValueDecimal = defaultValueDecimal
        self.defaultValueHumanName = defaultValueHumanName
        self.defaultValueId = defaultValueId
        self.defaultValueIdentifier = defaultValueIdentifier
        self.defaultValueInstant = defaultValueInstant
        self.defaultValueInteger = defaultValueInteger
        self.defaultValueMarkdown = defaultValueMarkdown
        self.defaultValueMeta = defaultValueMeta
        self.defaultValueOid = defaultValueOid
        self.defaultValuePeriod = defaultValuePeriod
        self.defaultValuePositiveInt = defaultValuePositiveInt
        self.defaultValueQuantity = defaultValueQuantity
        self.defaultValueRange = defaultValueRange
        self.defaultValueRatio = defaultValueRatio
        self.defaultValueReference = defaultValueReference
        self.defaultValueSampledData = defaultValueSampledData
        self.defaultValueSignature = defaultValueSignature
        self.defaultValueString = defaultValueString
        self.defaultValueTime = defaultValueTime
        self.defaultValueTiming = defaultValueTiming
        self.defaultValueUnsignedInt = defaultValueUnsignedInt
        self.defaultValueUri = defaultValueUri
        self.definition = definition
        self.exampleAddress = exampleAddress
        self.exampleAnnotation = exampleAnnotation
        self.exampleAttachment = exampleAttachment
        self.exampleBase64Binary = exampleBase64Binary
        self.exampleBoolean = exampleBoolean
        self.exampleCode = exampleCode
        self.exampleCodeableConcept = exampleCodeableConcept
        self.exampleCoding = exampleCoding
        self.exampleContactPoint = exampleContactPoint
        self.exampleDate = exampleDate
        self.exampleDateTime = exampleDateTime
        self.exampleDecimal = exampleDecimal
        self.exampleHumanName = exampleHumanName
        self.exampleId = exampleId
        self.exampleIdentifier = exampleIdentifier
        self.exampleInstant = exampleInstant
        self.exampleInteger = exampleInteger
        self.exampleMarkdown = exampleMarkdown
        self.exampleMeta = exampleMeta
        self.exampleOid = exampleOid
        self.examplePeriod = examplePeriod
        self.examplePositiveInt = examplePositiveInt
        self.exampleQuantity = exampleQuantity
        self.exampleRange = exampleRange
        self.exampleRatio = exampleRatio
        self.exampleReference = exampleReference
        self.exampleSampledData = exampleSampledData
        self.exampleSignature = exampleSignature
        self.exampleString = exampleString
        self.exampleTime = exampleTime
        self.exampleTiming = exampleTiming
        self.exampleUnsignedInt = exampleUnsignedInt
        self.exampleUri = exampleUri
        self.fixedAddress = fixedAddress
        self.fixedAnnotation = fixedAnnotation
        self.fixedAttachment = fixedAttachment
        self.fixedBase64Binary = fixedBase64Binary
        self.fixedBoolean = fixedBoolean
        self.fixedCode = fixedCode
        self.fixedCodeableConcept = fixedCodeableConcept
        self.fixedCoding = fixedCoding
        self.fixedContactPoint = fixedContactPoint
        self.fixedDate = fixedDate
        self.fixedDateTime = fixedDateTime
        self.fixedDecimal = fixedDecimal
        self.fixedHumanName = fixedHumanName
        self.fixedId = fixedId
        self.fixedIdentifier = fixedIdentifier
        self.fixedInstant = fixedInstant
        self.fixedInteger = fixedInteger
        self.fixedMarkdown = fixedMarkdown
        self.fixedMeta = fixedMeta
        self.fixedOid = fixedOid
        self.fixedPeriod = fixedPeriod
        self.fixedPositiveInt = fixedPositiveInt
        self.fixedQuantity = fixedQuantity
        self.fixedRange = fixedRange
        self.fixedRatio = fixedRatio
        self.fixedReference = fixedReference
        self.fixedSampledData = fixedSampledData
        self.fixedSignature = fixedSignature
        self.fixedString = fixedString
        self.fixedTime = fixedTime
        self.fixedTiming = fixedTiming
        self.fixedUnsignedInt = fixedUnsignedInt
        self.fixedUri = fixedUri
        self.isModifier = isModifier
        self.isSummary = isSummary
        self.label = label
        self.mapping = mapping
        self.max = max
        self.maxLength = maxLength
        self.maxValueAddress = maxValueAddress
        self.maxValueAnnotation = maxValueAnnotation
        self.maxValueAttachment = maxValueAttachment
        self.maxValueBase64Binary = maxValueBase64Binary
        self.maxValueBoolean = maxValueBoolean
        self.maxValueCode = maxValueCode
        self.maxValueCodeableConcept = maxValueCodeableConcept
        self.maxValueCoding = maxValueCoding
        self.maxValueContactPoint = maxValueContactPoint
        self.maxValueDate = maxValueDate
        self.maxValueDateTime = maxValueDateTime
        self.maxValueDecimal = maxValueDecimal
        self.maxValueHumanName = maxValueHumanName
        self.maxValueId = maxValueId
        self.maxValueIdentifier = maxValueIdentifier
        self.maxValueInstant = maxValueInstant
        self.maxValueInteger = maxValueInteger
        self.maxValueMarkdown = maxValueMarkdown
        self.maxValueMeta = maxValueMeta
        self.maxValueOid = maxValueOid
        self.maxValuePeriod = maxValuePeriod
        self.maxValuePositiveInt = maxValuePositiveInt
        self.maxValueQuantity = maxValueQuantity
        self.maxValueRange = maxValueRange
        self.maxValueRatio = maxValueRatio
        self.maxValueReference = maxValueReference
        self.maxValueSampledData = maxValueSampledData
        self.maxValueSignature = maxValueSignature
        self.maxValueString = maxValueString
        self.maxValueTime = maxValueTime
        self.maxValueTiming = maxValueTiming
        self.maxValueUnsignedInt = maxValueUnsignedInt
        self.maxValueUri = maxValueUri
        self.meaningWhenMissing = meaningWhenMissing
        self.min = min
        self.minValueAddress = minValueAddress
        self.minValueAnnotation = minValueAnnotation
        self.minValueAttachment = minValueAttachment
        self.minValueBase64Binary = minValueBase64Binary
        self.minValueBoolean = minValueBoolean
        self.minValueCode = minValueCode
        self.minValueCodeableConcept = minValueCodeableConcept
        self.minValueCoding = minValueCoding
        self.minValueContactPoint = minValueContactPoint
        self.minValueDate = minValueDate
        self.minValueDateTime = minValueDateTime
        self.minValueDecimal = minValueDecimal
        self.minValueHumanName = minValueHumanName
        self.minValueId = minValueId
        self.minValueIdentifier = minValueIdentifier
        self.minValueInstant = minValueInstant
        self.minValueInteger = minValueInteger
        self.minValueMarkdown = minValueMarkdown
        self.minValueMeta = minValueMeta
        self.minValueOid = minValueOid
        self.minValuePeriod = minValuePeriod
        self.minValuePositiveInt = minValuePositiveInt
        self.minValueQuantity = minValueQuantity
        self.minValueRange = minValueRange
        self.minValueRatio = minValueRatio
        self.minValueReference = minValueReference
        self.minValueSampledData = minValueSampledData
        self.minValueSignature = minValueSignature
        self.minValueString = minValueString
        self.minValueTime = minValueTime
        self.minValueTiming = minValueTiming
        self.minValueUnsignedInt = minValueUnsignedInt
        self.minValueUri = minValueUri
        self.mustSupport = mustSupport
        self.name = name
        self.nameReference = nameReference
        self.path = path
        self.patternAddress = patternAddress
        self.patternAnnotation = patternAnnotation
        self.patternAttachment = patternAttachment
        self.patternBase64Binary = patternBase64Binary
        self.patternBoolean = patternBoolean
        self.patternCode = patternCode
        self.patternCodeableConcept = patternCodeableConcept
        self.patternCoding = patternCoding
        self.patternContactPoint = patternContactPoint
        self.patternDate = patternDate
        self.patternDateTime = patternDateTime
        self.patternDecimal = patternDecimal
        self.patternHumanName = patternHumanName
        self.patternId = patternId
        self.patternIdentifier = patternIdentifier
        self.patternInstant = patternInstant
        self.patternInteger = patternInteger
        self.patternMarkdown = patternMarkdown
        self.patternMeta = patternMeta
        self.patternOid = patternOid
        self.patternPeriod = patternPeriod
        self.patternPositiveInt = patternPositiveInt
        self.patternQuantity = patternQuantity
        self.patternRange = patternRange
        self.patternRatio = patternRatio
        self.patternReference = patternReference
        self.patternSampledData = patternSampledData
        self.patternSignature = patternSignature
        self.patternString = patternString
        self.patternTime = patternTime
        self.patternTiming = patternTiming
        self.patternUnsignedInt = patternUnsignedInt
        self.patternUri = patternUri
        self.representation = representation
        self.requirements = requirements
        self.short = short
        self.slicing = slicing
        self.type = type

    def __repr__(self):
        return '<ElementDefinition %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ElementDefinitionBase(element.Element):
    """ Base definition information for tools.

    Information about the base definition of the element, provided to make it
    unncessary for tools to trace the deviation of the element through the
    derived and related profiles. This information is only provided where the
    element definition represents a constraint on another element definition,
    and must be present if there is a base element definition.
    """

    __tablename__ = "ElementDefinitionBase"

    max = Column(primitives.StringField)
    """ Max cardinality of the base element.
        Type `str`. """

    min = Column(Integer)
    """ Min cardinality of the base element.
        Type `int`. """

    path = Column(primitives.StringField)
    """ Path that identifies the base element.
        Type `str`. """

    def __init__(self, max, min, path,):
        """ Initialize all valid properties.
        """
        self.max = max
        self.min = min
        self.path = path

    def __repr__(self):
        return '<ElementDefinitionBase %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ElementDefinitionBinding(element.Element):
    """ ValueSet details if this is coded.

    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept).
    """

    __tablename__ = "ElementDefinitionBinding"

    description = Column(primitives.StringField)
    """ Human explanation of the value set.
        Type `str`. """

    strength = Column(primitives.StringField)
    """ required | extensible | preferred | example.
        Type `str`. """

    valueSetReference = Column(FHIRReference)
    """ Source of value set.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """

    valueSetUri = Column(primitives.StringField)
    """ Source of value set.
        Type `str`. """

    def __init__(self, description, strength, valueSetReference, valueSetUri,):
        """ Initialize all valid properties.
        """
        self.description = description
        self.strength = strength
        self.valueSetReference = valueSetReference
        self.valueSetUri = valueSetUri

    def __repr__(self):
        return '<ElementDefinitionBinding %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ElementDefinitionConstraint(element.Element):
    """ Condition that must evaluate to true.

    Formal constraints such as co-occurrence and other constraints that can be
    computationally evaluated within the context of the instance.
    """

    __tablename__ = "ElementDefinitionConstraint"

    human = Column(primitives.StringField)
    """ Human description of constraint.
        Type `str`. """

    key = Column(primitives.StringField)
    """ Target of 'condition' reference above.
        Type `str`. """

    requirements = Column(primitives.StringField)
    """ Why this constraint necessary or appropriate.
        Type `str`. """

    severity = Column(primitives.StringField)
    """ error | warning.
        Type `str`. """

    xpath = Column(primitives.StringField)
    """ XPath expression of constraint.
        Type `str`. """

    def __init__(self, human, key, requirements, severity, xpath,):
        """ Initialize all valid properties.
        """
        self.human = human
        self.key = key
        self.requirements = requirements
        self.severity = severity
        self.xpath = xpath

    def __repr__(self):
        return '<ElementDefinitionConstraint %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ElementDefinitionMapping(element.Element):
    """ Map element to another set of definitions.

    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """

    __tablename__ = "ElementDefinitionMapping"

    identity = Column(primitives.StringField)
    """ Reference to mapping declaration.
        Type `str`. """

    language = Column(primitives.StringField)
    """ Computable language of mapping.
        Type `str`. """

    map = Column(primitives.StringField)
    """ Details of the mapping.
        Type `str`. """

    def __init__(self, identity, language, map,):
        """ Initialize all valid properties.
        """
        self.identity = identity
        self.language = language
        self.map = map

    def __repr__(self):
        return '<ElementDefinitionMapping %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ElementDefinitionSlicing(element.Element):
    """ This element is sliced - slices follow.

    Indicates that the element is sliced into a set of alternative definitions
    (i.e. in a structure definition, there are multiple different constraints
    on a single element in the base resource). Slicing can be used in any
    resource that has cardinality ..* on the base resource, or any resource
    with a choice of types. The set of slices is any elements that come after
    this in the element sequence that have the same path, until a shorter path
    occurs (the shorter path terminates the set).
    """

    __tablename__ = "ElementDefinitionSlicing"

    description = Column(primitives.StringField)
    """ Text description of how slicing works (or not).
        Type `str`. """

    discriminator = Column(primitives.StringField)
    """ Element values that used to distinguish the slices.
        List of `str` items. """

    ordered = Column(bool)
    """ If elements must be in same order as slices.
        Type `bool`. """

    rules = Column(primitives.StringField)
    """ closed | open | openAtEnd.
        Type `str`. """

    def __init__(self, description, discriminator, ordered, rules,):
        """ Initialize all valid properties.
        """
        self.description = description
        self.discriminator = discriminator
        self.ordered = ordered
        self.rules = rules

    def __repr__(self):
        return '<ElementDefinitionSlicing %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ElementDefinitionType(element.Element):
    """ Data type and Profile for this element.

    The data type or resource that the value of this element is permitted to
    be.
    """

    __tablename__ = "ElementDefinitionType"

    aggregation = Column(primitives.StringField)
    """ contained | referenced | bundled - how aggregated.
        List of `str` items. """

    code = Column(primitives.StringField)
    """ Name of Data type or Resource.
        Type `str`. """

    profile = Column(primitives.StringField)
    """ Profile (StructureDefinition) to apply (or IG).
        List of `str` items. """

    def __init__(self, aggregation, code, profile,):
        """ Initialize all valid properties.
        """
        self.aggregation = aggregation
        self.code = code
        self.profile = profile

    def __repr__(self):
        return '<ElementDefinitionType %r>' % 'self.property'  # replace self.property


from . import address
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import meta
from . import period
from . import quantity
from . import range
from . import ratio
from . import sampleddata
from . import signature
from . import timing