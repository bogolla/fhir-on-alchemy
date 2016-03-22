#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Schedule)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class Schedule(domainresource.DomainResource):
    """ A container for slot(s) of time that may be available for booking
    appointments.
    """

    __tablename__ = "Schedule"

    actor = Column(FHIRReference)
    """ The resource this Schedule resource is providing availability
        information for. These are expected to usually be one of
        HealthcareService, Location, Practitioner, Device, Patient or
        RelatedPerson.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson, Device, HealthcareService, Location` (represented as `dict` in JSON). """

    comment = Column(primitives.StringField)
    """ Comments on the availability to describe any extended information.
        Such as custom constraints on the slot(s) that may be associated.
        Type `str`. """

    identifier = Column(Identifier)
    """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """

    planningHorizon = Column(Period)
    """ The period of time that the slots that are attached to this
        Schedule resource cover (even if none exist). These  cover the
        amount of time that an organization's planning horizon; the
        interval for which they are currently accepting appointments. This
        does not define a "template" for planning outside these dates.
        Type `Period` (represented as `dict` in JSON). """

    type = Column(CodeableConcept)
    """ The schedule type can be used for the categorization of healthcare
        services or other appointment types.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, actor, comment, identifier, planningHorizon, type,):
        """ Initialize all valid properties.
        """
        self.actor = actor
        self.comment = comment
        self.identifier = identifier
        self.planningHorizon = planningHorizon
        self.type = type

    def __repr__(self):
        return '<Schedule %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import period