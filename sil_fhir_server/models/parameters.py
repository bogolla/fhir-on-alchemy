#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Parameters)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import resource

class Parameters(resource.Resource):
    """ Operation Request or Response.

    This special resource type is used to represent an operation request and
    response (operations.html). It has no other use, and there is no RESTful
    endpoint associated with it.
    """

    __tablename__ = "Parameters"
    
    parameter = Column(primitives.StringField, ForeignKey('ParametersParameter.id'))
    """ Operation Parameter.
        List of `ParametersParameter` items (represented as `dict` in JSON). """

    def __init__(self, parameter,):
        """ Initialize all valid properties.
        """
        self.parameter = parameter

    def __repr__(self):
        return '<Parameters %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import backboneelement

class ParametersParameter(backboneelement.BackboneElement):
    """ Operation Parameter.

    A parameter passed to or received from the operation.
    """

    __tablename__ = "ParametersParameter"
    
    name = Column(primitives.StringField)
    """ Name from the definition.
        Type `str`. """
    
    part = Column(primitives.StringField, ForeignKey('ParametersParameter.id'))
    """ Named part of a parameter (e.g. Tuple).
        List of `ParametersParameter` items (represented as `dict` in JSON). """
    
    resource = Column(primitives.StringField, ForeignKey('Resource.id'))
    """ If parameter is a whole resource.
        Type `Resource` (represented as `dict` in JSON). """
    
    valueAddress = Column(primitives.StringField, ForeignKey('Address.id'))
    """ If parameter is a data type.
        Type `Address` (represented as `dict` in JSON). """
    
    valueAnnotation = Column(primitives.StringField, ForeignKey('Annotation.id'))
    """ If parameter is a data type.
        Type `Annotation` (represented as `dict` in JSON). """
    
    valueAttachment = Column(primitives.StringField, ForeignKey('Attachment.id'))
    """ If parameter is a data type.
        Type `Attachment` (represented as `dict` in JSON). """
    
    valueBase64Binary = Column(primitives.StringField)
    """ If parameter is a data type.
        Type `str`. """
    
    valueBoolean = Column(primitives.BooleanField)
    """ If parameter is a data type.
        Type `bool`. """
    
    valueCode = Column(primitives.StringField)
    """ If parameter is a data type.
        Type `str`. """
    
    valueCodeableConcept = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ If parameter is a data type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    valueCoding = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ If parameter is a data type.
        Type `Coding` (represented as `dict` in JSON). """
    
    valueContactPoint = Column(primitives.StringField, ForeignKey('ContactPoint.id'))
    """ If parameter is a data type.
        Type `ContactPoint` (represented as `dict` in JSON). """
    
    valueDate = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    valueDateTime = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    valueDecimal = Column(primitives.DecimalField)
    """ If parameter is a data type.
        Type `float`. """
    
    valueHumanName = Column(primitives.StringField, ForeignKey('HumanName.id'))
    """ If parameter is a data type.
        Type `HumanName` (represented as `dict` in JSON). """
    
    valueId = Column(primitives.StringField)
    """ If parameter is a data type.
        Type `str`. """
    
    valueIdentifier = Column(primitives.StringField, ForeignKey('Identifier.id'))
    """ If parameter is a data type.
        Type `Identifier` (represented as `dict` in JSON). """
    
    valueInstant = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    valueInteger = Column(primitives.IntegerField)
    """ If parameter is a data type.
        Type `int`. """
    
    valueMarkdown = Column(primitives.StringField)
    """ If parameter is a data type.
        Type `str`. """
    
    valueMeta = Column(primitives.StringField, ForeignKey('Meta.id'))
    """ If parameter is a data type.
        Type `Meta` (represented as `dict` in JSON). """
    
    valueOid = Column(primitives.StringField)
    """ If parameter is a data type.
        Type `str`. """
    
    valuePeriod = Column(primitives.StringField, ForeignKey('Period.id'))
    """ If parameter is a data type.
        Type `Period` (represented as `dict` in JSON). """
    
    valuePositiveInt = Column(primitives.IntegerField)
    """ If parameter is a data type.
        Type `int`. """
    
    valueQuantity = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ If parameter is a data type.
        Type `Quantity` (represented as `dict` in JSON). """
    
    valueRange = Column(primitives.StringField, ForeignKey('Range.id'))
    """ If parameter is a data type.
        Type `Range` (represented as `dict` in JSON). """
    
    valueRatio = Column(primitives.StringField, ForeignKey('Ratio.id'))
    """ If parameter is a data type.
        Type `Ratio` (represented as `dict` in JSON). """
    
    valueReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ If parameter is a data type.
        Type `FHIRReference` (represented as `dict` in JSON). """
    
    valueSampledData = Column(primitives.StringField, ForeignKey('SampledData.id'))
    """ If parameter is a data type.
        Type `SampledData` (represented as `dict` in JSON). """
    
    valueSignature = Column(primitives.StringField, ForeignKey('Signature.id'))
    """ If parameter is a data type.
        Type `Signature` (represented as `dict` in JSON). """
    
    valueString = Column(primitives.StringField)
    """ If parameter is a data type.
        Type `str`. """
    
    valueTime = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    valueTiming = Column(primitives.StringField, ForeignKey('Timing.id'))
    """ If parameter is a data type.
        Type `Timing` (represented as `dict` in JSON). """
    
    valueUnsignedInt = Column(primitives.IntegerField)
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