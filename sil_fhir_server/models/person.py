#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Person)
#  Date: 2016-03-18.


from . import domainresource

class Person(domainresource.DomainResource):
    """ A generic person record.

    Demographics and administrative information about a person independent of a
    specific health-related context.
    """

    __tablename__ = "Person"

    active = Column()
    """ This person's record is in active use.
        Type `bool`. """

    address = Column(Address)
    """ One or more addresses for the person.
        List of `Address` items (represented as `dict` in JSON). """

    birthDate = Column()
    """ The date on which the person was born.
        Type `FHIRDate` (represented as `str` in JSON). """

    gender = Column()
    """ male | female | other | unknown.
        Type `str`. """

    identifier = Column(Identifier)
    """ A human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """

    link = Column(PersonLink)
    """ Link to a resource that concerns the same actual person.
        List of `PersonLink` items (represented as `dict` in JSON). """

    managingOrganization = Column()
    """ The organization that is the custodian of the person record.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    name = Column(HumanName)
    """ A name associated with the person.
        List of `HumanName` items (represented as `dict` in JSON). """

    photo = Column()
    """ Image of the person.
        Type `Attachment` (represented as `dict` in JSON). """

    telecom = Column(ContactPoint)
    """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, active, address, birthDate, gender, identifier, link, managingOrganization, name, photo, telecom,):
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


from . import backboneelement

class PersonLink(backboneelement.BackboneElement):
    """ Link to a resource that concerns the same actual person.
    """

    __tablename__ = "PersonLink"

    assurance = Column()
    """ level1 | level2 | level3 | level4.
        Type `str`. """

    target = Column()
    """ The resource to which this actual person is associated.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson, Person` (represented as `dict` in JSON). """

    def __init__(self, assurance, target,):
        """ Initialize all valid properties.
        """
        self.assurance = assurance
        self.target = target

    def __repr__(self):
        return '<PersonLink %r>' % 'self.property'  # replace self.property


from . import address
from . import attachment
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier