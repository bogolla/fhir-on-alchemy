#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ImagingObjectSelection)
#  Date: 2016-03-18.


from . import domainresource

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

    author = Column()
    """ Author (human or machine).
        Type `FHIRReference` referencing `Practitioner, Device, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """

    authoringTime = Column()
    """ Authoring time of the selection.
        Type `FHIRDate` (represented as `str` in JSON). """

    description = Column()
    """ Description text.
        Type `str`. """

    patient = Column()
    """ Patient of the selected objects.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    study = Column(ImagingObjectSelectionStudy)
    """ Study identity of the selected instances.
        List of `ImagingObjectSelectionStudy` items (represented as `dict` in JSON). """

    title = Column()
    """ Reason for selection.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    uid = Column()
    """ Instance UID.
        Type `str`. """

    def __init__(self, author, authoringTime, description, patient, study, title, uid,):
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


from . import backboneelement

class ImagingObjectSelectionStudy(backboneelement.BackboneElement):
    """ Study identity of the selected instances.

    Study identity and locating information of the DICOM SOP instances in the
    selection.
    """

    __tablename__ = "ImagingObjectSelectionStudy"

    imagingStudy = Column()
    """ Reference to ImagingStudy.
        Type `FHIRReference` referencing `ImagingStudy` (represented as `dict` in JSON). """

    series = Column(ImagingObjectSelectionStudySeries)
    """ Series identity of the selected instances.
        List of `ImagingObjectSelectionStudySeries` items (represented as `dict` in JSON). """

    uid = Column()
    """ Study instance UID.
        Type `str`. """

    url = Column()
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

    instance = Column(ImagingObjectSelectionStudySeriesInstance)
    """ The selected instance.
        List of `ImagingObjectSelectionStudySeriesInstance` items (represented as `dict` in JSON). """

    uid = Column()
    """ Series instance UID.
        Type `str`. """

    url = Column()
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


class ImagingObjectSelectionStudySeriesInstance(backboneelement.BackboneElement):
    """ The selected instance.

    Identity and locating information of the selected DICOM SOP instances.
    """

    __tablename__ = "ImagingObjectSelectionStudySeriesInstance"

    frames = Column(ImagingObjectSelectionStudySeriesInstanceFrames)
    """ The frame set.
        List of `ImagingObjectSelectionStudySeriesInstanceFrames` items (represented as `dict` in JSON). """

    sopClass = Column()
    """ SOP class UID of instance.
        Type `str`. """

    uid = Column()
    """ Selected instance UID.
        Type `str`. """

    url = Column()
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


class ImagingObjectSelectionStudySeriesInstanceFrames(backboneelement.BackboneElement):
    """ The frame set.

    Identity and location information of the frames in the selected instance.
    """

    __tablename__ = "ImagingObjectSelectionStudySeriesInstanceFrames"

    frameNumbers = Column(int)
    """ Frame numbers.
        List of `int` items. """

    url = Column()
    """ Retrieve frame URL.
        Type `str`. """

    def __init__(self, frameNumbers, url,):
        """ Initialize all valid properties.
        """
        self.frameNumbers = frameNumbers
        self.url = url

    def __repr__(self):
        return '<ImagingObjectSelectionStudySeriesInstanceFrames %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference