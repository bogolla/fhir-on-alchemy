#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DomainResource)
#  Date: 2016-03-18.


from . import resource

class DomainResource(resource.Resource):
    """ A resource with narrative, extensions, and contained resources.

    A resource that includes narrative, extensions, and contained resources.
    """

    __tablename__ = "DomainResource"

    contained = Column(Resource)
    """ Contained, inline Resources.
        List of `Resource` items (represented as `dict` in JSON). """

    extension = Column(Extension)
    """ Additional Content defined by implementations.
        List of `Extension` items (represented as `dict` in JSON). """

    modifierExtension = Column(Extension)
    """ Extensions that cannot be ignored.
        List of `Extension` items (represented as `dict` in JSON). """

    text = Column()
    """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """

    def __init__(self, contained, extension, modifierExtension, text,):
        """ Initialize all valid properties.
        """
        self.contained = contained
        self.extension = extension
        self.modifierExtension = modifierExtension
        self.text = text

    def __repr__(self):
        return '<DomainResource %r>' % 'self.property'  # replace self.property


from . import extension
from . import narrative