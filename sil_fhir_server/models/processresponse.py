#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ProcessResponse)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class ProcessResponseNotes(backboneelement.BackboneElement):
    """ Notes.

    Suite of processing note or additional requirements is the processing has
    been held.
    """

    __tablename__ = "ProcessResponseNotes"

    text = Column(primitives.StringField)
    """ Notes text.
        Type `str`. """

    type = Column(primitives.StringField,
                  ForeignKey('Coding.id'))
    """ display | print | printoper.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, text, type,):
        """ Initialize all valid properties.
        """
        self.text = text
        self.type = type

    def __repr__(self):
        return '<ProcessResponseNotes %r>' % 'self.property'  # replace self.property


class ProcessResponse(domainresource.DomainResource):
    """ ProcessResponse resource.

    This resource provides processing status, errors and notes from the
    processing of a resource.
    """

    __tablename__ = "ProcessResponse"
    
    created = Column(primitives.DateTimeField)
    """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    disposition = Column(primitives.StringField)
    """ Disposition Message.
        Type `str`. """
    
    error = Column(primitives.StringField,
                   ForeignKey('Coding.id'))
    """ Error code.
        List of `Coding` items (represented as `dict` in JSON). """
    
    form = Column(primitives.StringField,
                  ForeignKey('Coding.id'))
    """ Printed Form Identifier.
        Type `Coding` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    notes = Column(primitives.StringField,
                   ForeignKey('ProcessResponseNotes.id'))
    """ Notes.
        List of `ProcessResponseNotes` items (represented as `dict` in JSON). """
    
    # todo organization = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    organization = Column(primitives.StringField)
    """ Authoring Organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
    
    originalRuleset = Column(primitives.StringField,
                             ForeignKey('Coding.id'))
    """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
    
    outcome = Column(primitives.StringField,
                     ForeignKey('Coding.id'))
    """ Processing outcome.
        Type `Coding` (represented as `dict` in JSON). """
    
    # todo request = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    request = Column(primitives.StringField)
    """ Request reference.
        Type `FHIRReference` referencing `Resource`
        (represented as `dict` in JSON). """
    
    # todo requestOrganization = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    requestOrganization = Column(primitives.StringField)
    """ Responsible organization.
        Type `FHIRReference` referencing `Organization`
        (represented as `dict` in JSON). """
    
    # todo requestProvider = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    requestProvider = Column(primitives.StringField)
    """ Responsible Practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    ruleset = Column(primitives.StringField,
                     ForeignKey('Coding.id'))
    """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, created, disposition, error, form, identifier,
                 notes, organization, originalRuleset, outcome, request,
                 requestOrganization, requestProvider, ruleset,):
        """ Initialize all valid properties.
        """
        self.created = created
        self.disposition = disposition
        self.error = error
        self.form = form
        self.identifier = identifier
        self.notes = notes
        self.organization = organization
        self.originalRuleset = originalRuleset
        self.outcome = outcome
        self.request = request
        self.requestOrganization = requestOrganization
        self.requestProvider = requestProvider
        self.ruleset = ruleset

    def __repr__(self):
        return '<ProcessResponse %r>' % 'self.property'  # replace self.property
