#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/NamingSystem)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class NamingSystem(domainresource.DomainResource):
    """ System of unique identification.

    A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """

    __tablename__ = "NamingSystem"

    contact = Column(NamingSystemContact)
    """ Contact details of the publisher.
        List of `NamingSystemContact` items (represented as `dict` in JSON). """

    date = Column(FHIRDate)
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

    replacedBy = Column(FHIRReference)
    """ Use this instead.
        Type `FHIRReference` referencing `NamingSystem` (represented as `dict` in JSON). """

    responsible = Column(primitives.StringField)
    """ Who maintains system namespace?.
        Type `str`. """

    status = Column(primitives.StringField)
    """ draft | active | retired.
        Type `str`. """

    type = Column(CodeableConcept)
    """ e.g. driver,  provider,  patient, bank etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """

    uniqueId = Column(NamingSystemUniqueId)
    """ Unique identifiers used for system.
        List of `NamingSystemUniqueId` items (represented as `dict` in JSON). """

    usage = Column(primitives.StringField)
    """ How/where is it used.
        Type `str`. """

    useContext = Column(CodeableConcept)
    """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, contact, date, description, kind, name, publisher, replacedBy, responsible, status, type, uniqueId, usage, useContext,):
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


from sqlalchemy import Column, Integer, String
from . import backboneelement

class NamingSystemContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    __tablename__ = "NamingSystemContact"

    name = Column(primitives.StringField)
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
        return '<NamingSystemContact %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class NamingSystemUniqueId(backboneelement.BackboneElement):
    """ Unique identifiers used for system.

    Indicates how the system may be identified when referenced in electronic
    exchange.
    """

    __tablename__ = "NamingSystemUniqueId"

    period = Column(Period)
    """ When is identifier valid?.
        Type `Period` (represented as `dict` in JSON). """

    preferred = Column(bool)
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


from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import period