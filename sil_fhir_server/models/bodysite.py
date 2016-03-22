#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/BodySite)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer
from sil_fhir_server.data_types import primitives
from . import domainresource

class BodySite(domainresource.DomainResource):
    """ Specific and identified anatomical location.

    Record details about the anatomical location of a specimen or body part.
    This resource may be used when a coded concept does not provide the
    necessary detail needed for the use case.
    """

    __tablename__ = "BodySite"

    code = Column(CodeableConcept)
    """ Named anatomical location.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    description = Column(primitives.StringField)
    """ The Description of anatomical location.
        Type `str`. """

    identifier = Column(Identifier)
    """ Bodysite identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    image = Column(Attachment)
    """ Attached images.
        List of `Attachment` items (represented as `dict` in JSON). """

    modifier = Column(CodeableConcept)
    """ Modification to location code.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    patient = Column(FHIRReference)
    """ Patient.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    def __init__(self, code, description, identifier, image, modifier, patient,):
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


from . import attachment
from . import codeableconcept
from . import fhirreference
from . import identifier