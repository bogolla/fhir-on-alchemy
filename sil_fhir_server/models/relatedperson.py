#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/RelatedPerson)
#  Date: 2016-03-18.


from . import domainresource

class RelatedPerson(domainresource.DomainResource):
    """ An person that is related to a patient, but who is not a direct target of
    care.

    Information about a person that is involved in the care for a patient, but
    who is not the target of healthcare, nor has a formal responsibility in the
    care process.
    """

    __tablename__ = "RelatedPerson"

    address = Column(Address)
    """ Address where the related person can be contacted or visited.
        List of `Address` items (represented as `dict` in JSON). """

    birthDate = Column()
    """ The date on which the related person was born.
        Type `FHIRDate` (represented as `str` in JSON). """

    gender = Column()
    """ male | female | other | unknown.
        Type `str`. """

    identifier = Column(Identifier)
    """ A human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """

    name = Column()
    """ A name associated with the person.
        Type `HumanName` (represented as `dict` in JSON). """

    patient = Column()
    """ The patient this person is related to.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

    period = Column()
    """ Period of time that this relationship is considered valid.
        Type `Period` (represented as `dict` in JSON). """

    photo = Column(Attachment)
    """ Image of the person.
        List of `Attachment` items (represented as `dict` in JSON). """

    relationship = Column()
    """ The nature of the relationship.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    telecom = Column(ContactPoint)
    """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, address, birthDate, gender, identifier, name, patient, period, photo, relationship, telecom,):
        """ Initialize all valid properties.
        """
        self.address = address
        self.birthDate = birthDate
        self.gender = gender
        self.identifier = identifier
        self.name = name
        self.patient = patient
        self.period = period
        self.photo = photo
        self.relationship = relationship
        self.telecom = telecom

    def __repr__(self):
        return '<RelatedPerson %r>' % 'self.property'  # replace self.property


from . import address
from . import attachment
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import period