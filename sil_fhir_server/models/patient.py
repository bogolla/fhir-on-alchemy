#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Patient)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class Patient(domainresource.DomainResource):
    """ Information about an individual or animal receiving health care services.

    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """

    __tablename__ = "Patient"

    active = Column(bool)
    """ Whether this patient's record is in active use.
        Type `bool`. """

    address = Column(Address)
    """ Addresses for the individual.
        List of `Address` items (represented as `dict` in JSON). """

    animal = Column(PatientAnimal)
    """ This patient is known to be an animal (non-human).
        Type `PatientAnimal` (represented as `dict` in JSON). """

    birthDate = Column(FHIRDate)
    """ The date of birth for the individual.
        Type `FHIRDate` (represented as `str` in JSON). """

    careProvider = Column(FHIRReference)
    """ Patient's nominated primary care provider.
        List of `FHIRReference` items referencing `Organization, Practitioner` (represented as `dict` in JSON). """

    communication = Column(PatientCommunication)
    """ A list of Languages which may be used to communicate with the
        patient about his or her health.
        List of `PatientCommunication` items (represented as `dict` in JSON). """

    contact = Column(PatientContact)
    """ A contact party (e.g. guardian, partner, friend) for the patient.
        List of `PatientContact` items (represented as `dict` in JSON). """

    deceasedBoolean = Column(bool)
    """ Indicates if the individual is deceased or not.
        Type `bool`. """

    deceasedDateTime = Column(FHIRDate)
    """ Indicates if the individual is deceased or not.
        Type `FHIRDate` (represented as `str` in JSON). """

    gender = Column(primitives.StringField)
    """ male | female | other | unknown.
        Type `str`. """

    identifier = Column(Identifier)
    """ An identifier for this patient.
        List of `Identifier` items (represented as `dict` in JSON). """

    link = Column(PatientLink)
    """ Link to another patient resource that concerns the same actual
        person.
        List of `PatientLink` items (represented as `dict` in JSON). """

    managingOrganization = Column(FHIRReference)
    """ Organization that is the custodian of the patient record.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    maritalStatus = Column(CodeableConcept)
    """ Marital (civil) status of a patient.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    multipleBirthBoolean = Column(bool)
    """ Whether patient is part of a multiple birth.
        Type `bool`. """

    multipleBirthInteger = Column(Integer)
    """ Whether patient is part of a multiple birth.
        Type `int`. """

    name = Column(HumanName)
    """ A name associated with the patient.
        List of `HumanName` items (represented as `dict` in JSON). """

    photo = Column(Attachment)
    """ Image of the patient.
        List of `Attachment` items (represented as `dict` in JSON). """

    telecom = Column(ContactPoint)
    """ A contact detail for the individual.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, active, address, animal, birthDate, careProvider, communication, contact, deceasedBoolean, deceasedDateTime, gender, identifier, link, managingOrganization, maritalStatus, multipleBirthBoolean, multipleBirthInteger, name, photo, telecom,):
        """ Initialize all valid properties.
        """
        self.active = active
        self.address = address
        self.animal = animal
        self.birthDate = birthDate
        self.careProvider = careProvider
        self.communication = communication
        self.contact = contact
        self.deceasedBoolean = deceasedBoolean
        self.deceasedDateTime = deceasedDateTime
        self.gender = gender
        self.identifier = identifier
        self.link = link
        self.managingOrganization = managingOrganization
        self.maritalStatus = maritalStatus
        self.multipleBirthBoolean = multipleBirthBoolean
        self.multipleBirthInteger = multipleBirthInteger
        self.name = name
        self.photo = photo
        self.telecom = telecom

    def __repr__(self):
        return '<Patient %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class PatientAnimal(backboneelement.BackboneElement):
    """ This patient is known to be an animal (non-human).

    This patient is known to be an animal.
    """

    __tablename__ = "PatientAnimal"

    breed = Column(CodeableConcept)
    """ E.g. Poodle, Angus.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    genderStatus = Column(CodeableConcept)
    """ E.g. Neutered, Intact.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    species = Column(CodeableConcept)
    """ E.g. Dog, Cow.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, breed, genderStatus, species,):
        """ Initialize all valid properties.
        """
        self.breed = breed
        self.genderStatus = genderStatus
        self.species = species

    def __repr__(self):
        return '<PatientAnimal %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class PatientCommunication(backboneelement.BackboneElement):
    """ A list of Languages which may be used to communicate with the patient about
    his or her health.

    Languages which may be used to communicate with the patient about his or
    her health.
    """

    __tablename__ = "PatientCommunication"

    language = Column(CodeableConcept)
    """ The language which can be used to communicate with the patient
        about his or her health.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    preferred = Column(bool)
    """ Language preference indicator.
        Type `bool`. """

    def __init__(self, language, preferred,):
        """ Initialize all valid properties.
        """
        self.language = language
        self.preferred = preferred

    def __repr__(self):
        return '<PatientCommunication %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class PatientContact(backboneelement.BackboneElement):
    """ A contact party (e.g. guardian, partner, friend) for the patient.
    """

    __tablename__ = "PatientContact"

    address = Column(Address)
    """ Address for the contact person.
        Type `Address` (represented as `dict` in JSON). """

    gender = Column(primitives.StringField)
    """ male | female | other | unknown.
        Type `str`. """

    name = Column(HumanName)
    """ A name associated with the contact person.
        Type `HumanName` (represented as `dict` in JSON). """

    organization = Column(FHIRReference)
    """ Organization that is associated with the contact.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    period = Column(Period)
    """ The period during which this contact person or organization is
        valid to be contacted relating to this patient.
        Type `Period` (represented as `dict` in JSON). """

    relationship = Column(CodeableConcept)
    """ The kind of relationship.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    telecom = Column(ContactPoint)
    """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, address, gender, name, organization, period, relationship, telecom,):
        """ Initialize all valid properties.
        """
        self.address = address
        self.gender = gender
        self.name = name
        self.organization = organization
        self.period = period
        self.relationship = relationship
        self.telecom = telecom

    def __repr__(self):
        return '<PatientContact %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class PatientLink(backboneelement.BackboneElement):
    """ Link to another patient resource that concerns the same actual person.

    Link to another patient resource that concerns the same actual patient.
    """

    __tablename__ = "PatientLink"

    other = Column(FHIRReference)
    """ The other patient resource that the link refers to.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    type = Column(primitives.StringField)
    """ replace | refer | seealso - type of link.
        Type `str`. """

    def __init__(self, other, type,):
        """ Initialize all valid properties.
        """
        self.other = other
        self.type = type

    def __repr__(self):
        return '<PatientLink %r>' % 'self.property'  # replace self.property


from . import address
from . import attachment
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import period