#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Reference)
#  Date: 2016-03-18.


from . import element

class Reference(element.Element):
    """ A reference from one resource to another.
    """

    __tablename__ = "Reference"

    display = Column()
    """ Text alternative for the resource.
        Type `str`. """

    reference = Column()
    """ Relative, internal or absolute URL reference.
        Type `str`. """

    def __init__(self, display, reference,):
        """ Initialize all valid properties.
        """
        self.display = display
        self.reference = reference

    def __repr__(self):
        return '<Reference %r>' % 'self.property'  # replace self.property

