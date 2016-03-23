#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DeviceUseRequest)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource


class DeviceUseRequest(domainresource.DomainResource):
    """ A request for a patient to use or be given a medical device.

    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """

    __tablename__ = "DeviceUseRequest"
    
    bodySiteCodeableConcept = Column(primitives.StringField,
                                     ForeignKey('CodeableConcept.id'))
    """ Target body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo bodySiteReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    bodySiteReference = Column(primitives.StringField)
    """ Target body site.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """
    
    # todo device = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    device = Column(primitives.StringField)
    """ Device requested.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
    
    # todo encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ Encounter motivating request.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Request identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    indication = Column(primitives.StringField,
                        ForeignKey('CodeableConcept.id'))
    """ Reason for request.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    notes = Column(primitives.StringField)
    """ Notes or comments.
        List of `str` items. """
    
    orderedOn = Column(primitives.DateTimeField)
    """ When ordered.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    priority = Column(primitives.StringField)
    """ routine | urgent | stat | asap.
        Type `str`. """
    
    prnReason = Column(primitives.StringField,
                       ForeignKey('CodeableConcept.id'))
    """ PRN.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    recordedOn = Column(primitives.DateTimeField)
    """ When recorded.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    status = Column(primitives.StringField)
    """ proposed | planned | requested | received | accepted | in-progress
        | completed | suspended | rejected | aborted.
        Type `str`. """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Focus of request.
        Type `FHIRReference` referencing `Patient`
        (represented as `dict` in JSON). """
    
    timingDateTime = Column(primitives.DateTimeField)
    """ Schedule for use.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    timingPeriod = Column(primitives.StringField,
                          ForeignKey('Period.id'))
    """ Schedule for use.
        Type `Period` (represented as `dict` in JSON). """
    
    timingTiming = Column(primitives.StringField,
                          ForeignKey('Timing.id'))
    """ Schedule for use.
        Type `Timing` (represented as `dict` in JSON). """

    def __init__(self, bodySiteCodeableConcept, bodySiteReference,
                 device, encounter, identifier, indication, notes,
                 orderedOn, priority, prnReason, recordedOn, status,
                 subject, timingDateTime, timingPeriod, timingTiming):
        """ Initialize all valid properties.
        """
        self.bodySiteCodeableConcept = bodySiteCodeableConcept
        self.bodySiteReference = bodySiteReference
        self.device = device
        self.encounter = encounter
        self.identifier = identifier
        self.indication = indication
        self.notes = notes
        self.orderedOn = orderedOn
        self.priority = priority
        self.prnReason = prnReason
        self.recordedOn = recordedOn
        self.status = status
        self.subject = subject
        self.timingDateTime = timingDateTime
        self.timingPeriod = timingPeriod
        self.timingTiming = timingTiming

    def __repr__(self):
        return '<DeviceUseRequest %r>' % 'self.property'  # replace self.property
