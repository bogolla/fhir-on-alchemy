#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/HealthcareService)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class HealthcareServiceAvailableTime(backboneelement.BackboneElement):
    """ Times the Service Site is available.

    A collection of times that the Service Site is available.
    """

    __tablename__ = "HealthcareServiceAvailableTime"

    allDay = Column(primitives.BooleanField)
    """ Always available? e.g. 24 hour service.
        Type `bool`. """

    availableEndTime = Column(primitives.DateTimeField)
    """ Closing time of day (ignored if allDay = true).
        Type `FHIRDate` (represented as `str` in JSON). """

    availableStartTime = Column(primitives.DateTimeField)
    """ Opening time of day (ignored if allDay = true).
        Type `FHIRDate` (represented as `str` in JSON). """

    daysOfWeek = Column(primitives.StringField)
    """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """

    def __init__(self, allDay, availableEndTime, availableStartTime,
                 daysOfWeek,):
        """ Initialize all valid properties.
        """
        self.allDay = allDay
        self.availableEndTime = availableEndTime
        self.availableStartTime = availableStartTime
        self.daysOfWeek = daysOfWeek

    def __repr__(self):
        return '<HealthcareServiceAvailableTime %r>' % 'self.property'  # replace self.property


class HealthcareServiceNotAvailable(backboneelement.BackboneElement):
    """ Not available during this time due to provided reason.

    The HealthcareService is not available during this period of time due to
    the provided reason.
    """

    __tablename__ = "HealthcareServiceNotAvailable"

    description = Column(primitives.StringField)
    """ Reason presented to the user explaining why time not available.
        Type `str`. """

    during = Column(primitives.StringField,
                    ForeignKey('Period.id'))
    """ Service not availablefrom this date.
        Type `Period` (represented as `dict` in JSON). """

    def __init__(self, description, during,):
        """ Initialize all valid properties.
        """
        self.description = description
        self.during = during

    def __repr__(self):
        return '<HealthcareServiceNotAvailable %r>' % 'self.property'  # replace self.property


class HealthcareServiceServiceType(backboneelement.BackboneElement):
    """ Specific service delivered or performed.

    A specific type of service that may be delivered or performed.
    """

    __tablename__ = "HealthcareServiceServiceType"

    specialty = Column(primitives.StringField,
                       ForeignKey('CodeableConcept.id'))
    """ Specialties handled by the Service Site.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Type of service delivered or performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, specialty, type,):
        """ Initialize all valid properties.
        """
        self.specialty = specialty
        self.type = type

    def __repr__(self):
        return '<HealthcareServiceServiceType %r>' % 'self.property'  # replace self.property


class HealthcareService(domainresource.DomainResource):
    """ The details of a healthcare service available at a location.
    """

    __tablename__ = "HealthcareService"
    
    appointmentRequired = Column(primitives.BooleanField)
    """ If an appointment is required for access to this service.
        Type `bool`. """
    
    availabilityExceptions = Column(primitives.StringField)
    """ Description of availability exceptions.
        Type `str`. """
    
    availableTime = Column(primitives.StringField,
                           ForeignKey(
                               'HealthcareServiceAvailableTime.id'))
    """ Times the Service Site is available.
        List of `HealthcareServiceAvailableTime` items (represented as `dict` in JSON). """
    
    characteristic = Column(primitives.StringField,
                            ForeignKey('CodeableConcept.id'))
    """ Collection of characteristics (attributes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    comment = Column(primitives.StringField)
    """ Additional description and/or any specific issues not covered
        elsewhere.
        Type `str`. """
    
    # todo coverageArea = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    coverageArea = Column(primitives.StringField)
    """ Location(s) service is inteded for/available to.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """
    
    eligibility = Column(primitives.StringField,
                         ForeignKey('CodeableConcept.id'))
    """ Specific eligibility requirements required to use the service.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    eligibilityNote = Column(primitives.StringField)
    """ Describes the eligibility conditions for the service.
        Type `str`. """
    
    extraDetails = Column(primitives.StringField)
    """ Extra details about the service that can't be placed in the other
        fields.
        Type `str`. """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ External identifiers for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    # todo location = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    location = Column(primitives.StringField)
    """ Location where service may be provided.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
    
    notAvailable = Column(primitives.StringField,
                          ForeignKey(
                              'HealthcareServiceNotAvailable.id'))
    """ Not available during this time due to provided reason.
        List of `HealthcareServiceNotAvailable` items (represented as `dict` in JSON). """
    
    photo = Column(primitives.StringField,
                   ForeignKey('Attachment.id'))
    """ Facilitates quick identification of the service.
        Type `Attachment` (represented as `dict` in JSON). """
    
    programName = Column(primitives.StringField)
    """ Program Names that categorize the service.
        List of `str` items. """
    
    # todo providedBy = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    providedBy = Column(primitives.StringField)
    """ Organization that provides this service.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
    
    publicKey = Column(primitives.StringField)
    """ PKI Public keys to support secure communications.
        Type `str`. """
    
    referralMethod = Column(primitives.StringField,
                            ForeignKey('CodeableConcept.id'))
    """ Ways that the service accepts referrals.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    serviceCategory = Column(primitives.StringField,
                             ForeignKey('CodeableConcept.id'))
    """ Broad category of service being performed or delivered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    serviceName = Column(primitives.StringField)
    """ Description of service as presented to a consumer while searching.
        Type `str`. """
    
    serviceProvisionCode = Column(primitives.StringField,
                                  ForeignKey('CodeableConcept.id'))
    """ Conditions under which service is available/offered.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    serviceType = Column(primitives.StringField,
                         ForeignKey(
                             'HealthcareServiceServiceType.id'))
    """ Specific service delivered or performed.
        List of `HealthcareServiceServiceType` items (represented as `dict` in JSON). """
    
    telecom = Column(primitives.StringField,
                     ForeignKey('ContactPoint.id'))
    """ Contacts related to the healthcare service.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, appointmentRequired, availabilityExceptions, availableTime,
                 characteristic, comment, coverageArea, eligibility,
                 eligibilityNote, extraDetails, identifier, location,
                 notAvailable, photo, programName, providedBy, publicKey,
                 referralMethod, serviceCategory, serviceName, serviceProvisionCode,
                 serviceType, telecom,):
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
