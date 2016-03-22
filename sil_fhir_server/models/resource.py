#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Resource)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import fhirabstractresource

class Resource(fhirabstractresource.FHIRAbstractResource):
    """ Base Resource.

    This is the base resource type for everything.
    """

    __tablename__ = "Resource"

    id = Column(primitives.StringField)
    """ Logical id of this artifact.
        Type `str`. """

    implicitRules = Column(primitives.StringField)
    """ A set of rules under which this content was created.
        Type `str`. """

    language = Column(primitives.StringField)
    """ Language of the resource content.
        Type `str`. """

    meta = Column(Meta)
    """ Metadata about the resource.
        Type `Meta` (represented as `dict` in JSON). """

    def __init__(self, id, implicitRules, language, meta,):
        """ Initialize all valid properties.
        """
        self.id = id
        self.implicitRules = implicitRules
        self.language = language
        self.meta = meta

    def __repr__(self):
        return '<Resource %r>' % 'self.property'  # replace self.property


from . import meta