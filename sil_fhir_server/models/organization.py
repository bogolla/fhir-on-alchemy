#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Organization)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class Organization(domainresource.DomainResource):
    """ A grouping of people or organizations with a common purpose.

    A formally or informally recognized grouping of people or organizations
    formed for the purpose of achieving some form of collective action.
    Includes companies, institutions, corporations, departments, community
    groups, healthcare practice groups, etc.
    """

    __tablename__ = "Organization"

    active = Column(bool)
    """ Whether the organization's record is still in active use.
        Type `bool`. """

    address = Column(Address)
    """ An address for the organization.
        List of `Address` items (represented as `dict` in JSON). """

    contact = Column(OrganizationContact)
    """ Contact for the organization for a certain purpose.
        List of `OrganizationContact` items (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Identifies this organization  across multiple systems.
        List of `Identifier` items (represented as `dict` in JSON). """

    name = Column(primitives.StringField)
    """ Name used for the organization.
        Type `str`. """

    partOf = Column(FHIRReference)
    """ The organization of which this organization forms a part.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    telecom = Column(ContactPoint)
    """ A contact detail for the organization.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    type = Column(CodeableConcept)
    """ Kind of organization.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, active, address, contact, identifier, name, partOf, telecom, type,):
        """ Initialize all valid properties.
        """
        self.active = active
        self.address = address
        self.contact = contact
        self.identifier = identifier
        self.name = name
        self.partOf = partOf
        self.telecom = telecom
        self.type = type

    def __repr__(self):
        return '<Organization %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class OrganizationContact(backboneelement.BackboneElement):
    """ Contact for the organization for a certain purpose.
    """

    __tablename__ = "OrganizationContact"

    address = Column(Address)
    """ Visiting or postal addresses for the contact.
        Type `Address` (represented as `dict` in JSON). """

    name = Column(HumanName)
    """ A name associated with the contact.
        Type `HumanName` (represented as `dict` in JSON). """

    purpose = Column(CodeableConcept)
    """ The type of contact.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    telecom = Column(ContactPoint)
    """ Contact details (telephone, email, etc.)  for a contact.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, address, name, purpose, telecom,):
        """ Initialize all valid properties.
        """
        self.address = address
        self.name = name
        self.purpose = purpose
        self.telecom = telecom

    def __repr__(self):
        return '<OrganizationContact %r>' % 'self.property'  # replace self.property


from . import address
from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import humanname
from . import identifier