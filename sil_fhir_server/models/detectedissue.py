#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DetectedIssue)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class DetectedIssueMitigation(backboneelement.BackboneElement):
    """ Step taken to address.

    Indicates an action that has been taken or is committed to to reduce or
    eliminate the likelihood of the risk identified by the detected issue from
    manifesting.  Can also reflect an observation of known mitigating factors
    that may reduce/eliminate the need for any action.
    """

    __tablename__ = "DetectedIssueMitigation"

    action = Column(primitives.StringField,
                    ForeignKey('CodeableConcept.id'))
    """ What mitigation?.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    # todo author = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    author = Column(primitives.StringField)
    """ Who is committing?.
        Type `FHIRReference` referencing `Practitioner`
        (represented as `dict` in JSON). """

    date = Column(primitives.DateTimeField)
    """ Date committed.
        Type `FHIRDate` (represented as `str` in JSON). """

    def __init__(self, action, author, date,):
        """ Initialize all valid properties.
        """
        self.action = action
        self.author = author
        self.date = date

    def __repr__(self):
        return '<DetectedIssueMitigation %r>' % 'self.property'  # replace self.property


class DetectedIssue(domainresource.DomainResource):
    """ Clinical issue with action.

    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """

    __tablename__ = "DetectedIssue"
    
    # todo author = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    author = Column(primitives.StringField)
    """ The provider or device that identified the issue.
        Type `FHIRReference` referencing `Practitioner, Device`
        (represented as `dict` in JSON). """
    
    category = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Issue Category, e.g. drug-drug, duplicate therapy, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    date = Column(primitives.DateTimeField)
    """ When identified.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    detail = Column(primitives.StringField)
    """ Description and context.
        Type `str`. """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Unique id for the detected issue.
        Type `Identifier` (represented as `dict` in JSON). """
    
    # todo implicated = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    implicated = Column(primitives.StringField)
    """ Problem resource.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
    
    mitigation = Column(primitives.StringField,
                        ForeignKey('DetectedIssueMitigation.id'))
    """ Step taken to address.
        List of `DetectedIssueMitigation` items (represented as `dict` in JSON). """
    
    # todo patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    patient = Column(primitives.StringField)
    """ Associated patient.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    reference = Column(primitives.StringField)
    """ Authority for issue.
        Type `str`. """
    
    severity = Column(primitives.StringField)
    """ high | moderate | low.
        Type `str`. """

    def __init__(self, author, category, date, detail, identifier,
                 implicated, mitigation, patient, reference, severity,):
        """ Initialize all valid properties.
        """
        self.author = author
        self.category = category
        self.date = date
        self.detail = detail
        self.identifier = identifier
        self.implicated = implicated
        self.mitigation = mitigation
        self.patient = patient
        self.reference = reference
        self.severity = severity

    def __repr__(self):
        return '<DetectedIssue %r>' % 'self.property'  # replace self.property
