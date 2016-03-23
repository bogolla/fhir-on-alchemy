#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Specimen)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class SpecimenCollection(backboneelement.BackboneElement):
    """ Collection details.

    Details concerning the specimen collection.
    """

    __tablename__ = "SpecimenCollection"

    bodySite = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Anatomical collection site.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    collectedDateTime = Column(primitives.DateTimeField)
    """ Collection time.
        Type `FHIRDate` (represented as `str` in JSON). """

    collectedPeriod = Column(primitives.StringField,
                             ForeignKey('Period.id'))
    """ Collection time.
        Type `Period` (represented as `dict` in JSON). """

    # todo collector = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    collector = Column(primitives.StringField)
    """ Who collected the specimen.
        Type `FHIRReference` referencing `Practitioner`
        (represented as `dict` in JSON). """

    comment = Column(primitives.StringField)
    """ Collector comments.
        List of `str` items. """

    method = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ Technique used to perform collection.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    quantity = Column(primitives.StringField,
                      ForeignKey('Quantity.id'))
    """ The quantity of specimen collected.
        Type `Quantity` referencing `SimpleQuantity`
        (represented as `dict` in JSON). """

    def __init__(self, bodySite, collectedDateTime, collectedPeriod,
                 collector, comment, method, quantity,):
        """ Initialize all valid properties.
        """
        self.bodySite = bodySite
        self.collectedDateTime = collectedDateTime
        self.collectedPeriod = collectedPeriod
        self.collector = collector
        self.comment = comment
        self.method = method
        self.quantity = quantity

    def __repr__(self):
        return '<SpecimenCollection %r>' % 'self.property'  # replace self.property


class SpecimenContainer(backboneelement.BackboneElement):
    """ Direct container of specimen (tube/slide, etc.).

    The container holding the specimen.  The recursive nature of containers;
    i.e. blood in tube in tray in rack is not addressed here.
    """

    __tablename__ = "SpecimenContainer"

    additiveCodeableConcept = Column(primitives.StringField,
                                     ForeignKey('CodeableConcept.id'))
    """ Additive associated with container.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    # todo additiveReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    additiveReference = Column(primitives.StringField)
    """ Additive associated with container.
        Type `FHIRReference` referencing `Substance` (represented as `dict` in JSON). """

    capacity = Column(primitives.StringField,
                      ForeignKey('Quantity.id'))
    """ Container volume or size.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    description = Column(primitives.StringField)
    """ Textual description of the container.
        Type `str`. """

    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Id for the container.
        List of `Identifier` items (represented as `dict` in JSON). """

    specimenQuantity = Column(primitives.StringField,
                              ForeignKey('Quantity.id'))
    """ Quantity of specimen within container.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Kind of container directly associated with specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, additiveCodeableConcept, additiveReference, capacity,
                 description, identifier, specimenQuantity, type,):
        """ Initialize all valid properties.
        """
        self.additiveCodeableConcept = additiveCodeableConcept
        self.additiveReference = additiveReference
        self.capacity = capacity
        self.description = description
        self.identifier = identifier
        self.specimenQuantity = specimenQuantity
        self.type = type

    def __repr__(self):
        return '<SpecimenContainer %r>' % 'self.property'  # replace self.property


class SpecimenTreatment(backboneelement.BackboneElement):
    """ Treatment and processing step details.

    Details concerning treatment and processing steps for the specimen.
    """

    __tablename__ = "SpecimenTreatment"

    # todo additive = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    additive = Column(primitives.StringField)
    """ Material used in the processing step.
        List of `FHIRReference` items referencing `Substance` (represented as `dict` in JSON). """

    description = Column(primitives.StringField)
    """ Textual description of procedure.
        Type `str`. """

    procedure = Column(primitives.StringField,
                       ForeignKey('CodeableConcept.id'))
    """ Indicates the treatment or processing step  applied to the specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, additive, description, procedure,):
        """ Initialize all valid properties.
        """
        self.additive = additive
        self.description = description
        self.procedure = procedure

    def __repr__(self):
        return '<SpecimenTreatment %r>' % 'self.property'  # replace self.property


class Specimen(domainresource.DomainResource):
    """ Sample for analysis.

    A sample to be used for analysis.
    """

    __tablename__ = "Specimen"
    
    accessionIdentifier = Column(primitives.StringField,
                                 ForeignKey('Identifier.id'))
    """ Identifier assigned by the lab.
        Type `Identifier` (represented as `dict` in JSON). """
    
    collection = Column(primitives.StringField,
                        ForeignKey('SpecimenCollection.id'))
    """ Collection details.
        Type `SpecimenCollection` (represented as `dict` in JSON). """
    
    container = Column(primitives.StringField,
                       ForeignKey('SpecimenContainer.id'))
    """ Direct container of specimen (tube/slide, etc.).
        List of `SpecimenContainer` items (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ External Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    # todo parent = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    parent = Column(primitives.StringField)
    """ Specimen from which this specimen originated.
        List of `FHIRReference` items referencing `Specimen` (represented as `dict` in JSON). """
    
    receivedTime = Column(primitives.DateTimeField)
    """ The time when specimen was received for processing.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    status = Column(primitives.StringField)
    """ available | unavailable | unsatisfactory | entered-in-error.
        Type `str`. """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Where the specimen came from. This may be from the patient(s) or
        from the environment or a device.
        Type `FHIRReference` referencing `Patient, Group, Device,
        Substance` (represented as `dict` in JSON). """
    
    treatment = Column(primitives.StringField, ForeignKey('SpecimenTreatment.id'))
    """ Treatment and processing step details.
        List of `SpecimenTreatment` items (represented as `dict` in JSON). """
    
    type = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ Kind of material that forms the specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, accessionIdentifier, collection, container, identifier,
                 parent, receivedTime, status, subject, treatment, type,):
        """ Initialize all valid properties.
        """
        self.accessionIdentifier = accessionIdentifier
        self.collection = collection
        self.container = container
        self.identifier = identifier
        self.parent = parent
        self.receivedTime = receivedTime
        self.status = status
        self.subject = subject
        self.treatment = treatment
        self.type = type

    def __repr__(self):
        return '<Specimen %r>' % 'self.property'  # replace self.property
