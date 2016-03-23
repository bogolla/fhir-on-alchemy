#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Procedure)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class ProcedureFocalDevice(backboneelement.BackboneElement):
    """ Device changed in procedure.

    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """

    __tablename__ = "ProcedureFocalDevice"

    action = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ Kind of change to device.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    # todo manipulated = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    manipulated = Column(primitives.StringField)
    """ Device that was changed.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """

    def __init__(self, action, manipulated,):
        """ Initialize all valid properties.
        """
        self.action = action
        self.manipulated = manipulated

    def __repr__(self):
        return '<ProcedureFocalDevice %r>' % 'self.property'  # replace self.property


class ProcedurePerformer(backboneelement.BackboneElement):
    """ The people who performed the procedure.

    Limited to 'real' people rather than equipment.
    """

    __tablename__ = "ProcedurePerformer"

    # todo actor = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    actor = Column(primitives.StringField)
    """ The reference to the practitioner.
        Type `FHIRReference` referencing `Practitioner, Organization,
        Patient, RelatedPerson` (represented as `dict` in JSON). """

    role = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ The role the actor was in.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, actor, role,):
        """ Initialize all valid properties.
        """
        self.actor = actor
        self.role = role

    def __repr__(self):
        return '<ProcedurePerformer %r>' % 'self.property'  # replace self.property


class Procedure(domainresource.DomainResource):
    """ An action that is being or was performed on a patient.

    An action that is or was performed on a patient. This can be a physical
    intervention like an operation, or less invasive like counseling or
    hypnotherapy.
    """

    __tablename__ = "Procedure"
    
    bodySite = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Target body sites.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    category = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Classification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Identification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    complication = Column(primitives.StringField,
                          ForeignKey('CodeableConcept.id'))
    """ Complication following the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    # todo encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ The encounter associated with the procedure.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
    
    focalDevice = Column(primitives.StringField,
                         ForeignKey('ProcedureFocalDevice.id'))
    """ Device changed in procedure.
        List of `ProcedureFocalDevice` items (represented as `dict` in JSON). """
    
    followUp = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Instructions for follow up.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ External Identifiers for this procedure.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    # todo location = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    location = Column(primitives.StringField)
    """ Where the procedure happened.
        Type `FHIRReference` referencing `Location`
        (represented as `dict` in JSON). """
    
    notPerformed = Column(primitives.BooleanField)
    """ True if procedure was not performed as scheduled.
        Type `bool`. """
    
    notes = Column(primitives.StringField,
                   ForeignKey('Annotation.id'))
    """ Additional information about the procedure.
        List of `Annotation` items (represented as `dict` in JSON). """
    
    outcome = Column(primitives.StringField,
                     ForeignKey('CodeableConcept.id'))
    """ The result of procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    performedDateTime = Column(primitives.DateTimeField)
    """ Date/Period the procedure was performed.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    performedPeriod = Column(primitives.StringField,
                             ForeignKey('Period.id'))
    """ Date/Period the procedure was performed.
        Type `Period` (represented as `dict` in JSON). """
    
    performer = Column(primitives.StringField,
                       ForeignKey('ProcedurePerformer.id'))
    """ The people who performed the procedure.
        List of `ProcedurePerformer` items (represented as `dict` in JSON). """
    
    reasonCodeableConcept = Column(primitives.StringField,
                                   ForeignKey('CodeableConcept.id'))
    """ Reason procedure performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    reasonNotPerformed = Column(primitives.StringField,
                                ForeignKey('CodeableConcept.id'))
    """ Reason procedure was not performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    # todo reasonReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    reasonReference = Column(primitives.StringField)
    """ Reason procedure performed.
        Type `FHIRReference` referencing `Condition`
        (represented as `dict` in JSON). """
    
    # todo report = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    report = Column(primitives.StringField)
    """ Any report resulting from the procedure.
        List of `FHIRReference` items referencing `DiagnosticReport`
        (represented as `dict` in JSON). """
    
    # todo request = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    request = Column(primitives.StringField)
    """ A request for this procedure.
        Type `FHIRReference` referencing `CarePlan, DiagnosticOrder,
        ProcedureRequest, ReferralRequest` (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ in-progress | aborted | completed | entered-in-error.
        Type `str`. """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Who the procedure was performed on.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
    
    # todo used = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    used = Column(primitives.StringField)
    """ Items used during procedure.
        List of `FHIRReference` items referencing `Device, Medication, Substance`
        (represented as `dict` in JSON). """

    def __init__(self, bodySite, category, code, complication, encounter,
                 focalDevice, followUp, identifier, location, notPerformed,
                 notes, outcome, performedDateTime, performedPeriod,
                 performer, reasonCodeableConcept, reasonNotPerformed,
                 reasonReference, report, request, status, subject, used,):
        """ Initialize all valid properties.
        """
        self.bodySite = bodySite
        self.category = category
        self.code = code
        self.complication = complication
        self.encounter = encounter
        self.focalDevice = focalDevice
        self.followUp = followUp
        self.identifier = identifier
        self.location = location
        self.notPerformed = notPerformed
        self.notes = notes
        self.outcome = outcome
        self.performedDateTime = performedDateTime
        self.performedPeriod = performedPeriod
        self.performer = performer
        self.reasonCodeableConcept = reasonCodeableConcept
        self.reasonNotPerformed = reasonNotPerformed
        self.reasonReference = reasonReference
        self.report = report
        self.request = request
        self.status = status
        self.subject = subject
        self.used = used

    def __repr__(self):
        return '<Procedure %r>' % 'self.property'  # replace self.property
