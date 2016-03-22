#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/VisionPrescription)
#  Date: 2016-03-18.


from sqlalchemy import Column
from sil_fhir_server.data_types import primitives
from . import domainresource

class VisionPrescription(domainresource.DomainResource):
    """ Prescription for vision correction products for a patient.

    An authorization for the supply of glasses and/or contact lenses to a
    patient.
    """

    __tablename__ = "VisionPrescription"

    dateWritten = Column(FHIRDate)
    """ When prescription was authorized.
        Type `FHIRDate` (represented as `str` in JSON). """

    dispense = Column(VisionPrescriptionDispense)
    """ Vision supply authorization.
        List of `VisionPrescriptionDispense` items (represented as `dict` in JSON). """

    encounter = Column(FHIRReference)
    """ Created during encounter / admission / stay.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    patient = Column(FHIRReference)
    """ Who prescription is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    prescriber = Column(FHIRReference)
    """ Who authorizes the vision product.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    reasonCodeableConcept = Column(CodeableConcept)
    """ Reason or indication for writing the prescription.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    reasonReference = Column(FHIRReference)
    """ Reason or indication for writing the prescription.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """

    def __init__(self, dateWritten, dispense, encounter, identifier, patient, prescriber, reasonCodeableConcept, reasonReference,):
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


from sqlalchemy import Column, Integer, String
from . import backboneelement

class VisionPrescriptionDispense(backboneelement.BackboneElement):
    """ Vision supply authorization.

    Deals with details of the dispense part of the supply specification.
    """

    __tablename__ = "VisionPrescriptionDispense"

    add = Column(float)
    """ Lens add.
        Type `float`. """

    axis = Column(Integer)
    """ Lens axis.
        Type `int`. """

    backCurve = Column(float)
    """ Contact lens back curvature.
        Type `float`. """

    base = Column(primitives.StringFieldField)
    """ up | down | in | out.
        Type `str`. """

    brand = Column(primitives.StringFieldField)
    """ Lens add.
        Type `str`. """

    color = Column(primitives.StringFieldField)
    """ Lens add.
        Type `str`. """

    cylinder = Column(float)
    """ Lens cylinder.
        Type `float`. """

    diameter = Column(float)
    """ Contact lens diameter.
        Type `float`. """

    duration = Column(Quantity)
    """ Lens wear duration.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    eye = Column(primitives.StringFieldField)
    """ right | left.
        Type `str`. """

    notes = Column(primitives.StringFieldField)
    """ Notes for coatings.
        Type `str`. """

    power = Column(float)
    """ Contact lens power.
        Type `float`. """

    prism = Column(float)
    """ Lens prism.
        Type `float`. """

    product = Column(Coding)
    """ Product to be supplied.
        Type `Coding` (represented as `dict` in JSON). """

    sphere = Column(float)
    """ Lens sphere.
        Type `float`. """

    def __init__(self, add, axis, backCurve, base, brand, color, cylinder, diameter, duration, eye, notes, power, prism, product, sphere,):
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


from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity