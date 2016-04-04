#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Address)
#  Date: 2016-03-18.


from sqlalchemy import Column
from sil_fhir_server.data_types import primitives
from sil_fhir_server.utilities.pg_composite import CompositeType


class AddressField(object):
    """ A postal address.

    There is a variety of postal address formats defined around the
    world. This format defines a superset that is the basis for all
    addresses around the world.
    """

    def __init__(self):
        pass

    def address(self):
        self.new_type = CompositeType(
            'address_field',
            [
                Column('city', primitives.StringField),
                # Name of city, town etc..
                # Type `str`.

                Column('country', primitives.StringField),
                # Country (can be ISO 3166 3 letter code).
                # Type `str`.

                Column('district', primitives.StringField),
                # District name (aka county)
                # Type `str`.

                Column('line', primitives.StringField),
                # Street name, number, direction & P.O. Box etc..
                # List of `str` items.

                Column('period', primitives.StringField),
                # Time period when address was/is in use.
                # Type `Period` (represented as `dict` in JSON).

                Column('postalCode', primitives.StringField),
                # Postal code for area.
                # Type `str`.

                Column('state', primitives.StringField),
                # Sub-unit of country (abbreviations ok).
                # Type `str`.

                Column('type', primitives.StringField),
                # postal | physical | both.
                # Type `str`.

                Column('text', primitives.StringField),
                # Text representation of the address.
                # Type `str`.

                Column('use', primitives.StringField)
                # home | work | temp | old - purpose of this address.
                # Type `str`.
            ]
        )
        return self.new_type
