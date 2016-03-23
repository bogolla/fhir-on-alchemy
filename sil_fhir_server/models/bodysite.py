#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/BodySite)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource


class BodySite(domainresource.DomainResource):
    """ Specific and identified anatomical location.

    Record details about the anatomical location of a specimen or body part.
    This resource may be used when a coded concept does not provide the
    necessary detail needed for the use case.
    """

    __tablename__ = "BodySite"
    
    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Named anatomical location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    description = Column(primitives.StringField)
    """ The Description of anatomical location.
        Type `str`. """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Bodysite identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    image = Column(primitives.StringField,
                   ForeignKey('Attachment.id'))
    """ Attached images.
        List of `Attachment` items (represented as `dict` in JSON). """
    
    modifier = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Modification to location code.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    # todo
    # patient = Column(primitives.StringField,
    #                  ForeignKey('FHIRReference.id'))
    """ Patient.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    def __init__(self, code, description, identifier, image,
                 modifier, patient,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.description = description
        self.identifier = identifier
        self.image = image
        self.modifier = modifier
        self.patient = patient

    def __repr__(self):
        return '<BodySite %r>' % 'self.property'  # replace self.property