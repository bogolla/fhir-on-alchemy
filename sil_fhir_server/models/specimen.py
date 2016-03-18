#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Specimen)
#  Date: 2016-03-18.


from . import domainresource

class Specimen(domainresource.DomainResource):
    """ Sample for analysis.

    A sample to be used for analysis.
    """

    __tablename__ = "Specimen"

    accessionIdentifier = Column()
    """ Identifier assigned by the lab.
        Type `Identifier` (represented as `dict` in JSON). """

    collection = Column()
    """ Collection details.
        Type `SpecimenCollection` (represented as `dict` in JSON). """

    container = Column(SpecimenContainer)
    """ Direct container of specimen (tube/slide, etc.).
        List of `SpecimenContainer` items (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ External Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    parent = Column(FHIRReference)
    """ Specimen from which this specimen originated.
        List of `FHIRReference` items referencing `Specimen` (represented as `dict` in JSON). """

    receivedTime = Column()
    """ The time when specimen was received for processing.
        Type `FHIRDate` (represented as `str` in JSON). """

    status = Column()
    """ available | unavailable | unsatisfactory | entered-in-error.
        Type `str`. """

    subject = Column()
    """ Where the specimen came from. This may be from the patient(s) or
        from the environment or a device.
        Type `FHIRReference` referencing `Patient, Group, Device, Substance` (represented as `dict` in JSON). """

    treatment = Column(SpecimenTreatment)
    """ Treatment and processing step details.
        List of `SpecimenTreatment` items (represented as `dict` in JSON). """

    type = Column()
    """ Kind of material that forms the specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, accessionIdentifier, collection, container, identifier, parent, receivedTime, status, subject, treatment, type,):
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


from . import backboneelement

class SpecimenCollection(backboneelement.BackboneElement):
    """ Collection details.

    Details concerning the specimen collection.
    """

    __tablename__ = "SpecimenCollection"

    bodySite = Column()
    """ Anatomical collection site.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    collectedDateTime = Column()
    """ Collection time.
        Type `FHIRDate` (represented as `str` in JSON). """

    collectedPeriod = Column()
    """ Collection time.
        Type `Period` (represented as `dict` in JSON). """

    collector = Column()
    """ Who collected the specimen.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    comment = Column(str)
    """ Collector comments.
        List of `str` items. """

    method = Column()
    """ Technique used to perform collection.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    quantity = Column()
    """ The quantity of specimen collected.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    def __init__(self, bodySite, collectedDateTime, collectedPeriod, collector, comment, method, quantity,):
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

    additiveCodeableConcept = Column()
    """ Additive associated with container.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    additiveReference = Column()
    """ Additive associated with container.
        Type `FHIRReference` referencing `Substance` (represented as `dict` in JSON). """

    capacity = Column()
    """ Container volume or size.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    description = Column()
    """ Textual description of the container.
        Type `str`. """

    identifier = Column(Identifier)
    """ Id for the container.
        List of `Identifier` items (represented as `dict` in JSON). """

    specimenQuantity = Column()
    """ Quantity of specimen within container.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    type = Column()
    """ Kind of container directly associated with specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, additiveCodeableConcept, additiveReference, capacity, description, identifier, specimenQuantity, type,):
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

    additive = Column(FHIRReference)
    """ Material used in the processing step.
        List of `FHIRReference` items referencing `Substance` (represented as `dict` in JSON). """

    description = Column()
    """ Textual description of procedure.
        Type `str`. """

    procedure = Column()
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


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity