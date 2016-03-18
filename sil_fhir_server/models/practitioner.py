#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Practitioner)
#  Date: 2016-03-18.


from . import domainresource

class Practitioner(domainresource.DomainResource):
    """ A person with a  formal responsibility in the provisioning of healthcare or
    related services.

    A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """

    __tablename__ = "Practitioner"

    active = Column()
    """ Whether this practitioner's record is in active use.
        Type `bool`. """

    address = Column(Address)
    """ Where practitioner can be found/visited.
        List of `Address` items (represented as `dict` in JSON). """

    birthDate = Column()
    """ The date  on which the practitioner was born.
        Type `FHIRDate` (represented as `str` in JSON). """

    communication = Column(CodeableConcept)
    """ A language the practitioner is able to use in patient communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    gender = Column()
    """ male | female | other | unknown.
        Type `str`. """

    identifier = Column(Identifier)
    """ A identifier for the person as this agent.
        List of `Identifier` items (represented as `dict` in JSON). """

    name = Column()
    """ A name associated with the person.
        Type `HumanName` (represented as `dict` in JSON). """

    photo = Column(Attachment)
    """ Image of the person.
        List of `Attachment` items (represented as `dict` in JSON). """

    practitionerRole = Column(PractitionerPractitionerRole)
    """ Roles/organizations the practitioner is associated with.
        List of `PractitionerPractitionerRole` items (represented as `dict` in JSON). """

    qualification = Column(PractitionerQualification)
    """ Qualifications obtained by training and certification.
        List of `PractitionerQualification` items (represented as `dict` in JSON). """

    telecom = Column(ContactPoint)
    """ A contact detail for the practitioner.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, active, address, birthDate, communication, gender, identifier, name, photo, practitionerRole, qualification, telecom,):
        """ Initialize all valid properties.
        """
        self.active = active
        self.address = address
        self.birthDate = birthDate
        self.communication = communication
        self.gender = gender
        self.identifier = identifier
        self.name = name
        self.photo = photo
        self.practitionerRole = practitionerRole
        self.qualification = qualification
        self.telecom = telecom

    def __repr__(self):
        return '<Practitioner %r>' % 'self.property'  # replace self.property


from . import backboneelement

class PractitionerPractitionerRole(backboneelement.BackboneElement):
    """ Roles/organizations the practitioner is associated with.

    The list of roles/organizations that the practitioner is associated with.
    """

    __tablename__ = "PractitionerPractitionerRole"

    healthcareService = Column(FHIRReference)
    """ The list of healthcare services that this worker provides for this
        role's Organization/Location(s).
        List of `FHIRReference` items referencing `HealthcareService` (represented as `dict` in JSON). """

    location = Column(FHIRReference)
    """ The location(s) at which this practitioner provides care.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """

    managingOrganization = Column()
    """ Organization where the roles are performed.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    period = Column()
    """ The period during which the practitioner is authorized to perform
        in these role(s).
        Type `Period` (represented as `dict` in JSON). """

    role = Column()
    """ Roles which this practitioner may perform.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    specialty = Column(CodeableConcept)
    """ Specific specialty of the practitioner.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, healthcareService, location, managingOrganization, period, role, specialty,):
        """ Initialize all valid properties.
        """
        self.healthcareService = healthcareService
        self.location = location
        self.managingOrganization = managingOrganization
        self.period = period
        self.role = role
        self.specialty = specialty

    def __repr__(self):
        return '<PractitionerPractitionerRole %r>' % 'self.property'  # replace self.property


class PractitionerQualification(backboneelement.BackboneElement):
    """ Qualifications obtained by training and certification.
    """

    __tablename__ = "PractitionerQualification"

    code = Column()
    """ Coded representation of the qualification.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ An identifier for this qualification for the practitioner.
        List of `Identifier` items (represented as `dict` in JSON). """

    issuer = Column()
    """ Organization that regulates and issues the qualification.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    period = Column()
    """ Period during which the qualification is valid.
        Type `Period` (represented as `dict` in JSON). """

    def __init__(self, code, identifier, issuer, period,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.identifier = identifier
        self.issuer = issuer
        self.period = period

    def __repr__(self):
        return '<PractitionerQualification %r>' % 'self.property'  # replace self.property


from . import address
from . import attachment
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import period