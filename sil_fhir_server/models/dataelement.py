#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DataElement)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class DataElementContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    __tablename__ = "DataElementContact"

    name = Column(primitives.StringField)
    """ Name of a individual to contact.
        Type `str`. """

    telecom = Column(primitives.StringField,
                     ForeignKey('ContactPoint.id'))
    """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, name, telecom,):
        """ Initialize all valid properties.
        """
        self.name = name
        self.telecom = telecom

    def __repr__(self):
        return '<DataElementContact %r>' % 'self.property'  # replace self.property


class DataElementMapping(backboneelement.BackboneElement):
    """ External specification mapped to.

    Identifies a specification (other than a terminology) that the elements
    which make up the DataElement have some correspondence with.
    """

    __tablename__ = "DataElementMapping"

    comments = Column(primitives.StringField)
    """ Versions, Issues, Scope limitations etc..
        Type `str`. """

    identity = Column(primitives.StringField)
    """ Internal id when this mapping is used.
        Type `str`. """

    name = Column(primitives.StringField)
    """ Names what this mapping refers to.
        Type `str`. """

    uri = Column(primitives.StringField)
    """ Identifies what this mapping refers to.
        Type `str`. """

    def __init__(self, comments, identity, name, uri,):
        """ Initialize all valid properties.
        """
        self.comments = comments
        self.identity = identity
        self.name = name
        self.uri = uri

    def __repr__(self):
        return '<DataElementMapping %r>' % 'self.property'  # replace self.property


class DataElement(domainresource.DomainResource):
    """ Resource data element.

    The formal description of a single piece of information that can be
    gathered and reported.
    """

    __tablename__ = "DataElement"
    
    contact = Column(primitives.StringField,
                     ForeignKey('DataElementContact.id'))
    """ Contact details of the publisher.
        List of `DataElementContact` items (represented as `dict` in JSON). """
    
    copyright = Column(primitives.StringField)
    """ Use and/or publishing restrictions.
        Type `str`. """
    
    date = Column(primitives.DateTimeField)
    """ Date for this version of the data element.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    element = Column(primitives.StringField,
                     ForeignKey('ElementDefinition.id'))
    """ Definition of element.
        List of `ElementDefinition` items (represented as `dict` in JSON). """
    
    experimental = Column(primitives.BooleanField)
    """ If for testing purposes, not real usage.
        Type `bool`. """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Logical id to reference this data element.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    mapping = Column(primitives.StringField,
                     ForeignKey('DataElementMapping.id'))
    """ External specification mapped to.
        List of `DataElementMapping` items (represented as `dict` in JSON). """
    
    name = Column(primitives.StringField)
    """ Descriptive label for this element definition.
        Type `str`. """
    
    publisher = Column(primitives.StringField)
    """ Name of the publisher (Organization or individual).
        Type `str`. """
    
    status = Column(primitives.StringField)
    """ draft | active | retired.
        Type `str`. """
    
    stringency = Column(primitives.StringField)
    """ comparable | fully-specified | equivalent | convertable | scaleable
        | flexible.
        Type `str`. """
    
    url = Column(primitives.StringField)
    """ Globally unique logical id for data element.
        Type `str`. """
    
    useContext = Column(primitives.StringField,
                        ForeignKey('CodeableConcept.id'))
    """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    version = Column(primitives.StringField)
    """ Logical id for this version of the data element.
        Type `str`. """

    def __init__(self, contact, copyright, date, element, experimental,
                 identifier, mapping, name, publisher, status,
                 stringency, url, useContext, version):
        """ Initialize all valid properties.
        """
        self.contact = contact
        self.copyright = copyright
        self.date = date
        self.element = element
        self.experimental = experimental
        self.identifier = identifier
        self.mapping = mapping
        self.name = name
        self.publisher = publisher
        self.status = status
        self.stringency = stringency
        self.url = url
        self.useContext = useContext
        self.version = version

    def __repr__(self):
        return '<DataElement %r>' % 'self.property'  # replace self.property
