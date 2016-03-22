#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/HumanName)
#  Date: 2016-03-18.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import complex_dt


class HumanName(complex_dt.ComplexElement):
    """ Name of a human - parts and usage.

    A human's name with the ability to identify parts and usage.
    """

    __tablename__ = "HumanName"

    family = Column(primitives.StringField)
    """ Family name (often called 'Surname').
        List of `str` items. """

    given = Column(primitives.StringField)
    """ Given names (not always 'first'). Includes middle names.
        List of `str` items. """

    period = Column(primitives.StringField, ForeignKey('Period.id'))
    """ Time period when name was/is in use.
        Type `Period` (represented as `dict` in JSON). """

    prefix = Column(primitives.StringField)
    """ Parts that come before the name.
        List of `str` items. """

    suffix = Column(primitives.StringField)
    """ Parts that come after the name.
        List of `str` items. """

    text = Column(primitives.StringField)
    """ Text representation of the full name.
        Type `str`. """

    use = Column(primitives.StringField)
    """ usual | official | temp | nickname | anonymous | old | maiden.
        Type `str`. """

    def __init__(self, family, given, period, prefix, suffix, text,
                 use):
        """ Initialize all valid properties. """
        self.family = family
        self.given = given
        self.period = period
        self.prefix = prefix
        self.suffix = suffix
        self.text = text
        self.use = use

    def __repr__(self):
        return '<HumanName %r>' % 'self.property'  # replace self.property
