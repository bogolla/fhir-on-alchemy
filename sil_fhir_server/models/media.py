#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Media)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource

class Media(domainresource.DomainResource):
    """ A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """

    __tablename__ = "Media"
    
    content = Column(primitives.StringField,
                     ForeignKey('Attachment.id'))
    """ Actual Media - reference or data.
        Type `Attachment` (represented as `dict` in JSON). """
    
    deviceName = Column(primitives.StringField)
    """ Name of the device/manufacturer.
        Type `str`. """
    
    duration = Column(primitives.IntegerField)
    """ Length in seconds (audio / video).
        Type `int`. """
    
    frames = Column(primitives.IntegerField)
    """ Number of frames if > 1 (photo).
        Type `int`. """
    
    height = Column(primitives.IntegerField)
    """ Height of the image in pixels (photo/video).
        Type `int`. """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Identifier(s) for the image.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    # todo operator = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    operator = Column(primitives.StringField)
    """ The person who generated the image.
        Type `FHIRReference` referencing `Practitioner`
        (represented as `dict` in JSON). """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Who/What this Media is a record of.
        Type `FHIRReference` referencing `Patient, Practitioner,
        Group, Device, Specimen` (represented as `dict` in JSON). """
    
    subtype = Column(primitives.StringField,
                     ForeignKey('CodeableConcept.id'))
    """ The type of acquisition equipment/process.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    type = Column(primitives.StringField)
    """ photo | video | audio.
        Type `str`. """
    
    view = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Imaging view, e.g. Lateral or Antero-posterior.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    width = Column(primitives.IntegerField)
    """ Width of the image in pixels (photo/video).
        Type `int`. """

    def __init__(self, content, deviceName, duration, frames, height,
                 identifier, operator, subject, subtype, type, view,
                 width,):
        """ Initialize all valid properties.
        """
        self.content = content
        self.deviceName = deviceName
        self.duration = duration
        self.frames = frames
        self.height = height
        self.identifier = identifier
        self.operator = operator
        self.subject = subject
        self.subtype = subtype
        self.type = type
        self.view = view
        self.width = width

    def __repr__(self):
        return '<Media %r>' % 'self.property'  # replace self.property