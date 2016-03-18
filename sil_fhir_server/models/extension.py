#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Extension)
#  Date: 2016-03-18.


from . import element

class Extension(element.Element):
    """ None.

    Optional Extensions Element - found in all resources.
    """

    __tablename__ = "Extension"

    url = Column()
    """ identifies the meaning of the extension.
        Type `str`. """

    valueAddress = Column()
    """ Value of extension.
        Type `Address` (represented as `dict` in JSON). """

    valueAnnotation = Column()
    """ Value of extension.
        Type `Annotation` (represented as `dict` in JSON). """

    valueAttachment = Column()
    """ Value of extension.
        Type `Attachment` (represented as `dict` in JSON). """

    valueBase64Binary = Column()
    """ Value of extension.
        Type `str`. """

    valueBoolean = Column()
    """ Value of extension.
        Type `bool`. """

    valueCode = Column()
    """ Value of extension.
        Type `str`. """

    valueCodeableConcept = Column()
    """ Value of extension.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    valueCoding = Column()
    """ Value of extension.
        Type `Coding` (represented as `dict` in JSON). """

    valueContactPoint = Column()
    """ Value of extension.
        Type `ContactPoint` (represented as `dict` in JSON). """

    valueDate = Column()
    """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """

    valueDateTime = Column()
    """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """

    valueDecimal = Column()
    """ Value of extension.
        Type `float`. """

    valueHumanName = Column()
    """ Value of extension.
        Type `HumanName` (represented as `dict` in JSON). """

    valueId = Column()
    """ Value of extension.
        Type `str`. """

    valueIdentifier = Column()
    """ Value of extension.
        Type `Identifier` (represented as `dict` in JSON). """

    valueInstant = Column()
    """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """

    valueInteger = Column()
    """ Value of extension.
        Type `int`. """

    valueMarkdown = Column()
    """ Value of extension.
        Type `str`. """

    valueMeta = Column()
    """ Value of extension.
        Type `Meta` (represented as `dict` in JSON). """

    valueOid = Column()
    """ Value of extension.
        Type `str`. """

    valuePeriod = Column()
    """ Value of extension.
        Type `Period` (represented as `dict` in JSON). """

    valuePositiveInt = Column()
    """ Value of extension.
        Type `int`. """

    valueQuantity = Column()
    """ Value of extension.
        Type `Quantity` (represented as `dict` in JSON). """

    valueRange = Column()
    """ Value of extension.
        Type `Range` (represented as `dict` in JSON). """

    valueRatio = Column()
    """ Value of extension.
        Type `Ratio` (represented as `dict` in JSON). """

    valueReference = Column()
    """ Value of extension.
        Type `FHIRReference` (represented as `dict` in JSON). """

    valueSampledData = Column()
    """ Value of extension.
        Type `SampledData` (represented as `dict` in JSON). """

    valueSignature = Column()
    """ Value of extension.
        Type `Signature` (represented as `dict` in JSON). """

    valueString = Column()
    """ Value of extension.
        Type `str`. """

    valueTime = Column()
    """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """

    valueTiming = Column()
    """ Value of extension.
        Type `Timing` (represented as `dict` in JSON). """

    valueUnsignedInt = Column()
    """ Value of extension.
        Type `int`. """

    valueUri = Column()
    """ Value of extension.
        Type `str`. """

    def __init__(self, url, valueAddress, valueAnnotation, valueAttachment, valueBase64Binary, valueBoolean, valueCode, valueCodeableConcept, valueCoding, valueContactPoint, valueDate, valueDateTime, valueDecimal, valueHumanName, valueId, valueIdentifier, valueInstant, valueInteger, valueMarkdown, valueMeta, valueOid, valuePeriod, valuePositiveInt, valueQuantity, valueRange, valueRatio, valueReference, valueSampledData, valueSignature, valueString, valueTime, valueTiming, valueUnsignedInt, valueUri,):
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