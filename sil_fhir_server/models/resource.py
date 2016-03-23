#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Resource)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declared_attr

from app import db
from sil_fhir_server.data_types import primitives


# todo class Resource(fhirabstractresource.FHIRAbstractResource):
class Resource(db.Model):
    """ Base Resource.

    This is the base resource type for everything.
    """

    __tablename__ = "Resource"
    __abstract__ = True
    
    id = Column(primitives.StringField, primary_key=True)
    """ Logical id of this artifact.
        Type `str`. """
    
    implicitRules = Column(primitives.StringField)
    """ A set of rules under which this content was created.
        Type `str`. """
    
    language = Column(primitives.StringField)
    """ Language of the resource content.
        Type `str`. """

    @declared_attr
    def meta(cls):
        return Column(primitives.StringField, ForeignKey('Meta.id'))
    # meta = Column(primitives.StringField, ForeignKey('Meta.id'))
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