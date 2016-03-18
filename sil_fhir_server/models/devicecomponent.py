#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DeviceComponent)
#  Date: 2016-03-18.


from . import domainresource

class DeviceComponent(domainresource.DomainResource):
    """ An instance of a medical-related component of a medical device.

    Describes the characteristics, operational status and capabilities of a
    medical-related component of a medical device.
    """

    __tablename__ = "DeviceComponent"

    identifier = Column()
    """ Instance id assigned by the software stack.
        Type `Identifier` (represented as `dict` in JSON). """

    languageCode = Column()
    """ Language code for the human-readable text strings produced by the
        device.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    lastSystemChange = Column()
    """ Recent system change timestamp.
        Type `FHIRDate` (represented as `str` in JSON). """

    measurementPrinciple = Column()
    """ other | chemical | electrical | impedance | nuclear | optical |
        thermal | biological | mechanical | acoustical | manual+.
        Type `str`. """

    operationalStatus = Column(CodeableConcept)
    """ Component operational status.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    parameterGroup = Column()
    """ Current supported parameter group.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    parent = Column()
    """ Parent resource link.
        Type `FHIRReference` referencing `DeviceComponent` (represented as `dict` in JSON). """

    productionSpecification = Column(DeviceComponentProductionSpecification)
    """ Production specification of the component.
        List of `DeviceComponentProductionSpecification` items (represented as `dict` in JSON). """

    source = Column()
    """ A source device of this component.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """

    type = Column()
    """ What kind of component it is.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, identifier, languageCode, lastSystemChange, measurementPrinciple, operationalStatus, parameterGroup, parent, productionSpecification, source, type,):
        """ Initialize all valid properties.
        """
        self.identifier = identifier
        self.languageCode = languageCode
        self.lastSystemChange = lastSystemChange
        self.measurementPrinciple = measurementPrinciple
        self.operationalStatus = operationalStatus
        self.parameterGroup = parameterGroup
        self.parent = parent
        self.productionSpecification = productionSpecification
        self.source = source
        self.type = type

    def __repr__(self):
        return '<DeviceComponent %r>' % 'self.property'  # replace self.property


from . import backboneelement

class DeviceComponentProductionSpecification(backboneelement.BackboneElement):
    """ Production specification of the component.

    Describes the production specification such as component revision, serial
    number, etc.
    """

    __tablename__ = "DeviceComponentProductionSpecification"

    componentId = Column()
    """ Internal component unique identification.
        Type `Identifier` (represented as `dict` in JSON). """

    productionSpec = Column()
    """ A printable string defining the component.
        Type `str`. """

    specType = Column()
    """ Specification type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, componentId, productionSpec, specType,):
        """ Initialize all valid properties.
        """
        self.componentId = componentId
        self.productionSpec = productionSpec
        self.specType = specType

    def __repr__(self):
        return '<DeviceComponentProductionSpecification %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier