#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/EligibilityRequest)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class EligibilityRequest(domainresource.DomainResource):
    """ Eligibility request.

    This resource provides the insurance eligibility details from the insurer
    regarding a specified coverage and optionally some class of service.
    """

    __tablename__ = "EligibilityRequest"
    
    created = Column(FHIRDate)
    """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    identifier = Column(Identifier)
    """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    organization = Column(FHIRReference)
    """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
    
    originalRuleset = Column(Coding)
    """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
    
    provider = Column(FHIRReference)
    """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    ruleset = Column(Coding)
    """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
    
    target = Column(FHIRReference)
    """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    def __init__(self, created, identifier, organization, originalRuleset, provider, ruleset, target,):
        """ Initialize all valid properties.
        """
        self.created = created
        self.identifier = identifier
        self.organization = organization
        self.originalRuleset = originalRuleset
        self.provider = provider
        self.ruleset = ruleset
        self.target = target

    def __repr__(self):
        return '<EligibilityRequest %r>' % 'self.property'  # replace self.property


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier