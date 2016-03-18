#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/SearchParameter)
#  Date: 2016-03-18.


from . import domainresource

class SearchParameter(domainresource.DomainResource):
    """ Search Parameter for a resource.

    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """

    __tablename__ = "SearchParameter"

    base = Column()
    """ The resource type this search parameter applies to.
        Type `str`. """

    code = Column()
    """ Code used in URL.
        Type `str`. """

    contact = Column(SearchParameterContact)
    """ Contact details of the publisher.
        List of `SearchParameterContact` items (represented as `dict` in JSON). """

    date = Column()
    """ Publication Date(/time).
        Type `FHIRDate` (represented as `str` in JSON). """

    description = Column()
    """ Documentation for  search parameter.
        Type `str`. """

    experimental = Column()
    """ If for testing purposes, not real usage.
        Type `bool`. """

    name = Column()
    """ Informal name for this search parameter.
        Type `str`. """

    publisher = Column()
    """ Name of the publisher (Organization or individual).
        Type `str`. """

    requirements = Column()
    """ Why this search parameter is defined.
        Type `str`. """

    status = Column()
    """ draft | active | retired.
        Type `str`. """

    target = Column(str)
    """ Types of resource (if a resource reference).
        List of `str` items. """

    type = Column()
    """ number | date | string | token | reference | composite | quantity |
        uri.
        Type `str`. """

    url = Column()
    """ Absolute URL used to reference this search parameter.
        Type `str`. """

    xpath = Column()
    """ XPath that extracts the values.
        Type `str`. """

    xpathUsage = Column()
    """ normal | phonetic | nearby | distance | other.
        Type `str`. """

    def __init__(self, base, code, contact, date, description, experimental, name, publisher, requirements, status, target, type, url, xpath, xpathUsage,):
        """ Initialize all valid properties.
        """
        self.base = base
        self.code = code
        self.contact = contact
        self.date = date
        self.description = description
        self.experimental = experimental
        self.name = name
        self.publisher = publisher
        self.requirements = requirements
        self.status = status
        self.target = target
        self.type = type
        self.url = url
        self.xpath = xpath
        self.xpathUsage = xpathUsage

    def __repr__(self):
        return '<SearchParameter %r>' % 'self.property'  # replace self.property


from . import backboneelement

class SearchParameterContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    __tablename__ = "SearchParameterContact"

    name = Column()
    """ Name of a individual to contact.
        Type `str`. """

    telecom = Column(ContactPoint)
    """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, name, telecom,):
        """ Initialize all valid properties.
        """
        self.name = name
        self.telecom = telecom

    def __repr__(self):
        return '<SearchParameterContact %r>' % 'self.property'  # replace self.property


from . import contactpoint
from . import fhirdate