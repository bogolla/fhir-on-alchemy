#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Element)
#  Date: 2016-03-18.


from . import fhirabstractbase

class Element(fhirabstractbase.FHIRAbstractBase):
    """ Base for all elements.

    Base definition for all elements in a resource.
    """

    __tablename__ = "Element"

    extension = Column(Extension)
    """ Additional Content defined by implementations.
        List of `Extension` items (represented as `dict` in JSON). """

    id = Column()
    """ xml:id (or equivalent in JSON).
        Type `str`. """

    def __init__(self, extension, id,):
        """ Initialize all valid properties.
        """
        self.extension = extension
        self.id = id

    def __repr__(self):
        return '<Element %r>' % 'self.property'  # replace self.property


from . import extension