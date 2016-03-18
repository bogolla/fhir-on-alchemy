#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ContactPoint)
#  Date: 2016-03-18.


from . import element

class ContactPoint(element.Element):
    """ Details of a Technology mediated contact point (phone, fax, email, etc.).

    Details for all kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """

    __tablename__ = "ContactPoint"

    period = Column()
    """ Time period when the contact point was/is in use.
        Type `Period` (represented as `dict` in JSON). """

    rank = Column()
    """ Specify preferred order of use (1 = highest).
        Type `int`. """

    system = Column()
    """ phone | fax | email | pager | other.
        Type `str`. """

    use = Column()
    """ home | work | temp | old | mobile - purpose of this contact point.
        Type `str`. """

    value = Column()
    """ The actual contact point details.
        Type `str`. """

    def __init__(self, period, rank, system, use, value,):
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