#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/EnrollmentResponse)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource

class EnrollmentResponse(domainresource.DomainResource):
    """ EnrollmentResponse resource.

    This resource provides enrollment and plan details from the processing of
    an Enrollment resource.
    """

    __tablename__ = "EnrollmentResponse"
    
    created = Column(primitives.DateTimeField)
    """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    disposition = Column(primitives.StringField)
    """ Disposition Message.
        Type `str`. """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    # todo organization = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    organization = Column(primitives.StringField)
    """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
    
    originalRuleset = Column(primitives.StringField,
                             ForeignKey('Coding.id'))
    """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
    
    outcome = Column(primitives.StringField)
    """ complete | error.
        Type `str`. """
    
    # todo request = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    request = Column(primitives.StringField)
    """ Claim reference.
        Type `FHIRReference` referencing `EnrollmentRequest`
        (represented as `dict` in JSON). """
    
    # todo requestOrganization = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    requestOrganization = Column(primitives.StringField)
    """ Responsible organization.
        Type `FHIRReference` referencing `Organization`
        (represented as `dict` in JSON). """
    
    # todo requestProvider = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    requestProvider = Column(primitives.StringField)
    """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    ruleset = Column(primitives.StringField,
                     ForeignKey('Coding.id'))
    """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """

    def __init__(self, created, disposition, identifier,
                 organization, originalRuleset, outcome,
                 request, requestOrganization, requestProvider,
                 ruleset,):
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
        return '<EnrollmentResponse %r>' % 'self.property'  # replace self.property