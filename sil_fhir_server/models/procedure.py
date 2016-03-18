#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Procedure)
#  Date: 2016-03-18.


from . import domainresource

class Procedure(domainresource.DomainResource):
    """ An action that is being or was performed on a patient.

    An action that is or was performed on a patient. This can be a physical
    intervention like an operation, or less invasive like counseling or
    hypnotherapy.
    """

    __tablename__ = "Procedure"

    bodySite = Column(CodeableConcept)
    """ Target body sites.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    category = Column()
    """ Classification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    code = Column()
    """ Identification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    complication = Column(CodeableConcept)
    """ Complication following the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    encounter = Column()
    """ The encounter associated with the procedure.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    focalDevice = Column(ProcedureFocalDevice)
    """ Device changed in procedure.
        List of `ProcedureFocalDevice` items (represented as `dict` in JSON). """

    followUp = Column(CodeableConcept)
    """ Instructions for follow up.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ External Identifiers for this procedure.
        List of `Identifier` items (represented as `dict` in JSON). """

    location = Column()
    """ Where the procedure happened.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """

    notPerformed = Column()
    """ True if procedure was not performed as scheduled.
        Type `bool`. """

    notes = Column(Annotation)
    """ Additional information about the procedure.
        List of `Annotation` items (represented as `dict` in JSON). """

    outcome = Column()
    """ The result of procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    performedDateTime = Column()
    """ Date/Period the procedure was performed.
        Type `FHIRDate` (represented as `str` in JSON). """

    performedPeriod = Column()
    """ Date/Period the procedure was performed.
        Type `Period` (represented as `dict` in JSON). """

    performer = Column(ProcedurePerformer)
    """ The people who performed the procedure.
        List of `ProcedurePerformer` items (represented as `dict` in JSON). """

    reasonCodeableConcept = Column()
    """ Reason procedure performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    reasonNotPerformed = Column(CodeableConcept)
    """ Reason procedure was not performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    reasonReference = Column()
    """ Reason procedure performed.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """

    report = Column(FHIRReference)
    """ Any report resulting from the procedure.
        List of `FHIRReference` items referencing `DiagnosticReport` (represented as `dict` in JSON). """

    request = Column()
    """ A request for this procedure.
        Type `FHIRReference` referencing `CarePlan, DiagnosticOrder, ProcedureRequest, ReferralRequest` (represented as `dict` in JSON). """

    status = Column()
    """ in-progress | aborted | completed | entered-in-error.
        Type `str`. """

    subject = Column()
    """ Who the procedure was performed on.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """

    used = Column(FHIRReference)
    """ Items used during procedure.
        List of `FHIRReference` items referencing `Device, Medication, Substance` (represented as `dict` in JSON). """

    def __init__(self, bodySite, category, code, complication, encounter, focalDevice, followUp, identifier, location, notPerformed, notes, outcome, performedDateTime, performedPeriod, performer, reasonCodeableConcept, reasonNotPerformed, reasonReference, report, request, status, subject, used,):
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


from . import backboneelement

class ProcedureFocalDevice(backboneelement.BackboneElement):
    """ Device changed in procedure.

    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """

    __tablename__ = "ProcedureFocalDevice"

    action = Column()
    """ Kind of change to device.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    manipulated = Column()
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

    actor = Column()
    """ The reference to the practitioner.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """

    role = Column()
    """ The role the actor was in.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, actor, role,):
        """ Initialize all valid properties.
        """
        self.actor = actor
        self.role = role

    def __repr__(self):
        return '<ProcedurePerformer %r>' % 'self.property'  # replace self.property


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period