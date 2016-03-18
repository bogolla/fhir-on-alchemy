#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Basic)
#  Date: 2016-03-18.


from . import domainresource

class Basic(domainresource.DomainResource):
    """ Resource for non-supported content.

    Basic is used for handling concepts not yet defined in FHIR, narrative-only
    resources that don't map to an existing resource, and custom resources not
    appropriate for inclusion in the FHIR specification.
    """

    __tablename__ = "Basic"

    author = Column()
    """ Who created.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """

    code = Column()
    """ Kind of Resource.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    created = Column()
    """ When created.
        Type `FHIRDate` (represented as `str` in JSON). """

    identifier = Column(Identifier)
    """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    subject = Column()
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


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier