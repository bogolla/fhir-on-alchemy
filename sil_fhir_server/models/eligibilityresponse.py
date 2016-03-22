#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/EligibilityResponse)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class EligibilityResponse(domainresource.DomainResource):
    """ EligibilityResponse resource.

    This resource provides eligibility and plan details from the processing of
    an Eligibility resource.
    """

    __tablename__ = "EligibilityResponse"

    created = Column(FHIRDate)
    """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

    disposition = Column(primitives.StringField)
    """ Disposition Message.
        Type `str`. """

    identifier = Column(Identifier)
    """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    organization = Column(FHIRReference)
    """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    originalRuleset = Column(Coding)
    """ Original version.
        Type `Coding` (represented as `dict` in JSON). """

    outcome = Column(primitives.StringField)
    """ complete | error.
        Type `str`. """

    request = Column(FHIRReference)
    """ Claim reference.
        Type `FHIRReference` referencing `EligibilityRequest` (represented as `dict` in JSON). """

    requestOrganization = Column(FHIRReference)
    """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    requestProvider = Column(FHIRReference)
    """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    ruleset = Column(Coding)
    """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, created, disposition, identifier, organization, originalRuleset, outcome, request, requestOrganization, requestProvider, ruleset,):
        """ Initialize all valid properties.
        """
        self.created = created
        self.disposition = disposition
        self.identifier = identifier
        self.organization = organization
        self.originalRuleset = originalRuleset
        self.outcome = outcome
        self.request = request
        self.requestOrganization = requestOrganization
        self.requestProvider = requestProvider
        self.ruleset = ruleset

    def __repr__(self):
        return '<EligibilityResponse %r>' % 'self.property'  # replace self.property


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier