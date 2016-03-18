#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/HumanName)
#  Date: 2016-03-18.


from . import element

class HumanName(element.Element):
    """ Name of a human - parts and usage.

    A human's name with the ability to identify parts and usage.
    """

    __tablename__ = "HumanName"

    family = Column(str)
    """ Family name (often called 'Surname').
        List of `str` items. """

    given = Column(str)
    """ Given names (not always 'first'). Includes middle names.
        List of `str` items. """

    period = Column()
    """ Time period when name was/is in use.
        Type `Period` (represented as `dict` in JSON). """

    prefix = Column(str)
    """ Parts that come before the name.
        List of `str` items. """

    suffix = Column(str)
    """ Parts that come after the name.
        List of `str` items. """

    text = Column()
    """ Text representation of the full name.
        Type `str`. """

    use = Column()
    """ usual | official | temp | nickname | anonymous | old | maiden.
        Type `str`. """

    def __init__(self, family, given, period, prefix, suffix, text, use,):
        """ Initialize all valid properties.
        """
        self.family = family
        self.given = given
        self.period = period
        self.prefix = prefix
        self.suffix = suffix
        self.text = text
        self.use = use

    def __repr__(self):
        return '<HumanName %r>' % 'self.property'  # replace self.property


from . import period