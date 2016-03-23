#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DiagnosticOrder)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class DiagnosticOrderEvent(backboneelement.BackboneElement):
    """ A list of events of interest in the lifecycle.

    A summary of the events of interest that have occurred as the request is
    processed; e.g. when the order was made, various processing steps
    (specimens received), when it was completed.
    """

    __tablename__ = "DiagnosticOrderEvent"

    # todo actor = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    actor = Column(primitives.StringField)
    """ Who recorded or did this.
        Type `FHIRReference` referencing `Practitioner, Device`
        (represented as `dict` in JSON). """

    dateTime = Column(primitives.DateTimeField)
    """ The date at which the event happened.
        Type `FHIRDate` (represented as `str` in JSON). """

    description = Column(primitives.StringField,
                         ForeignKey('CodeableConcept.id'))
    """ More information about the event and its context.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ proposed | draft | planned | requested | received | accepted | in-
        progress | review | completed | cancelled | suspended | rejected |
        failed.
        Type `str`. """

    def __init__(self, actor, dateTime, description, status,):
        """ Initialize all valid properties.
        """
        self.actor = actor
        self.dateTime = dateTime
        self.description = description
        self.status = status

    def __repr__(self):
        return '<DiagnosticOrderEvent %r>' % 'self.property'  # replace self.property


class DiagnosticOrderItem(backboneelement.BackboneElement):
    """ The items the orderer requested.

    The specific diagnostic investigations that are requested as part of this
    request. Sometimes, there can only be one item per request, but in most
    contexts, more than one investigation can be requested.
    """

    __tablename__ = "DiagnosticOrderItem"

    bodySite = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Location of requested test (if applicable).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Code to indicate the item (test or panel) being ordered.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    event = Column(primitives.StringField,
                   ForeignKey('DiagnosticOrderEvent.id'))
    """ Events specific to this item.
        List of `DiagnosticOrderEvent` items (represented as `dict` in JSON). """

    # todo specimen = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    specimen = Column(primitives.StringField)
    """ If this item relates to specific specimens.
        List of `FHIRReference` items referencing `Specimen`
        (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ proposed | draft | planned | requested | received | accepted | in-
        progress | review | completed | cancelled | suspended | rejected |
        failed.
        Type `str`. """

    def __init__(self, bodySite, code, event, specimen, status,):
        """ Initialize all valid properties.
        """
        self.bodySite = bodySite
        self.code = code
        self.event = event
        self.specimen = specimen
        self.status = status

    def __repr__(self):
        return '<DiagnosticOrderItem %r>' % 'self.property'  # replace self.property


class DiagnosticOrder(domainresource.DomainResource):
    """ A request for a diagnostic service.

    A record of a request for a diagnostic investigation service to be
    performed.
    """

    __tablename__ = "DiagnosticOrder"
    
    # todo encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ The encounter that this diagnostic order is associated with.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
    
    event = Column(primitives.StringField,
                   ForeignKey('DiagnosticOrderEvent.id'))
    """ A list of events of interest in the lifecycle.
        List of `DiagnosticOrderEvent` items (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Identifiers assigned to this order.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    item = Column(primitives.StringField,
                  ForeignKey('DiagnosticOrderItem.id'))
    """ The items the orderer requested.
        List of `DiagnosticOrderItem` items (represented as `dict` in JSON). """
    
    note = Column(primitives.StringField,
                  ForeignKey('Annotation.id'))
    """ Other notes and comments.
        List of `Annotation` items (represented as `dict` in JSON). """
    
    # todo orderer = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    orderer = Column(primitives.StringField)
    """ Who ordered the test.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    priority = Column(primitives.StringField)
    """ routine | urgent | stat | asap.
        Type `str`. """
    
    reason = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ Explanation/Justification for test.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    # todo specimen = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    specimen = Column(primitives.StringField)
    """ If the whole order relates to specific specimens.
        List of `FHIRReference` items referencing `Specimen`
        (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ proposed | draft | planned | requested | received | accepted | in-
        progress | review | completed | cancelled | suspended | rejected |
        failed.
        Type `str`. """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Who and/or what test is about.
        Type `FHIRReference` referencing `Patient, Group, Location, Device`
        (represented as `dict` in JSON). """
    
    # todo supportingInformation = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    supportingInformation = Column(primitives.StringField)
    """ Additional clinical information.
        List of `FHIRReference` items referencing `Observation,
        Condition, DocumentReference` (represented as `dict` in JSON). """

    def __init__(self, encounter, event, identifier, item, note,
                 orderer, priority, reason, specimen, status,
                 subject, supportingInformation,):
        """ Initialize all valid properties.
        """
        self.encounter = encounter
        self.event = event
        self.identifier = identifier
        self.item = item
        self.note = note
        self.orderer = orderer
        self.priority = priority
        self.reason = reason
        self.specimen = specimen
        self.status = status
        self.subject = subject
        self.supportingInformation = supportingInformation

    def __repr__(self):
        return '<DiagnosticOrder %r>' % 'self.property'  # replace self.property
