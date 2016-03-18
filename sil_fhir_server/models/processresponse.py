#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ProcessResponse)
#  Date: 2016-03-18.


from . import domainresource

class ProcessResponse(domainresource.DomainResource):
    """ ProcessResponse resource.

    This resource provides processing status, errors and notes from the
    processing of a resource.
    """

    __tablename__ = "ProcessResponse"

    created = Column()
    """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

    disposition = Column()
    """ Disposition Message.
        Type `str`. """

    error = Column(Coding)
    """ Error code.
        List of `Coding` items (represented as `dict` in JSON). """

    form = Column()
    """ Printed Form Identifier.
        Type `Coding` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    notes = Column(ProcessResponseNotes)
    """ Notes.
        List of `ProcessResponseNotes` items (represented as `dict` in JSON). """

    organization = Column()
    """ Authoring Organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    originalRuleset = Column()
    """ Original version.
        Type `Coding` (represented as `dict` in JSON). """

    outcome = Column()
    """ Processing outcome.
        Type `Coding` (represented as `dict` in JSON). """

    request = Column()
    """ Request reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    requestOrganization = Column()
    """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    requestProvider = Column()
    """ Responsible Practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    ruleset = Column()
    """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, created, disposition, error, form, identifier, notes, organization, originalRuleset, outcome, request, requestOrganization, requestProvider, ruleset,):
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


from . import backboneelement

class ProcessResponseNotes(backboneelement.BackboneElement):
    """ Notes.

    Suite of processing note or additional requirements is the processing has
    been held.
    """

    __tablename__ = "ProcessResponseNotes"

    text = Column()
    """ Notes text.
        Type `str`. """

    type = Column()
    """ display | print | printoper.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, text, type,):
        """ Initialize all valid properties.
        """
        self.text = text
        self.type = type

    def __repr__(self):
        return '<ProcessResponseNotes %r>' % 'self.property'  # replace self.property


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier