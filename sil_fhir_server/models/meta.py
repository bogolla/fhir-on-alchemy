#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Meta)
#  Date: 2016-03-18.


from . import element

class Meta(element.Element):
    """ Metadata about a resource.

    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content may not always be
    associated with version changes to the resource.
    """

    __tablename__ = "Meta"

    lastUpdated = Column()
    """ When the resource version last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

    profile = Column(str)
    """ Profiles this resource claims to conform to.
        List of `str` items. """

    security = Column(Coding)
    """ Security Labels applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """

    tag = Column(Coding)
    """ Tags applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """

    versionId = Column()
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


from . import coding
from . import fhirdate