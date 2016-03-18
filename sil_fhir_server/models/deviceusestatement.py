#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DeviceUseStatement)
#  Date: 2016-03-18.


from . import domainresource

class DeviceUseStatement(domainresource.DomainResource):
    """ None.

    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """

    __tablename__ = "DeviceUseStatement"

    bodySiteCodeableConcept = Column()
    """ Target body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    bodySiteReference = Column()
    """ Target body site.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """

    device = Column()
    """ None.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ None.
        List of `Identifier` items (represented as `dict` in JSON). """

    indication = Column(CodeableConcept)
    """ None.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    notes = Column(str)
    """ None.
        List of `str` items. """

    recordedOn = Column()
    """ None.
        Type `FHIRDate` (represented as `str` in JSON). """

    subject = Column()
    """ None.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    timingDateTime = Column()
    """ None.
        Type `FHIRDate` (represented as `str` in JSON). """

    timingPeriod = Column()
    """ None.
        Type `Period` (represented as `dict` in JSON). """

    timingTiming = Column()
    """ None.
        Type `Timing` (represented as `dict` in JSON). """

    whenUsed = Column()
    """ None.
        Type `Period` (represented as `dict` in JSON). """

    def __init__(self, bodySiteCodeableConcept, bodySiteReference, device, identifier, indication, notes, recordedOn, subject, timingDateTime, timingPeriod, timingTiming, whenUsed,):
        """ Initialize all valid properties.
        """
        self.bodySiteCodeableConcept = bodySiteCodeableConcept
        self.bodySiteReference = bodySiteReference
        self.device = device
        self.identifier = identifier
        self.indication = indication
        self.notes = notes
        self.recordedOn = recordedOn
        self.subject = subject
        self.timingDateTime = timingDateTime
        self.timingPeriod = timingPeriod
        self.timingTiming = timingTiming
        self.whenUsed = whenUsed

    def __repr__(self):
        return '<DeviceUseStatement %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import timing