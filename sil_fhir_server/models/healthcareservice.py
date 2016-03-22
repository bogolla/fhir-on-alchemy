#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/HealthcareService)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class HealthcareService(domainresource.DomainResource):
    """ The details of a healthcare service available at a location.
    """

    __tablename__ = "HealthcareService"

    appointmentRequired = Column(bool)
    """ If an appointment is required for access to this service.
        Type `bool`. """

    availabilityExceptions = Column(primitives.StringField)
    """ Description of availability exceptions.
        Type `str`. """

    availableTime = Column(HealthcareServiceAvailableTime)
    """ Times the Service Site is available.
        List of `HealthcareServiceAvailableTime` items (represented as `dict` in JSON). """

    characteristic = Column(CodeableConcept)
    """ Collection of characteristics (attributes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    comment = Column(primitives.StringField)
    """ Additional description and/or any specific issues not covered
        elsewhere.
        Type `str`. """

    coverageArea = Column(FHIRReference)
    """ Location(s) service is inteded for/available to.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """

    eligibility = Column(CodeableConcept)
    """ Specific eligibility requirements required to use the service.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    eligibilityNote = Column(primitives.StringField)
    """ Describes the eligibility conditions for the service.
        Type `str`. """

    extraDetails = Column(primitives.StringField)
    """ Extra details about the service that can't be placed in the other
        fields.
        Type `str`. """

    identifier = Column(Identifier)
    """ External identifiers for this item.
        List of `Identifier` items (represented as `dict` in JSON). """

    location = Column(FHIRReference)
    """ Location where service may be provided.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """

    notAvailable = Column(HealthcareServiceNotAvailable)
    """ Not available during this time due to provided reason.
        List of `HealthcareServiceNotAvailable` items (represented as `dict` in JSON). """

    photo = Column(Attachment)
    """ Facilitates quick identification of the service.
        Type `Attachment` (represented as `dict` in JSON). """

    programName = Column(primitives.StringField)
    """ Program Names that categorize the service.
        List of `str` items. """

    providedBy = Column(FHIRReference)
    """ Organization that provides this service.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    publicKey = Column(primitives.StringField)
    """ PKI Public keys to support secure communications.
        Type `str`. """

    referralMethod = Column(CodeableConcept)
    """ Ways that the service accepts referrals.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    serviceCategory = Column(CodeableConcept)
    """ Broad category of service being performed or delivered.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    serviceName = Column(primitives.StringField)
    """ Description of service as presented to a consumer while searching.
        Type `str`. """

    serviceProvisionCode = Column(CodeableConcept)
    """ Conditions under which service is available/offered.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    serviceType = Column(HealthcareServiceServiceType)
    """ Specific service delivered or performed.
        List of `HealthcareServiceServiceType` items (represented as `dict` in JSON). """

    telecom = Column(ContactPoint)
    """ Contacts related to the healthcare service.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, appointmentRequired, availabilityExceptions, availableTime, characteristic, comment, coverageArea, eligibility, eligibilityNote, extraDetails, identifier, location, notAvailable, photo, programName, providedBy, publicKey, referralMethod, serviceCategory, serviceName, serviceProvisionCode, serviceType, telecom,):
        """ Initialize all valid properties.
        """
        self.appointmentRequired = appointmentRequired
        self.availabilityExceptions = availabilityExceptions
        self.availableTime = availableTime
        self.characteristic = characteristic
        self.comment = comment
        self.coverageArea = coverageArea
        self.eligibility = eligibility
        self.eligibilityNote = eligibilityNote
        self.extraDetails = extraDetails
        self.identifier = identifier
        self.location = location
        self.notAvailable = notAvailable
        self.photo = photo
        self.programName = programName
        self.providedBy = providedBy
        self.publicKey = publicKey
        self.referralMethod = referralMethod
        self.serviceCategory = serviceCategory
        self.serviceName = serviceName
        self.serviceProvisionCode = serviceProvisionCode
        self.serviceType = serviceType
        self.telecom = telecom

    def __repr__(self):
        return '<HealthcareService %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class HealthcareServiceAvailableTime(backboneelement.BackboneElement):
    """ Times the Service Site is available.

    A collection of times that the Service Site is available.
    """

    __tablename__ = "HealthcareServiceAvailableTime"

    allDay = Column(bool)
    """ Always available? e.g. 24 hour service.
        Type `bool`. """

    availableEndTime = Column(FHIRDate)
    """ Closing time of day (ignored if allDay = true).
        Type `FHIRDate` (represented as `str` in JSON). """

    availableStartTime = Column(FHIRDate)
    """ Opening time of day (ignored if allDay = true).
        Type `FHIRDate` (represented as `str` in JSON). """

    daysOfWeek = Column(primitives.StringField)
    """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """

    def __init__(self, allDay, availableEndTime, availableStartTime, daysOfWeek,):
        """ Initialize all valid properties.
        """
        self.allDay = allDay
        self.availableEndTime = availableEndTime
        self.availableStartTime = availableStartTime
        self.daysOfWeek = daysOfWeek

    def __repr__(self):
        return '<HealthcareServiceAvailableTime %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class HealthcareServiceNotAvailable(backboneelement.BackboneElement):
    """ Not available during this time due to provided reason.

    The HealthcareService is not available during this period of time due to
    the provided reason.
    """

    __tablename__ = "HealthcareServiceNotAvailable"

    description = Column(primitives.StringField)
    """ Reason presented to the user explaining why time not available.
        Type `str`. """

    during = Column(Period)
    """ Service not availablefrom this date.
        Type `Period` (represented as `dict` in JSON). """

    def __init__(self, description, during,):
        """ Initialize all valid properties.
        """
        self.description = description
        self.during = during

    def __repr__(self):
        return '<HealthcareServiceNotAvailable %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class HealthcareServiceServiceType(backboneelement.BackboneElement):
    """ Specific service delivered or performed.

    A specific type of service that may be delivered or performed.
    """

    __tablename__ = "HealthcareServiceServiceType"

    specialty = Column(CodeableConcept)
    """ Specialties handled by the Service Site.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    type = Column(CodeableConcept)
    """ Type of service delivered or performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, specialty, type,):
        """ Initialize all valid properties.
        """
        self.specialty = specialty
        self.type = type

    def __repr__(self):
        return '<HealthcareServiceServiceType %r>' % 'self.property'  # replace self.property


from . import attachment
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period