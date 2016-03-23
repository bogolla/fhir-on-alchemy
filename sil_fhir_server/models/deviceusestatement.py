#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DeviceUseStatement)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource

class DeviceUseStatement(domainresource.DomainResource):
    """ None.

    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """

    __tablename__ = "DeviceUseStatement"
    
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
    """ None.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ None.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    indication = Column(primitives.StringField,
                        ForeignKey('CodeableConcept.id'))
    """ None.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    notes = Column(primitives.StringField)
    """ None.
        List of `str` items. """
    
    recordedOn = Column(primitives.DateTimeField)
    """ None.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ None.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    timingDateTime = Column(primitives.DateTimeField)
    """ None.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    timingPeriod = Column(primitives.StringField,
                          ForeignKey('Period.id'))
    """ None.
        Type `Period` (represented as `dict` in JSON). """
    
    timingTiming = Column(primitives.StringField,
                          ForeignKey('Timing.id'))
    """ None.
        Type `Timing` (represented as `dict` in JSON). """
    
    whenUsed = Column(primitives.StringField,
                      ForeignKey('Period.id'))
    """ None.
        Type `Period` (represented as `dict` in JSON). """

    def __init__(self, bodySiteCodeableConcept, bodySiteReference,
                 device, identifier, indication, notes, recordedOn,
                 subject, timingDateTime, timingPeriod, timingTiming,
                 whenUsed):
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