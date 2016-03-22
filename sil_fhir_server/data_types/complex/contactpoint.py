#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ContactPoint)
#  Date: 2016-03-18.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import complex_dt


class ContactPoint(complex_dt.ComplexElement):
    """ Details of a Technology mediated contact point (phone, fax, email, etc.).

    Details for all kinds of technology mediated contact points for a
    person or organization, including telephone, email, etc.
    """

    __tablename__ = "ContactPoint"

    period = Column(primitives.StringField, ForeignKey('Period.id'))
    """ Time period when the contact point was/is in use.
        Type `Period` (represented as `dict` in JSON). """

    rank = Column(primitives.IntegerField)
    """ Specify preferred order of use (1 = highest).
        Type `int`. """

    system = Column(primitives.StringField)
    """ phone | fax | email | pager | other.
        Type `str`. """

    use = Column(primitives.StringField)
    """ home | work | temp | old | mobile - purpose of this contact point.
        Type `str`. """

    value = Column(primitives.StringField)
    """ The actual contact point details.
        Type `str`. """

    def __init__(self, period, rank, system, use, value):
        """ Initialize all valid properties.
        """
        self.period = period
        self.rank = rank
        self.system = system
        self.use = use
        self.value = value

    def __repr__(self):
        return '<ContactPoint %r>' % 'self.property'  # replace self.property


from . import period