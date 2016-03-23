#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Meta)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import element

class Meta(element.Element):
    """ Metadata about a resource.

    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content may not always be
    associated with version changes to the resource.
    """

    __tablename__ = "Meta"
    
    lastUpdated = Column(primitives.DateTimeField)
    """ When the resource version last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    profile = Column(primitives.StringField)
    """ Profiles this resource claims to conform to.
        List of `str` items. """
    
    security = Column(primitives.StringField,
                      ForeignKey('Coding.id'))
    """ Security Labels applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """
    
    tag = Column(primitives.StringField,
                 ForeignKey('Coding.id'))
    """ Tags applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """
    
    versionId = Column(primitives.StringField)
    """ Version specific identifier.
        Type `str`. """

    def __init__(self, lastUpdated, profile, security, tag, versionId,):
        """ Initialize all valid properties.
        """
        self.lastUpdated = lastUpdated
        self.profile = profile
        self.security = security
        self.tag = tag
        self.versionId = versionId

    def __repr__(self):
        return '<Meta %r>' % 'self.property'  # replace self.property