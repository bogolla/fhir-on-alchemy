#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ProcessRequest)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class ProcessRequest(domainresource.DomainResource):
    """ Process request.

    This resource provides the target, request and response, and action details
    for an action to be performed by the target on or about existing resources.
    """

    __tablename__ = "ProcessRequest"

    action = Column(primitives.StringField)
    """ cancel | poll | reprocess | status.
        Type `str`. """

    created = Column(FHIRDate)
    """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

    exclude = Column(primitives.StringField)
    """ Resource type(s) to exclude.
        List of `str` items. """

    identifier = Column(Identifier)
    """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    include = Column(primitives.StringField)
    """ Resource type(s) to include.
        List of `str` items. """

    item = Column(ProcessRequestItem)
    """ Items to re-adjudicate.
        List of `ProcessRequestItem` items (represented as `dict` in JSON). """

    nullify = Column(bool)
    """ Nullify.
        Type `bool`. """

    organization = Column(FHIRReference)
    """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    originalRuleset = Column(Coding)
    """ Original version.
        Type `Coding` (represented as `dict` in JSON). """

    period = Column(Period)
    """ Period.
        Type `Period` (represented as `dict` in JSON). """

    provider = Column(FHIRReference)
    """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    reference = Column(primitives.StringField)
    """ Reference number/string.
        Type `str`. """

    request = Column(FHIRReference)
    """ Request reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    response = Column(FHIRReference)
    """ Response reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    ruleset = Column(Coding)
    """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """

    target = Column(FHIRReference)
    """ Target of the request.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    def __init__(self, action, created, exclude, identifier, include, item, nullify, organization, originalRuleset, period, provider, reference, request, response, ruleset, target,):
        """ Initialize all valid properties.
        """
        self.action = action
        self.created = created
        self.exclude = exclude
        self.identifier = identifier
        self.include = include
        self.item = item
        self.nullify = nullify
        self.organization = organization
        self.originalRuleset = originalRuleset
        self.period = period
        self.provider = provider
        self.reference = reference
        self.request = request
        self.response = response
        self.ruleset = ruleset
        self.target = target

    def __repr__(self):
        return '<ProcessRequest %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class ProcessRequestItem(backboneelement.BackboneElement):
    """ Items to re-adjudicate.

    List of top level items to be re-adjudicated, if none specified then the
    entire submission is re-adjudicated.
    """

    __tablename__ = "ProcessRequestItem"

    sequenceLinkId = Column(Integer)
    """ Service instance.
        Type `int`. """

    def __init__(self, sequenceLinkId,):
        """ Initialize all valid properties.
        """
        self.sequenceLinkId = sequenceLinkId

    def __repr__(self):
        return '<ProcessRequestItem %r>' % 'self.property'  # replace self.property


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period