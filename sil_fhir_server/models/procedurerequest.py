#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ProcedureRequest)
#  Date: 2016-03-18.


from . import domainresource

class ProcedureRequest(domainresource.DomainResource):
    """ A request for a procedure to be performed.

    A request for a procedure to be performed. May be a proposal or an order.
    """

    __tablename__ = "ProcedureRequest"

    asNeededBoolean = Column()
    """ Preconditions for procedure.
        Type `bool`. """

    asNeededCodeableConcept = Column()
    """ Preconditions for procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    bodySite = Column(CodeableConcept)
    """ What part of body to perform on.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    code = Column()
    """ What procedure to perform.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    encounter = Column()
    """ Encounter request created during.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Unique identifier for the request.
        List of `Identifier` items (represented as `dict` in JSON). """

    notes = Column(Annotation)
    """ Additional information about desired procedure.
        List of `Annotation` items (represented as `dict` in JSON). """

    orderedOn = Column()
    """ When request was created.
        Type `FHIRDate` (represented as `str` in JSON). """

    orderer = Column()
    """ Who made request.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson, Device` (represented as `dict` in JSON). """

    performer = Column()
    """ Who should perform the procedure.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """

    priority = Column()
    """ routine | urgent | stat | asap.
        Type `str`. """

    reasonCodeableConcept = Column()
    """ Why procedure should occur.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    reasonReference = Column()
    """ Why procedure should occur.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """

    scheduledDateTime = Column()
    """ When procedure should occur.
        Type `FHIRDate` (represented as `str` in JSON). """

    scheduledPeriod = Column()
    """ When procedure should occur.
        Type `Period` (represented as `dict` in JSON). """

    scheduledTiming = Column()
    """ When procedure should occur.
        Type `Timing` (represented as `dict` in JSON). """

    status = Column()
    """ proposed | draft | requested | received | accepted | in-progress |
        completed | suspended | rejected | aborted.
        Type `str`. """

    subject = Column()
    """ Who the procedure should be done to.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """

    def __init__(self, asNeededBoolean, asNeededCodeableConcept, bodySite, code, encounter, identifier, notes, orderedOn, orderer, performer, priority, reasonCodeableConcept, reasonReference, scheduledDateTime, scheduledPeriod, scheduledTiming, status, subject,):
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


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import timing