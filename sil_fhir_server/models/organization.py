#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Organization)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class OrganizationContact(backboneelement.BackboneElement):
    """ Contact for the organization for a certain purpose.
    """

    __tablename__ = "OrganizationContact"

    address = Column(primitives.StringField,
                     ForeignKey('Address.id'))
    """ Visiting or postal addresses for the contact.
        Type `Address` (represented as `dict` in JSON). """

    name = Column(primitives.StringField,
                  ForeignKey('HumanName.id'))
    """ A name associated with the contact.
        Type `HumanName` (represented as `dict` in JSON). """

    purpose = Column(primitives.StringField,
                     ForeignKey('CodeableConcept.id'))
    """ The type of contact.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    telecom = Column(primitives.StringField,
                     ForeignKey('ContactPoint.id'))
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


class Organization(domainresource.DomainResource):
    """ A grouping of people or organizations with a common purpose.

    A formally or informally recognized grouping of people or organizations
    formed for the purpose of achieving some form of collective action.
    Includes companies, institutions, corporations, departments, community
    groups, healthcare practice groups, etc.
    """

    __tablename__ = "Organization"
    
    active = Column(primitives.BooleanField)
    """ Whether the organization's record is still in active use.
        Type `bool`. """
    
    address = Column(primitives.StringField,
                     ForeignKey('Address.id'))
    """ An address for the organization.
        List of `Address` items (represented as `dict` in JSON). """
    
    contact = Column(primitives.StringField,
                     ForeignKey('OrganizationContact.id'))
    """ Contact for the organization for a certain purpose.
        List of `OrganizationContact` items (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Identifies this organization  across multiple systems.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    name = Column(primitives.StringField)
    """ Name used for the organization.
        Type `str`. """
    
    # todo partOf = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    partOf = Column(primitives.StringField)
    """ The organization of which this organization forms a part.
        Type `FHIRReference` referencing `Organization`
        (represented as `dict` in JSON). """
    
    telecom = Column(primitives.StringField,
                     ForeignKey('ContactPoint.id'))
    """ A contact detail for the organization.
        List of `ContactPoint` items (represented as `dict` in JSON). """
    
    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Kind of organization.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, active, address, contact, identifier, name,
                 partOf, telecom, type,):
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
