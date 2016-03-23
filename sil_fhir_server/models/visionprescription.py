#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/VisionPrescription)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class VisionPrescriptionDispense(backboneelement.BackboneElement):
    """ Vision supply authorization.

    Deals with details of the dispense part of the supply specification.
    """

    __tablename__ = "VisionPrescriptionDispense"

    add = Column(primitives.DecimalField)
    """ Lens add.
        Type `float`. """

    axis = Column(primitives.IntegerField)
    """ Lens axis.
        Type `int`. """

    backCurve = Column(primitives.DecimalField)
    """ Contact lens back curvature.
        Type `float`. """

    base = Column(primitives.StringField)
    """ up | down | in | out.
        Type `str`. """

    brand = Column(primitives.StringField)
    """ Lens add.
        Type `str`. """

    color = Column(primitives.StringField)
    """ Lens add.
        Type `str`. """

    cylinder = Column(primitives.DecimalField)
    """ Lens cylinder.
        Type `float`. """

    diameter = Column(primitives.DecimalField)
    """ Contact lens diameter.
        Type `float`. """

    duration = Column(primitives.StringField,
                      ForeignKey('Quantity.id'))
    """ Lens wear duration.
        Type `Quantity` referencing `SimpleQuantity`
        (represented as `dict` in JSON). """

    eye = Column(primitives.StringField)
    """ right | left.
        Type `str`. """

    notes = Column(primitives.StringField)
    """ Notes for coatings.
        Type `str`. """

    power = Column(primitives.DecimalField)
    """ Contact lens power.
        Type `float`. """

    prism = Column(primitives.DecimalField)
    """ Lens prism.
        Type `float`. """

    product = Column(primitives.StringField,
                     ForeignKey('Coding.id'))
    """ Product to be supplied.
        Type `Coding` (represented as `dict` in JSON). """

    sphere = Column(primitives.DecimalField)
    """ Lens sphere.
        Type `float`. """

    def __init__(self, add, axis, backCurve, base, brand, color,
                 cylinder, diameter, duration, eye, notes, power,
                 prism, product, sphere,):
        """ Initialize all valid properties.
        """
        self.add = add
        self.axis = axis
        self.backCurve = backCurve
        self.base = base
        self.brand = brand
        self.color = color
        self.cylinder = cylinder
        self.diameter = diameter
        self.duration = duration
        self.eye = eye
        self.notes = notes
        self.power = power
        self.prism = prism
        self.product = product
        self.sphere = sphere

    def __repr__(self):
        return '<VisionPrescriptionDispense %r>' % 'self.property'  # replace self.property


class VisionPrescription(domainresource.DomainResource):
    """ Prescription for vision correction products for a patient.

    An authorization for the supply of glasses and/or contact lenses to a
    patient.
    """

    __tablename__ = "VisionPrescription"
    
    dateWritten = Column(primitives.DateField)
    """ When prescription was authorized.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    dispense = Column(primitives.StringField,
                      ForeignKey('VisionPrescriptionDispense.id'))
    """ Vision supply authorization.
        List of `VisionPrescriptionDispense` items (represented as `dict` in JSON). """
    
    # todo encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ Created during encounter / admission / stay.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    # todo patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    patient = Column(primitives.StringField)
    """ Who prescription is for.
        Type `FHIRReference` referencing `Patient`
        (represented as `dict` in JSON). """
    
    # todo prescriber = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    prescriber = Column(primitives.StringField)
    """ Who authorizes the vision product.
        Type `FHIRReference` referencing `Practitioner`
        (represented as `dict` in JSON). """
    
    reasonCodeableConcept = Column(primitives.StringField,
                                   ForeignKey('CodeableConcept.id'))
    """ Reason or indication for writing the prescription.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo reasonReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    reasonReference = Column(primitives.StringField)
    """ Reason or indication for writing the prescription.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """

    def __init__(self, dateWritten, dispense, encounter, identifier, patient,
                 prescriber, reasonCodeableConcept, reasonReference,):
        """ Initialize all valid properties.
        """
        self.dateWritten = dateWritten
        self.dispense = dispense
        self.encounter = encounter
        self.identifier = identifier
        self.patient = patient
        self.prescriber = prescriber
        self.reasonCodeableConcept = reasonCodeableConcept
        self.reasonReference = reasonReference

    def __repr__(self):
        return '<VisionPrescription %r>' % 'self.property'  # replace self.property
