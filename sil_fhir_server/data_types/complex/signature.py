#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Signature)
#  Date: 2016-03-18.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import complex_dt


class Signature(complex_dt.ComplexElement):
    """ A digital Signature - XML DigSig, JWT, Graphical image of signature, etc..

    A digital signature along with supporting context. The signature may be
    electronic/cryptographic in nature, or a graphical image representing a
    hand-written signature, or a signature process. Different Signature
    approaches have different data_types.
    """

    __tablename__ = "Signature"

    blob = Column(primitives.StringField)
    """ The actual signature content (XML DigSig. JWT, picture, etc.).
        Type `str`. """

    contentType = Column(primitives.StringField)
    """ The technical format of the signature.
        Type `str`. """

    type = Column(primitives.StringField,
                  ForeignKey('Coding.id'))
    """ Indication of the reason the entity signed the object(s).
        List of `Coding` items (represented as `dict` in JSON). """

    when = Column(primitives.DateTimeField)
    """ When the signature was created.
        Type `FHIRDate` (represented as `str` in JSON). """

    # TODO
    # whoReference = Column(primitives.StringField,
    #                       ForeignKey('FHIRReference'))
    """ Who signed the signature.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient, Device, Organization` (represented as `dict` in JSON). """

    whoUri = Column(primitives.StringField)
    """ Who signed the signature.
        Type `str`. """

    def __init__(self, blob, contentType, type, when, whoReference, whoUri):
        """ Initialize all valid properties.
        """
        self.blob = blob
        self.contentType = contentType
        self.type = type
        self.when = when
        self.whoReference = whoReference
        self.whoUri = whoUri

    def __repr__(self):
        return '<Signature %r>' % 'self.property'  # replace self.property
