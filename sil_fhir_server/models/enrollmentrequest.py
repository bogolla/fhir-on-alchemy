#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/EnrollmentRequest)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource

class EnrollmentRequest(domainresource.DomainResource):
    """ Enrollment request.

    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """

    __tablename__ = "EnrollmentRequest"
    
    # todo coverage = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    coverage = Column(primitives.StringField)
    """ Insurance information.
        Type `FHIRReference` referencing `Coverage`
        (represented as `dict` in JSON). """
    
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
        Type `FHIRReference` referencing `Practitioner`
        (represented as `dict` in JSON). """
    
    relationship = Column(primitives.StringField,
                          ForeignKey('Coding.id'))
    """ Patient relationship to subscriber.
        Type `Coding` (represented as `dict` in JSON). """
    
    ruleset = Column(primitives.StringField,
                     ForeignKey('Coding.id'))
    """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ The subject of the Products and Services.
        Type `FHIRReference` referencing `Patient`
        (represented as `dict` in JSON). """
    
    # todo target = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    target = Column(primitives.StringField)
    """ Insurer.
        Type `FHIRReference` referencing `Organization`
        (represented as `dict` in JSON). """

    def __init__(self, coverage, created, identifier, organization,
                 originalRuleset, provider, relationship, ruleset,
                 subject, target,):
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