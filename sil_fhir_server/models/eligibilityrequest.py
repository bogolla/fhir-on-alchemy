#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/EligibilityRequest)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource


class EligibilityRequest(domainresource.DomainResource):
    """ Eligibility request.

    This resource provides the insurance eligibility details from the insurer
    regarding a specified coverage and optionally some class of service.
    """

    __tablename__ = "EligibilityRequest"
    
    created = Column(primitives.DateTimeField)
    """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    # todo organization = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    organization = Column(primitives.StringField)
    """ Responsible organization.
        Type `FHIRReference` referencing `Organization`
        (represented as `dict` in JSON). """
    
    originalRuleset = Column(primitives.StringField,
                             ForeignKey('Coding.id'))
    """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
    
    # todo provider = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    provider = Column(primitives.StringField)
    """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    ruleset = Column(primitives.StringField,
                     ForeignKey('Coding.id'))
    """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
    
    # todo target = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    target = Column(primitives.StringField)
    """ Insurer.
        Type `FHIRReference` referencing `Organization`
        (represented as `dict` in JSON). """

    def __init__(self, created, identifier, organization,
                 originalRuleset, provider, ruleset, target,):
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
