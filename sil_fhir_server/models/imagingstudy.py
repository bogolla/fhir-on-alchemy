#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ImagingStudy)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class ImagingStudy(domainresource.DomainResource):
    """ A set of images produced in single study (one or more series of references
    images).

    Representation of the content produced in a DICOM imaging study. A study
    comprises a set of series, each of which includes a set of Service-Object
    Pair Instances (SOP Instances - images or other data) acquired or produced
    in a common context.  A series is of only one modality (e.g. X-ray, CT, MR,
    ultrasound), but a study may have multiple series of different modalities.
    """

    __tablename__ = "ImagingStudy"

    accession = Column(Identifier)
    """ Related workflow identifier ("Accession Number").
        Type `Identifier` (represented as `dict` in JSON). """

    availability = Column(primitives.StringField)
    """ ONLINE | OFFLINE | NEARLINE | UNAVAILABLE (0008,0056).
        Type `str`. """

    description = Column(primitives.StringField)
    """ Institution-generated description.
        Type `str`. """

    identifier = Column(Identifier)
    """ Other identifiers for the study.
        List of `Identifier` items (represented as `dict` in JSON). """

    interpreter = Column(FHIRReference)
    """ Who interpreted images.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    modalityList = Column(Coding)
    """ All series modality if actual acquisition modalities.
        List of `Coding` items (represented as `dict` in JSON). """

    numberOfInstances = Column(Integer)
    """ Number of Study Related Instances.
        Type `int`. """

    numberOfSeries = Column(Integer)
    """ Number of Study Related Series.
        Type `int`. """

    order = Column(FHIRReference)
    """ Order(s) that caused this study to be performed.
        List of `FHIRReference` items referencing `DiagnosticOrder` (represented as `dict` in JSON). """

    patient = Column(FHIRReference)
    """ Who the images are of.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    procedure = Column(FHIRReference)
    """ Type of procedure performed.
        List of `FHIRReference` items referencing `Procedure` (represented as `dict` in JSON). """

    referrer = Column(FHIRReference)
    """ Referring physician (0008,0090).
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    series = Column(ImagingStudySeries)
    """ Each study has one or more series of instances.
        List of `ImagingStudySeries` items (represented as `dict` in JSON). """

    started = Column(FHIRDate)
    """ When the study was started.
        Type `FHIRDate` (represented as `str` in JSON). """

    uid = Column(primitives.StringField)
    """ Formal identifier for the study.
        Type `str`. """

    url = Column(primitives.StringField)
    """ Retrieve URI.
        Type `str`. """

    def __init__(self, accession, availability, description, identifier, interpreter, modalityList, numberOfInstances, numberOfSeries, order, patient, procedure, referrer, series, started, uid, url,):
        """ Initialize all valid properties.
        """
        self.accession = accession
        self.availability = availability
        self.description = description
        self.identifier = identifier
        self.interpreter = interpreter
        self.modalityList = modalityList
        self.numberOfInstances = numberOfInstances
        self.numberOfSeries = numberOfSeries
        self.order = order
        self.patient = patient
        self.procedure = procedure
        self.referrer = referrer
        self.series = series
        self.started = started
        self.uid = uid
        self.url = url

    def __repr__(self):
        return '<ImagingStudy %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class ImagingStudySeries(backboneelement.BackboneElement):
    """ Each study has one or more series of instances.

    Each study has one or more series of images or other content.
    """

    __tablename__ = "ImagingStudySeries"

    availability = Column(primitives.StringField)
    """ ONLINE | OFFLINE | NEARLINE | UNAVAILABLE.
        Type `str`. """

    bodySite = Column(Coding)
    """ Body part examined.
        Type `Coding` (represented as `dict` in JSON). """

    description = Column(primitives.StringField)
    """ A description of the series.
        Type `str`. """

    instance = Column(ImagingStudySeriesInstance)
    """ A single SOP instance from the series.
        List of `ImagingStudySeriesInstance` items (represented as `dict` in JSON). """

    laterality = Column(Coding)
    """ Body part laterality.
        Type `Coding` (represented as `dict` in JSON). """

    modality = Column(Coding)
    """ The modality of the instances in the series.
        Type `Coding` (represented as `dict` in JSON). """

    number = Column(Integer)
    """ Numeric identifier of this series.
        Type `int`. """

    numberOfInstances = Column(Integer)
    """ Number of Series Related Instances.
        Type `int`. """

    started = Column(FHIRDate)
    """ When the series started.
        Type `FHIRDate` (represented as `str` in JSON). """

    uid = Column(primitives.StringField)
    """ Formal identifier for this series.
        Type `str`. """

    url = Column(primitives.StringField)
    """ Location of the referenced instance(s).
        Type `str`. """

    def __init__(self, availability, bodySite, description, instance, laterality, modality, number, numberOfInstances, started, uid, url,):
        """ Initialize all valid properties.
        """
        self.availability = availability
        self.bodySite = bodySite
        self.description = description
        self.instance = instance
        self.laterality = laterality
        self.modality = modality
        self.number = number
        self.numberOfInstances = numberOfInstances
        self.started = started
        self.uid = uid
        self.url = url

    def __repr__(self):
        return '<ImagingStudySeries %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class ImagingStudySeriesInstance(backboneelement.BackboneElement):
    """ A single SOP instance from the series.

    A single SOP Instance within the series, e.g. an image, or presentation
    state.
    """

    __tablename__ = "ImagingStudySeriesInstance"

    content = Column(Attachment)
    """ Content of the instance.
        List of `Attachment` items (represented as `dict` in JSON). """

    number = Column(Integer)
    """ The number of this instance in the series.
        Type `int`. """

    sopClass = Column(primitives.StringField)
    """ DICOM class type.
        Type `str`. """

    title = Column(primitives.StringField)
    """ Description of instance.
        Type `str`. """

    type = Column(primitives.StringField)
    """ Type of instance (image etc.).
        Type `str`. """

    uid = Column(primitives.StringField)
    """ Formal identifier for this instance.
        Type `str`. """

    def __init__(self, content, number, sopClass, title, type, uid,):
        """ Initialize all valid properties.
        """
        self.content = content
        self.number = number
        self.sopClass = sopClass
        self.title = title
        self.type = type
        self.uid = uid

    def __repr__(self):
        return '<ImagingStudySeriesInstance %r>' % 'self.property'  # replace self.property


from . import attachment
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier