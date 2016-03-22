#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Address)
#  Date: 2016-03-18.


from sqlalchemy import Column, ForeignKey
from . import complex_dt
from sil_fhir_server.data_types import primitives


class Address(complex_dt.ComplexElement):
    """ A postal address.

    There is a variety of postal address formats defined around the
    world. This format defines a superset that is the basis for all
    addresses around the world.
    """

    __tablename__ = "Address"

    city = Column(primitives.StringField)
    """ Name of city, town etc..
        Type `str`. """

    country = Column(primitives.StringField)
    """ Country (can be ISO 3166 3 letter code).
        Type `str`. """

    district = Column(primitives.StringField)
    """ District name (aka county).
        Type `str`. """

    line = Column(primitives.StringField)
    """ Street name, number, direction & P.O. Box etc..
        List of `str` items. """

    period = Column(primitives.StringField, ForeignKey('Period.id'))
    """ Time period when address was/is in use.
        Type `Period` (represented as `dict` in JSON). """

    postalCode = Column(primitives.StringField)
    """ Postal code for area.
        Type `str`. """

    state = Column(primitives.StringField)
    """ Sub-unit of country (abbreviations ok).
        Type `str`. """

    text = Column(primitives.StringField)
    """ Text representation of the address.
        Type `str`. """

    type = Column(primitives.StringField)
    """ postal | physical | both.
        Type `str`. """

    use = Column(primitives.StringField)
    """ home | work | temp | old - purpose of this address.
        Type `str`. """

    def __init__(self, city, country, district, line, period,
                 postalCode, state, text, type, use):
        """ Initialize all valid properties. """

        self.city = city
        self.country = country
        self.district = district
        self.line = line
        self.period = period
        self.postalCode = postalCode
        self.state = state
        self.text = text
        self.type = type
        self.use = use

    def __repr__(self):
        return '<Address %r>' % 'self.property'  # replace self.property
