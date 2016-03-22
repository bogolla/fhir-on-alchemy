#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Device)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class Device(domainresource.DomainResource):
    """ An instance of a manufactured te that is used in the provision of
    healthcare.

    This resource identifies an instance of a manufactured item that is used in
    the provision of healthcare without being substantially changed through
    that activity. The device may be a medical or non-medical device.  Medical
    devices includes durable (reusable) medical equipment, implantable devices,
    as well as disposable equipment used for diagnostic, treatment, and
    research for healthcare and public health.  Non-medical devices may include
    items such as a machine, cellphone, computer, application, etc.
    """

    __tablename__ = "Device"

    contact = Column(ContactPoint)
    """ Details for human/organization for support.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    expiry = Column(FHIRDate)
    """ Date and time of expiry of this device (if applicable).
        Type `FHIRDate` (represented as `str` in JSON). """

    identifier = Column(Identifier)
    """ Instance id from manufacturer, owner, and others.
        List of `Identifier` items (represented as `dict` in JSON). """

    location = Column(FHIRReference)
    """ Where the resource is found.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """

    lotNumber = Column(primitives.StringField)
    """ Lot number of manufacture.
        Type `str`. """

    manufactureDate = Column(FHIRDate)
    """ Manufacture date.
        Type `FHIRDate` (represented as `str` in JSON). """

    manufacturer = Column(primitives.StringField)
    """ Name of device manufacturer.
        Type `str`. """

    model = Column(primitives.StringField)
    """ Model id assigned by the manufacturer.
        Type `str`. """

    note = Column(Annotation)
    """ Device notes and comments.
        List of `Annotation` items (represented as `dict` in JSON). """

    owner = Column(FHIRReference)
    """ Organization responsible for device.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    patient = Column(FHIRReference)
    """ If the resource is affixed to a person.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    status = Column(primitives.StringField)
    """ available | not-available | entered-in-error.
        Type `str`. """

    type = Column(CodeableConcept)
    """ What kind of device this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    udi = Column(primitives.StringField)
    """ FDA mandated Unique Device Identifier.
        Type `str`. """

    url = Column(primitives.StringField)
    """ Network address to contact device.
        Type `str`. """

    version = Column(primitives.StringField)
    """ Version number (i.e. software).
        Type `str`. """

    def __init__(self, contact, expiry, identifier, location, lotNumber, manufactureDate, manufacturer, model, note, owner, patient, status, type, udi, url, version,):
        """ Initialize all valid properties.
        """
        self.contact = contact
        self.expiry = expiry
        self.identifier = identifier
        self.location = location
        self.lotNumber = lotNumber
        self.manufactureDate = manufactureDate
        self.manufacturer = manufacturer
        self.model = model
        self.note = note
        self.owner = owner
        self.patient = patient
        self.status = status
        self.type = type
        self.udi = udi
        self.url = url
        self.version = version

    def __repr__(self):
        return '<Device %r>' % 'self.property'  # replace self.property


from . import annotation
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier