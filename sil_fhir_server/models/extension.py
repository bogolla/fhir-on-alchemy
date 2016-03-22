#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Extension)
#  Date: 2016-03-18.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import element


class Extension(element.Element):
    """ None.

    Optional Extensions Element - found in all resources.
    """

    __tablename__ = "Extension"

    url = Column(primitives.StringField)
    """ identifies the meaning of the extension.
        Type `str`. """

    valueAddress = Column(primitives.StringField,
                          ForeignKey('Address.id'))
    """ Value of extension.
        Type `Address` (represented as `dict` in JSON). """

    valueAnnotation = Column(primitives.StringField,
                             ForeignKey('Annotation.id'))
    """ Value of extension.
        Type `Annotation` (represented as `dict` in JSON). """

    valueAttachment = Column(primitives.StringField,
                             ForeignKey('Attachment.id'))
    """ Value of extension.
        Type `Attachment` (represented as `dict` in JSON). """

    valueBase64Binary = Column(primitives.StringField)
    """ Value of extension.
        Type `str`. """

    valueBoolean = Column(primitives.DecimalField)
    """ Value of extension.
        Type `bool`. """

    valueCode = Column(primitives.StringField)
    """ Value of extension.
        Type `str`. """

    valueCodeableConcept = Column(primitives.StringField,
                                  ForeignKey('CodeableConcept.id'))
    """ Value of extension.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    valueCoding = Column(primitives.StringField,
                         ForeignKey('Coding.id'))
    """ Value of extension.
        Type `Coding` (represented as `dict` in JSON). """

    valueContactPoint = Column(primitives.StringField,
                               ForeignKey('ContactPoint.id'))
    """ Value of extension.
        Type `ContactPoint` (represented as `dict` in JSON). """

    valueDate = Column(primitives.DateTimeField)
    """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """

    valueDateTime = Column(primitives.DateTimeField)
    """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """

    valueDecimal = Column(primitives.DecimalField)
    """ Value of extension.
        Type `float`. """

    valueHumanName = Column(primitives.StringField,
                            ForeignKey('HumanName.id'))
    """ Value of extension.
        Type `HumanName` (represented as `dict` in JSON). """

    valueId = Column(primitives.StringField)
    """ Value of extension.
        Type `str`. """

    valueIdentifier = Column(primitives.StringField,
                             ForeignKey('Identifier.id'))
    """ Value of extension.
        Type `Identifier` (represented as `dict` in JSON). """

    valueInstant = Column(primitives.InstantField)
    """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """

    valueInteger = Column(primitives.IntegerField)
    """ Value of extension.
        Type `int`. """

    valueMarkdown = Column(primitives.StringField)
    """ Value of extension.
        Type `str`. """

    # valueMeta = Column(Meta)
    """ Value of extension.
        Type `Meta` (represented as `dict` in JSON). """

    valueOid = Column(primitives.StringField)
    """ Value of extension.
        Type `str`. """

    valuePeriod = Column(primitives.StringField,
                         ForeignKey('Period.id'))
    """ Value of extension.
        Type `Period` (represented as `dict` in JSON). """

    valuePositiveInt = Column(primitives.IntegerField)
    """ Value of extension.
        Type `int`. """

    valueQuantity = Column(primitives.StringField,
                           ForeignKey('Quantity.id'))
    """ Value of extension.
        Type `Quantity` (represented as `dict` in JSON). """

    valueRange = Column(primitives.StringField,
                        ForeignKey('Range.id'))
    """ Value of extension.
        Type `Range` (represented as `dict` in JSON). """

    valueRatio = Column(primitives.StringField,
                        ForeignKey('Ratio.id'))
    """ Value of extension.
        Type `Ratio` (represented as `dict` in JSON). """

    valueReference = Column(primitives.StringField,
                            ForeignKey('FHIRReference.id'))
    """ Value of extension.
        Type `FHIRReference` (represented as `dict` in JSON). """

    valueSampledData = Column(primitives.StringField,
                              ForeignKey('SampledData.id'))
    """ Value of extension.
        Type `SampledData` (represented as `dict` in JSON). """

    valueSignature = Column(primitives.StringField,
                            ForeignKey('Signature.id'))
    """ Value of extension.
        Type `Signature` (represented as `dict` in JSON). """

    valueString = Column(primitives.StringField)
    """ Value of extension.
        Type `str`. """

    valueTime = Column(primitives.TimeField)
    """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """

    valueTiming = Column(primitives.StringField,
                         ForeignKey('Timing.id'))
    """ Value of extension.
        Type `Timing` (represented as `dict` in JSON). """

    valueUnsignedInt = Column(primitives.IntegerField)
    """ Value of extension.
        Type `int`. """

    valueUri = Column(primitives.StringField)
    """ Value of extension.
        Type `str`. """

    def __init__(self, url, valueAddress, valueAnnotation,
                 valueAttachment, valueBase64Binary, valueBoolean,
                 valueCode, valueCodeableConcept, valueCoding,
                 valueContactPoint, valueDate, valueDateTime,
                 valueDecimal, valueHumanName, valueId,
                 valueIdentifier, valueInstant, valueInteger,
                 valueMarkdown, valueMeta, valueOid, valuePeriod,
                 valuePositiveInt, valueQuantity, valueRange,
                 valueRatio, valueReference, valueSampledData,
                 valueSignature, valueString, valueTime, valueTiming,
                 valueUnsignedInt, valueUri,):
        """ Initialize all valid properties.
        """
        self.url = url
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
        return '<Extension %r>' % 'self.property'  # replace self.property
