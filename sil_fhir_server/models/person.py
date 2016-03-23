#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Person)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class PersonLink(backboneelement.BackboneElement):
    """ Link to a resource that concerns the same actual person.
    """

    __tablename__ = "PersonLink"

    assurance = Column(primitives.StringField)
    """ level1 | level2 | level3 | level4.
        Type `str`. """

    # todo    target = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    target = Column(primitives.StringField)
    """ The resource to which this actual person is associated.
        Type `FHIRReference` referencing `Patient, Practitioner,
        RelatedPerson, Person` (represented as `dict` in JSON). """

    def __init__(self, assurance, target,):
        """ Initialize all valid properties.
        """
        self.assurance = assurance
        self.target = target

    def __repr__(self):
        return '<PersonLink %r>' % 'self.property'  # replace self.property


class Person(domainresource.DomainResource):
    """ A generic person record.

    Demographics and administrative information about a person independent of a
    specific health-related context.
    """

    __tablename__ = "Person"
    
    active = Column(primitives.BooleanField)
    """ This person's record is in active use.
        Type `bool`. """
    
    address = Column(primitives.StringField,
                     ForeignKey('Address.id'))
    """ One or more addresses for the person.
        List of `Address` items (represented as `dict` in JSON). """
    
    birthDate = Column(primitives.DateTimeField)
    """ The date on which the person was born.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    gender = Column(primitives.StringField)
    """ male | female | other | unknown.
        Type `str`. """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ A human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    link = Column(primitives.StringField,
                  ForeignKey('PersonLink.id'))
    """ Link to a resource that concerns the same actual person.
        List of `PersonLink` items (represented as `dict` in JSON). """
    
    # todo managingOrganization = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    managingOrganization = Column(primitives.StringField)
    """ The organization that is the custodian of the person record.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
    
    name = Column(primitives.StringField,
                  ForeignKey('HumanName.id'))
    """ A name associated with the person.
        List of `HumanName` items (represented as `dict` in JSON). """
    
    photo = Column(primitives.StringField,
                   ForeignKey('Attachment.id'))
    """ Image of the person.
        Type `Attachment` (represented as `dict` in JSON). """
    
    telecom = Column(primitives.StringField,
                     ForeignKey('ContactPoint.id'))
    """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, active, address, birthDate, gender, identifier, link,
                 managingOrganization, name, photo, telecom,):
        """ Initialize all valid properties.
        """
        self.active = active
        self.address = address
        self.birthDate = birthDate
        self.gender = gender
        self.identifier = identifier
        self.link = link
        self.managingOrganization = managingOrganization
        self.name = name
        self.photo = photo
        self.telecom = telecom

    def __repr__(self):
        return '<Person %r>' % 'self.property'  # replace self.property
