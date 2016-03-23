#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Patient)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class PatientAnimal(backboneelement.BackboneElement):
    """ This patient is known to be an animal (non-human).

    This patient is known to be an animal.
    """

    __tablename__ = "PatientAnimal"

    breed = Column(primitives.StringField,
                   ForeignKey('CodeableConcept.id'))
    """ E.g. Poodle, Angus.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    genderStatus = Column(primitives.StringField,
                          ForeignKey('CodeableConcept.id'))
    """ E.g. Neutered, Intact.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    species = Column(primitives.StringField,
                     ForeignKey('CodeableConcept.id'))
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


class PatientCommunication(backboneelement.BackboneElement):
    """ A list of Languages which may be used to communicate with the patient about
    his or her health.

    Languages which may be used to communicate with the patient about his or
    her health.
    """

    __tablename__ = "PatientCommunication"

    language = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ The language which can be used to communicate with the patient
        about his or her health.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    preferred = Column(primitives.BooleanField)
    """ Language preference indicator.
        Type `bool`. """

    def __init__(self, language, preferred,):
        """ Initialize all valid properties.
        """
        self.language = language
        self.preferred = preferred

    def __repr__(self):
        return '<PatientCommunication %r>' % 'self.property'  # replace self.property


class PatientContact(backboneelement.BackboneElement):
    """ A contact party (e.g. guardian, partner, friend) for the patient.
    """

    __tablename__ = "PatientContact"

    address = Column(primitives.StringField,
                     ForeignKey('Address.id'))
    """ Address for the contact person.
        Type `Address` (represented as `dict` in JSON). """

    gender = Column(primitives.StringField)
    """ male | female | other | unknown.
        Type `str`. """

    name = Column(primitives.StringField,
                  ForeignKey('HumanName.id'))
    """ A name associated with the contact person.
        Type `HumanName` (represented as `dict` in JSON). """

    # todo organization = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    organization = Column(primitives.StringField)
    """ Organization that is associated with the contact.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    period = Column(primitives.StringField,
                    ForeignKey('Period.id'))
    """ The period during which this contact person or organization is
        valid to be contacted relating to this patient.
        Type `Period` (represented as `dict` in JSON). """

    relationship = Column(primitives.StringField,
                          ForeignKey('CodeableConcept.id'))
    """ The kind of relationship.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    telecom = Column(primitives.StringField,
                     ForeignKey('ContactPoint.id'))
    """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, address, gender, name, organization, period,
                 relationship, telecom,):
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


class PatientLink(backboneelement.BackboneElement):
    """ Link to another patient resource that concerns the same actual person.

    Link to another patient resource that concerns the same actual patient.
    """

    __tablename__ = "PatientLink"

    # todo other = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    other = Column(primitives.StringField)
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


class Patient(domainresource.DomainResource):
    """ Information about an individual or animal receiving health care services.

    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """

    __tablename__ = "Patient"
    
    active = Column(primitives.BooleanField)
    """ Whether this patient's record is in active use.
        Type `bool`. """
    
    address = Column(primitives.StringField,
                     ForeignKey('Address.id'))
    """ Addresses for the individual.
        List of `Address` items (represented as `dict` in JSON). """
    
    animal = Column(primitives.StringField,
                    ForeignKey('PatientAnimal.id'))
    """ This patient is known to be an animal (non-human).
        Type `PatientAnimal` (represented as `dict` in JSON). """
    
    birthDate = Column(primitives.DateTimeField)
    """ The date of birth for the individual.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    # todo careProvider = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    careProvider = Column(primitives.StringField)
    """ Patient's nominated primary care provider.
        List of `FHIRReference` items referencing `Organization,
        Practitioner` (represented as `dict` in JSON). """
    
    communication = Column(primitives.StringField,
                           ForeignKey('PatientCommunication.id'))
    """ A list of Languages which may be used to communicate with the
        patient about his or her health.
        List of `PatientCommunication` items (represented as `dict` in JSON). """
    
    contact = Column(primitives.StringField,
                     ForeignKey('PatientContact.id'))
    """ A contact party (e.g. guardian, partner, friend) for the patient.
        List of `PatientContact` items (represented as `dict` in JSON). """
    
    deceasedBoolean = Column(primitives.BooleanField)
    """ Indicates if the individual is deceased or not.
        Type `bool`. """
    
    deceasedDateTime = Column(primitives.DateTimeField)
    """ Indicates if the individual is deceased or not.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    gender = Column(primitives.StringField)
    """ male | female | other | unknown.
        Type `str`. """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ An identifier for this patient.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    link = Column(primitives.StringField,
                  ForeignKey('PatientLink.id'))
    """ Link to another patient resource that concerns the same actual
        person.
        List of `PatientLink` items (represented as `dict` in JSON). """
    
    # todo managingOrganization = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    managingOrganization = Column(primitives.StringField)
    """ Organization that is the custodian of the patient record.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
    
    maritalStatus = Column(primitives.StringField,
                           ForeignKey('CodeableConcept.id'))
    """ Marital (civil) status of a patient.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    multipleBirthBoolean = Column(primitives.BooleanField)
    """ Whether patient is part of a multiple birth.
        Type `bool`. """
    
    multipleBirthInteger = Column(primitives.IntegerField)
    """ Whether patient is part of a multiple birth.
        Type `int`. """
    
    name = Column(primitives.StringField,
                  ForeignKey('HumanName.id'))
    """ A name associated with the patient.
        List of `HumanName` items (represented as `dict` in JSON). """
    
    photo = Column(primitives.StringField,
                   ForeignKey('Attachment.id'))
    """ Image of the patient.
        List of `Attachment` items (represented as `dict` in JSON). """
    
    telecom = Column(primitives.StringField,
                     ForeignKey('ContactPoint.id'))
    """ A contact detail for the individual.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, active, address, animal, birthDate, careProvider,
                 communication, contact, deceasedBoolean, deceasedDateTime,
                 gender, identifier, link, managingOrganization,
                 maritalStatus, multipleBirthBoolean, multipleBirthInteger,
                 name, photo, telecom,):
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
