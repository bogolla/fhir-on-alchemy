#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Parameters)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import resource

class Parameters(resource.Resource):
    """ Operation Request or Response.

    This special resource type is used to represent an operation request and
    response (operations.html). It has no other use, and there is no RESTful
    endpoint associated with it.
    """

    __tablename__ = "Parameters"

    parameter = Column(ParametersParameter)
    """ Operation Parameter.
        List of `ParametersParameter` items (represented as `dict` in JSON). """

    def __init__(self, parameter,):
        """ Initialize all valid properties.
        """
        self.parameter = parameter

    def __repr__(self):
        return '<Parameters %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class ParametersParameter(backboneelement.BackboneElement):
    """ Operation Parameter.

    A parameter passed to or received from the operation.
    """

    __tablename__ = "ParametersParameter"

    name = Column(primitives.StringField)
    """ Name from the definition.
        Type `str`. """

    part = Column(ParametersParameter)
    """ Named part of a parameter (e.g. Tuple).
        List of `ParametersParameter` items (represented as `dict` in JSON). """

    resource = Column(Resource)
    """ If parameter is a whole resource.
        Type `Resource` (represented as `dict` in JSON). """

    valueAddress = Column(Address)
    """ If parameter is a data type.
        Type `Address` (represented as `dict` in JSON). """

    valueAnnotation = Column(Annotation)
    """ If parameter is a data type.
        Type `Annotation` (represented as `dict` in JSON). """

    valueAttachment = Column(Attachment)
    """ If parameter is a data type.
        Type `Attachment` (represented as `dict` in JSON). """

    valueBase64Binary = Column(primitives.StringField)
    """ If parameter is a data type.
        Type `str`. """

    valueBoolean = Column(bool)
    """ If parameter is a data type.
        Type `bool`. """

    valueCode = Column(primitives.StringField)
    """ If parameter is a data type.
        Type `str`. """

    valueCodeableConcept = Column(CodeableConcept)
    """ If parameter is a data type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    valueCoding = Column(Coding)
    """ If parameter is a data type.
        Type `Coding` (represented as `dict` in JSON). """

    valueContactPoint = Column(ContactPoint)
    """ If parameter is a data type.
        Type `ContactPoint` (represented as `dict` in JSON). """

    valueDate = Column(FHIRDate)
    """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """

    valueDateTime = Column(FHIRDate)
    """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """

    valueDecimal = Column(float)
    """ If parameter is a data type.
        Type `float`. """

    valueHumanName = Column(HumanName)
    """ If parameter is a data type.
        Type `HumanName` (represented as `dict` in JSON). """

    valueId = Column(primitives.StringField)
    """ If parameter is a data type.
        Type `str`. """

    valueIdentifier = Column(Identifier)
    """ If parameter is a data type.
        Type `Identifier` (represented as `dict` in JSON). """

    valueInstant = Column(FHIRDate)
    """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """

    valueInteger = Column(Integer)
    """ If parameter is a data type.
        Type `int`. """

    valueMarkdown = Column(primitives.StringField)
    """ If parameter is a data type.
        Type `str`. """

    valueMeta = Column(Meta)
    """ If parameter is a data type.
        Type `Meta` (represented as `dict` in JSON). """

    valueOid = Column(primitives.StringField)
    """ If parameter is a data type.
        Type `str`. """

    valuePeriod = Column(Period)
    """ If parameter is a data type.
        Type `Period` (represented as `dict` in JSON). """

    valuePositiveInt = Column(Integer)
    """ If parameter is a data type.
        Type `int`. """

    valueQuantity = Column(Quantity)
    """ If parameter is a data type.
        Type `Quantity` (represented as `dict` in JSON). """

    valueRange = Column(Range)
    """ If parameter is a data type.
        Type `Range` (represented as `dict` in JSON). """

    valueRatio = Column(Ratio)
    """ If parameter is a data type.
        Type `Ratio` (represented as `dict` in JSON). """

    valueReference = Column(FHIRReference)
    """ If parameter is a data type.
        Type `FHIRReference` (represented as `dict` in JSON). """

    valueSampledData = Column(SampledData)
    """ If parameter is a data type.
        Type `SampledData` (represented as `dict` in JSON). """

    valueSignature = Column(Signature)
    """ If parameter is a data type.
        Type `Signature` (represented as `dict` in JSON). """

    valueString = Column(primitives.StringField)
    """ If parameter is a data type.
        Type `str`. """

    valueTime = Column(FHIRDate)
    """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """

    valueTiming = Column(Timing)
    """ If parameter is a data type.
        Type `Timing` (represented as `dict` in JSON). """

    valueUnsignedInt = Column(Integer)
    """ If parameter is a data type.
        Type `int`. """

    valueUri = Column(primitives.StringField)
    """ If parameter is a data type.
        Type `str`. """

    def __init__(self, name, part, resource, valueAddress, valueAnnotation, valueAttachment, valueBase64Binary, valueBoolean, valueCode, valueCodeableConcept, valueCoding, valueContactPoint, valueDate, valueDateTime, valueDecimal, valueHumanName, valueId, valueIdentifier, valueInstant, valueInteger, valueMarkdown, valueMeta, valueOid, valuePeriod, valuePositiveInt, valueQuantity, valueRange, valueRatio, valueReference, valueSampledData, valueSignature, valueString, valueTime, valueTiming, valueUnsignedInt, valueUri,):
        """ Initialize all valid properties.
        """
        self.name = name
        self.part = part
        self.resource = resource
        self.valueAddress = valueAddress
        self.valueAnnotation = valueAnnotation
        self.valueAttachment = valueAttachment
        self.valueBase64Binary = valueBase64Binary
        self.valueBoolean = valueBoolean
        self.valueCode = valueCode
        self.valueCodeableConcept = valueCodeableConcept
        self.valueCoding = valueCoding
        self.valueContactPoint = valueContactPoint
        self.valueDate = valueDate
        self.valueDateTime = valueDateTime
        self.valueDecimal = valueDecimal
        self.valueHumanName = valueHumanName
        self.valueId = valueId
        self.valueIdentifier = valueIdentifier
        self.valueInstant = valueInstant
        self.valueInteger = valueInteger
        self.valueMarkdown = valueMarkdown
        self.valueMeta = valueMeta
        self.valueOid = valueOid
        self.valuePeriod = valuePeriod
        self.valuePositiveInt = valuePositiveInt
        self.valueQuantity = valueQuantity
        self.valueRange = valueRange
        self.valueRatio = valueRatio
        self.valueReference = valueReference
        self.valueSampledData = valueSampledData
        self.valueSignature = valueSignature
        self.valueString = valueString
        self.valueTime = valueTime
        self.valueTiming = valueTiming
        self.valueUnsignedInt = valueUnsignedInt
        self.valueUri = valueUri

    def __repr__(self):
        return '<ParametersParameter %r>' % 'self.property'  # replace self.property


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