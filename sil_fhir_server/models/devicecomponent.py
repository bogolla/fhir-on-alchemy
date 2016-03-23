#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DeviceComponent)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class DeviceComponentProductionSpecification(backboneelement.BackboneElement):
    """ Production specification of the component.

    Describes the production specification such as component revision, serial
    number, etc.
    """

    __tablename__ = "DeviceComponentProductionSpecification"

    componentId = Column(primitives.StringField,
                         ForeignKey('Identifier.id'))
    """ Internal component unique identification.
        Type `Identifier` (represented as `dict` in JSON). """

    productionSpec = Column(primitives.StringField)
    """ A printable string defining the component.
        Type `str`. """

    specType = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
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


class DeviceComponent(domainresource.DomainResource):
    """ An instance of a medical-related component of a medical device.

    Describes the characteristics, operational status and capabilities of a
    medical-related component of a medical device.
    """

    __tablename__ = "DeviceComponent"
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Instance id assigned by the software stack.
        Type `Identifier` (represented as `dict` in JSON). """
    
    languageCode = Column(primitives.StringField,
                          ForeignKey('CodeableConcept.id'))
    """ Language code for the human-readable text strings produced by the
        device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    lastSystemChange = Column(primitives.DateTimeField)
    """ Recent system change timestamp.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    measurementPrinciple = Column(primitives.StringField)
    """ other | chemical | electrical | impedance | nuclear | optical |
        thermal | biological | mechanical | acoustical | manual+.
        Type `str`. """
    
    operationalStatus = Column(primitives.StringField,
                               ForeignKey('CodeableConcept.id'))
    """ Component operational status.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    parameterGroup = Column(primitives.StringField,
                            ForeignKey('CodeableConcept.id'))
    """ Current supported parameter group.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo parent = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    parent = Column(primitives.StringField)
    """ Parent resource link.
        Type `FHIRReference` referencing `DeviceComponent`
        (represented as `dict` in JSON). """
    
    productionSpecification = Column(primitives.StringField,
                                     ForeignKey(
                                         'DeviceComponentProductionSpecification.id'))
    """ Production specification of the component.
        List of `DeviceComponentProductionSpecification` items
        (represented as `dict` in JSON). """
    
    # todo source = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    source = Column(primitives.StringField)
    """ A source device of this component.
        Type `FHIRReference` referencing `Device`
        (represented as `dict` in JSON). """
    
    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ What kind of component it is.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, identifier, languageCode, lastSystemChange,
                 measurementPrinciple, operationalStatus,
                 parameterGroup, parent, productionSpecification,
                 source, type,):
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
