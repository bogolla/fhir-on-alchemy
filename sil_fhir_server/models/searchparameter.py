#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/SearchParameter)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource

class SearchParameter(domainresource.DomainResource):
    """ Search Parameter for a resource.

    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """

    __tablename__ = "SearchParameter"
    
    base = Column(primitives.StringField)
    """ The resource type this search parameter applies to.
        Type `str`. """
    
    code = Column(primitives.StringField)
    """ Code used in URL.
        Type `str`. """
    
    contact = Column(primitives.StringField, ForeignKey('SearchParameterContact.id'))
    """ Contact details of the publisher.
        List of `SearchParameterContact` items (represented as `dict` in JSON). """
    
    date = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ Publication Date(/time).
        Type `FHIRDate` (represented as `str` in JSON). """
    
    description = Column(primitives.StringField)
    """ Documentation for  search parameter.
        Type `str`. """
    
    experimental = Column(primitives.BooleanField)
    """ If for testing purposes, not real usage.
        Type `bool`. """
    
    name = Column(primitives.StringField)
    """ Informal name for this search parameter.
        Type `str`. """
    
    publisher = Column(primitives.StringField)
    """ Name of the publisher (Organization or individual).
        Type `str`. """
    
    requirements = Column(primitives.StringField)
    """ Why this search parameter is defined.
        Type `str`. """
    
    status = Column(primitives.StringField)
    """ draft | active | retired.
        Type `str`. """
    
    target = Column(primitives.StringField)
    """ Types of resource (if a resource reference).
        List of `str` items. """
    
    type = Column(primitives.StringField)
    """ number | date | string | token | reference | composite | quantity |
        uri.
        Type `str`. """
    
    url = Column(primitives.StringField)
    """ Absolute URL used to reference this search parameter.
        Type `str`. """
    
    xpath = Column(primitives.StringField)
    """ XPath that extracts the values.
        Type `str`. """
    
    xpathUsage = Column(primitives.StringField)
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


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import backboneelement

class SearchParameterContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    __tablename__ = "SearchParameterContact"
    
    name = Column(primitives.StringField)
    """ Name of a individual to contact.
        Type `str`. """
    
    telecom = Column(primitives.StringField, ForeignKey('ContactPoint.id'))
    """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, name, telecom,):
        """ Initialize all valid properties.
        """
        self.name = name
        self.telecom = telecom

    def __repr__(self):
        return '<SearchParameterContact %r>' % 'self.property'  # replace self.property