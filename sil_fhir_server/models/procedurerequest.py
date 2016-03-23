#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ProcedureRequest)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource

class ProcedureRequest(domainresource.DomainResource):
    """ A request for a procedure to be performed.

    A request for a procedure to be performed. May be a proposal or an order.
    """

    __tablename__ = "ProcedureRequest"
    
    asNeededBoolean = Column(primitives.BooleanField)
    """ Preconditions for procedure.
        Type `bool`. """
    
    asNeededCodeableConcept = Column(primitives.StringField,
                                     ForeignKey('CodeableConcept.id'))
    """ Preconditions for procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    bodySite = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ What part of body to perform on.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ What procedure to perform.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ Encounter request created during.
        Type `FHIRReference` referencing `Encounter`
        (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Unique identifier for the request.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    notes = Column(primitives.StringField,
                   ForeignKey('Annotation.id'))
    """ Additional information about desired procedure.
        List of `Annotation` items (represented as `dict` in JSON). """
    
    orderedOn = Column(primitives.DateTimeField)
    """ When request was created.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    # todo orderer = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    orderer = Column(primitives.StringField)
    """ Who made request.
        Type `FHIRReference` referencing `Practitioner, Patient,
        RelatedPerson, Device` (represented as `dict` in JSON). """
    
    # todo performer = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    performer = Column(primitives.StringField)
    """ Who should perform the procedure.
        Type `FHIRReference` referencing `Practitioner, Organization,
        Patient, RelatedPerson` (represented as `dict` in JSON). """
    
    priority = Column(primitives.StringField)
    """ routine | urgent | stat | asap.
        Type `str`. """
    
    reasonCodeableConcept = Column(primitives.StringField,
                                   ForeignKey('CodeableConcept.id'))
    """ Why procedure should occur.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    # todo reasonReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    reasonReference = Column(primitives.StringField)
    """ Why procedure should occur.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """
    
    scheduledDateTime = Column(primitives.DateTimeField)
    """ When procedure should occur.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    scheduledPeriod = Column(primitives.StringField,
                             ForeignKey('Period.id'))
    """ When procedure should occur.
        Type `Period` (represented as `dict` in JSON). """
    
    scheduledTiming = Column(primitives.StringField,
                             ForeignKey('Timing.id'))
    """ When procedure should occur.
        Type `Timing` (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ proposed | draft | requested | received | accepted | in-progress |
        completed | suspended | rejected | aborted.
        Type `str`. """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Who the procedure should be done to.
        Type `FHIRReference` referencing `Patient, Group`
        (represented as `dict` in JSON). """

    def __init__(self, asNeededBoolean, asNeededCodeableConcept, bodySite,
                 code, encounter, identifier, notes, orderedOn, orderer,
                 performer, priority, reasonCodeableConcept, reasonReference,
                 scheduledDateTime, scheduledPeriod, scheduledTiming, status, subject,):
        """ Initialize all valid properties.
        """
        self.asNeededBoolean = asNeededBoolean
        self.asNeededCodeableConcept = asNeededCodeableConcept
        self.bodySite = bodySite
        self.code = code
        self.encounter = encounter
        self.identifier = identifier
        self.notes = notes
        self.orderedOn = orderedOn
        self.orderer = orderer
        self.performer = performer
        self.priority = priority
        self.reasonCodeableConcept = reasonCodeableConcept
        self.reasonReference = reasonReference
        self.scheduledDateTime = scheduledDateTime
        self.scheduledPeriod = scheduledPeriod
        self.scheduledTiming = scheduledTiming
        self.status = status
        self.subject = subject

    def __repr__(self):
        return '<ProcedureRequest %r>' % 'self.property'  # replace self.property