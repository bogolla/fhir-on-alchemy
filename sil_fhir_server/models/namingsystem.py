#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/NamingSystem)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class NamingSystemContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    __tablename__ = "NamingSystemContact"

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
        return '<NamingSystemContact %r>' % 'self.property'  # replace self.property


class NamingSystemUniqueId(backboneelement.BackboneElement):
    """ Unique identifiers used for system.

    Indicates how the system may be identified when referenced in electronic
    exchange.
    """

    __tablename__ = "NamingSystemUniqueId"

    period = Column(primitives.StringField,
                    ForeignKey('Period.id'))
    """ When is identifier valid?.
        Type `Period` (represented as `dict` in JSON). """

    preferred = Column(primitives.BooleanField)
    """ Is this the id that should be used for this type.
        Type `bool`. """

    type = Column(primitives.StringField)
    """ oid | uuid | uri | other.
        Type `str`. """

    value = Column(primitives.StringField)
    """ The unique identifier.
        Type `str`. """

    def __init__(self, period, preferred, type, value,):
        """ Initialize all valid properties.
        """
        self.period = period
        self.preferred = preferred
        self.type = type
        self.value = value

    def __repr__(self):
        return '<NamingSystemUniqueId %r>' % 'self.property'  # replace self.property


class NamingSystem(domainresource.DomainResource):
    """ System of unique identification.

    A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """

    __tablename__ = "NamingSystem"
    
    contact = Column(primitives.StringField,
                     ForeignKey('NamingSystemContact.id'))
    """ Contact details of the publisher.
        List of `NamingSystemContact` items (represented as `dict` in JSON). """
    
    date = Column(primitives.DateTimeField)
    """ Publication Date(/time).
        Type `FHIRDate` (represented as `str` in JSON). """
    
    description = Column(primitives.StringField)
    """ What does naming system identify?.
        Type `str`. """
    
    kind = Column(primitives.StringField)
    """ codesystem | identifier | root.
        Type `str`. """
    
    name = Column(primitives.StringField)
    """ Human-readable label.
        Type `str`. """
    
    publisher = Column(primitives.StringField)
    """ Name of the publisher (Organization or individual).
        Type `str`. """
    
    # todo replacedBy = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    replacedBy = Column(primitives.StringField)
    """ Use this instead.
        Type `FHIRReference` referencing `NamingSystem` (represented as `dict` in JSON). """
    
    responsible = Column(primitives.StringField)
    """ Who maintains system namespace?.
        Type `str`. """
    
    status = Column(primitives.StringField)
    """ draft | active | retired.
        Type `str`. """
    
    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ e.g. driver,  provider,  patient, bank etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    uniqueId = Column(primitives.StringField,
                      ForeignKey('NamingSystemUniqueId.id'))
    """ Unique identifiers used for system.
        List of `NamingSystemUniqueId` items (represented as `dict` in JSON). """
    
    usage = Column(primitives.StringField)
    """ How/where is it used.
        Type `str`. """
    
    useContext = Column(primitives.StringField,
                        ForeignKey('CodeableConcept.id'))
    """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, contact, date, description, kind, name,
                 publisher, replacedBy, responsible, status,
                 type, uniqueId, usage, useContext):
        """ Initialize all valid properties.
        """
        self.contact = contact
        self.date = date
        self.description = description
        self.kind = kind
        self.name = name
        self.publisher = publisher
        self.replacedBy = replacedBy
        self.responsible = responsible
        self.status = status
        self.type = type
        self.uniqueId = uniqueId
        self.usage = usage
        self.useContext = useContext

    def __repr__(self):
        return '<NamingSystem %r>' % 'self.property'  # replace self.property
