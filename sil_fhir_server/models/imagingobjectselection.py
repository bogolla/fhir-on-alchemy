#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ImagingObjectSelection)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class ImagingObjectSelectionStudySeriesInstanceFrames(backboneelement.BackboneElement):
    """ The frame set.

    Identity and location information of the frames in the selected instance.
    """

    __tablename__ = "ImagingObjectSelectionStudySeriesInstanceFrames"

    frameNumbers = Column(primitives.IntegerField)
    """ Frame numbers.
        List of `int` items. """

    url = Column(primitives.StringField)
    """ Retrieve frame URL.
        Type `str`. """

    def __init__(self, frameNumbers, url,):
        """ Initialize all valid properties.
        """
        self.frameNumbers = frameNumbers
        self.url = url

    def __repr__(self):
        return '<ImagingObjectSelectionStudySeriesInstanceFrames %r>' % 'self.property'  # replace self.property


class ImagingObjectSelectionStudySeriesInstance(backboneelement.BackboneElement):
    """ The selected instance.

    Identity and locating information of the selected DICOM SOP instances.
    """

    __tablename__ = "ImagingObjectSelectionStudySeriesInstance"

    frames = Column(primitives.StringField,
                    ForeignKey(
                        'ImagingObjectSelectionStudySeriesInstanceFrames.id'))
    """ The frame set.
        List of `ImagingObjectSelectionStudySeriesInstanceFrames` items (represented as `dict` in JSON). """

    sopClass = Column(primitives.StringField)
    """ SOP class UID of instance.
        Type `str`. """

    uid = Column(primitives.StringField)
    """ Selected instance UID.
        Type `str`. """

    url = Column(primitives.StringField)
    """ Retrieve instance URL.
        Type `str`. """

    def __init__(self, frames, sopClass, uid, url,):
        """ Initialize all valid properties.
        """
        self.frames = frames
        self.sopClass = sopClass
        self.uid = uid
        self.url = url

    def __repr__(self):
        return '<ImagingObjectSelectionStudySeriesInstance %r>' % 'self.property'  # replace self.property


class ImagingObjectSelectionStudy(backboneelement.BackboneElement):
    """ Study identity of the selected instances.

    Study identity and locating information of the DICOM SOP instances in the
    selection.
    """

    __tablename__ = "ImagingObjectSelectionStudy"

    # todo imagingStudy = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    imagingStudy = Column(primitives.StringField)
    """ Reference to ImagingStudy.
        Type `FHIRReference` referencing `ImagingStudy` (represented as `dict` in JSON). """

    series = Column(primitives.StringField,
                    ForeignKey(
                        'ImagingObjectSelectionStudySeries.id'))
    """ Series identity of the selected instances.
        List of `ImagingObjectSelectionStudySeries` items (represented as `dict` in JSON). """

    uid = Column(primitives.StringField)
    """ Study instance UID.
        Type `str`. """

    url = Column(primitives.StringField)
    """ Retrieve study URL.
        Type `str`. """

    def __init__(self, imagingStudy, series, uid, url,):
        """ Initialize all valid properties.
        """
        self.imagingStudy = imagingStudy
        self.series = series
        self.uid = uid
        self.url = url

    def __repr__(self):
        return '<ImagingObjectSelectionStudy %r>' % 'self.property'  # replace self.property


class ImagingObjectSelectionStudySeries(backboneelement.BackboneElement):
    """ Series identity of the selected instances.

    Series identity and locating information of the DICOM SOP instances in the
    selection.
    """

    __tablename__ = "ImagingObjectSelectionStudySeries"

    instance = Column(primitives.StringField,
                      ForeignKey(
                          'ImagingObjectSelectionStudySeriesInstance.id'))
    """ The selected instance.
        List of `ImagingObjectSelectionStudySeriesInstance` items
        (represented as `dict` in JSON). """

    uid = Column(primitives.StringField)
    """ Series instance UID.
        Type `str`. """

    url = Column(primitives.StringField)
    """ Retrieve series URL.
        Type `str`. """

    def __init__(self, instance, uid, url,):
        """ Initialize all valid properties.
        """
        self.instance = instance
        self.uid = uid
        self.url = url

    def __repr__(self):
        return '<ImagingObjectSelectionStudySeries %r>' % 'self.property'  # replace self.property


class ImagingObjectSelection(domainresource.DomainResource):
    """ Key Object Selection.

    A manifest of a set of DICOM Service-Object Pair Instances (SOP Instances).
    The referenced SOP Instances (images or other content) are for a single
    patient, and may be from one or more studies. The referenced SOP Instances
    have been selected for a purpose, such as quality assurance, conference, or
    consult. Reflecting that range of purposes, typical ImagingObjectSelection
    resources may include all SOP Instances in a study (perhaps for sharing
    through a Health Information Exchange); key images from multiple studies
    (for reference by a referring or treating physician); a multi-frame
    ultrasound instance ("cine" video clip) and a set of measurements taken
    from that instance (for inclusion in a teaching file); and so on.
    """

    __tablename__ = "ImagingObjectSelection"
    
    # todo author = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    author = Column(primitives.StringField)
    """ Author (human or machine).
        Type `FHIRReference` referencing `Practitioner, Device,
        Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
    
    authoringTime = Column(primitives.DateTimeField)
    """ Authoring time of the selection.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    description = Column(primitives.StringField)
    """ Description text.
        Type `str`. """
    
    # todo patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    patient = Column(primitives.StringField)
    """ Patient of the selected objects.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    study = Column(primitives.StringField,
                   ForeignKey(
                       'ImagingObjectSelectionStudy.id'))
    """ Study identity of the selected instances.
        List of `ImagingObjectSelectionStudy` items (represented as `dict` in JSON). """
    
    title = Column(primitives.StringField,
                   ForeignKey('CodeableConcept.id'))
    """ Reason for selection.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    uid = Column(primitives.StringField)
    """ Instance UID.
        Type `str`. """

    def __init__(self, author, authoringTime, description,
                 patient, study, title, uid,):
        """ Initialize all valid properties.
        """
        self.author = author
        self.authoringTime = authoringTime
        self.description = description
        self.patient = patient
        self.study = study
        self.title = title
        self.uid = uid

    def __repr__(self):
        return '<ImagingObjectSelection %r>' % 'self.property'  # replace self.property
