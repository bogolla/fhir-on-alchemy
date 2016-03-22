#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DeviceUseRequest)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class DeviceUseRequest(domainresource.DomainResource):
    """ A request for a patient to use or be given a medical device.

    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """

    __tablename__ = "DeviceUseRequest"

    bodySiteCodeableConcept = Column(CodeableConcept)
    """ Target body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    bodySiteReference = Column(FHIRReference)
    """ Target body site.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """

    device = Column(FHIRReference)
    """ Device requested.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """

    encounter = Column(FHIRReference)
    """ Encounter motivating request.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Request identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    indication = Column(CodeableConcept)
    """ Reason for request.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    notes = Column(primitives.StringField)
    """ Notes or comments.
        List of `str` items. """

    orderedOn = Column(FHIRDate)
    """ When ordered.
        Type `FHIRDate` (represented as `str` in JSON). """

    priority = Column(primitives.StringField)
    """ routine | urgent | stat | asap.
        Type `str`. """

    prnReason = Column(CodeableConcept)
    """ PRN.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    recordedOn = Column(FHIRDate)
    """ When recorded.
        Type `FHIRDate` (represented as `str` in JSON). """

    status = Column(primitives.StringField)
    """ proposed | planned | requested | received | accepted | in-progress
        | completed | suspended | rejected | aborted.
        Type `str`. """

    subject = Column(FHIRReference)
    """ Focus of request.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    timingDateTime = Column(FHIRDate)
    """ Schedule for use.
        Type `FHIRDate` (represented as `str` in JSON). """

    timingPeriod = Column(Period)
    """ Schedule for use.
        Type `Period` (represented as `dict` in JSON). """

    timingTiming = Column(Timing)
    """ Schedule for use.
        Type `Timing` (represented as `dict` in JSON). """

    def __init__(self, bodySiteCodeableConcept, bodySiteReference, device, encounter, identifier, indication, notes, orderedOn, priority, prnReason, recordedOn, status, subject, timingDateTime, timingPeriod, timingTiming,):
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


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import timing