#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/EnrollmentRequest)
#  Date: 2016-03-18.


from . import domainresource

class EnrollmentRequest(domainresource.DomainResource):
    """ Enrollment request.

    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """

    __tablename__ = "EnrollmentRequest"

    coverage = Column()
    """ Insurance information.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """

    created = Column()
    """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

    identifier = Column(Identifier)
    """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    organization = Column()
    """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    originalRuleset = Column()
    """ Original version.
        Type `Coding` (represented as `dict` in JSON). """

    provider = Column()
    """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """

    relationship = Column()
    """ Patient relationship to subscriber.
        Type `Coding` (represented as `dict` in JSON). """

    ruleset = Column()
    """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """

    subject = Column()
    """ The subject of the Products and Services.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    target = Column()
    """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    def __init__(self, coverage, created, identifier, organization, originalRuleset, provider, relationship, ruleset, subject, target,):
        """ Initialize all valid properties.
        """
        self.coverage = coverage
        self.created = created
        self.identifier = identifier
        self.organization = organization
        self.originalRuleset = originalRuleset
        self.provider = provider
        self.relationship = relationship
        self.ruleset = ruleset
        self.subject = subject
        self.target = target

    def __repr__(self):
        return '<EnrollmentRequest %r>' % 'self.property'  # replace self.property


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier