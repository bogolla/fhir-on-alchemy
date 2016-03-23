#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Basic)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource


class Basic(domainresource.DomainResource):
    """ Resource for non-supported content.

    Basic is used for handling concepts not yet defined in FHIR, narrative-only
    resources that don't map to an existing resource, and custom resources not
    appropriate for inclusion in the FHIR specification.
    """

    __tablename__ = "Basic"

    # todo
    # author = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Who created.
        Type `FHIRReference` referencing `Practitioner, Patient,
        RelatedPerson` (represented as `dict` in JSON). """
    
    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Kind of Resource.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    created = Column(primitives.DateTimeField)
    """ When created.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    # todo
    # subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Identifies the focus of this resource.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    def __init__(self, author, code, created, identifier, subject,):
        """ Initialize all valid properties.
        """
        self.author = author
        self.code = code
        self.created = created
        self.identifier = identifier
        self.subject = subject

    def __repr__(self):
        return '<Basic %r>' % 'self.property'  # replace self.property
