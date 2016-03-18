#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Signature)
#  Date: 2016-03-18.


from . import element

class Signature(element.Element):
    """ A digital Signature - XML DigSig, JWT, Graphical image of signature, etc..

    A digital signature along with supporting context. The signature may be
    electronic/cryptographic in nature, or a graphical image representing a
    hand-written signature, or a signature process. Different Signature
    approaches have different utilities.
    """

    __tablename__ = "Signature"

    blob = Column()
    """ The actual signature content (XML DigSig. JWT, picture, etc.).
        Type `str`. """

    contentType = Column()
    """ The technical format of the signature.
        Type `str`. """

    type = Column(Coding)
    """ Indication of the reason the entity signed the object(s).
        List of `Coding` items (represented as `dict` in JSON). """

    when = Column()
    """ When the signature was created.
        Type `FHIRDate` (represented as `str` in JSON). """

    whoReference = Column()
    """ Who signed the signature.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient, Device, Organization` (represented as `dict` in JSON). """

    whoUri = Column()
    """ Who signed the signature.
        Type `str`. """

    def __init__(self, blob, contentType, type, when, whoReference, whoUri,):
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


from . import coding
from . import fhirdate
from . import fhirreference