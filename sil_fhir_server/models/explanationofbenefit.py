#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit)
#  Date: 2016-03-18.


from . import domainresource

class ExplanationOfBenefit(domainresource.DomainResource):
    """ Remittance resource.

    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    __tablename__ = "ExplanationOfBenefit"

    created = Column()
    """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

    disposition = Column()
    """ Disposition Message.
        Type `str`. """

    identifier = Column(Identifier)
    """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    organization = Column()
    """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    originalRuleset = Column()
    """ Original version.
        Type `Coding` (represented as `dict` in JSON). """

    outcome = Column()
    """ complete | error.
        Type `str`. """

    request = Column()
    """ Claim reference.
        Type `FHIRReference` referencing `Claim` (represented as `dict` in JSON). """

    requestOrganization = Column()
    """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    requestProvider = Column()
    """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    ruleset = Column()
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
        return '<ExplanationOfBenefit %r>' % 'self.property'  # replace self.property


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier