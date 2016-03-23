#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/RelatedPerson)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource

class RelatedPerson(domainresource.DomainResource):
    """ An person that is related to a patient, but who is not a direct target of
    care.

    Information about a person that is involved in the care for a patient, but
    who is not the target of healthcare, nor has a formal responsibility in the
    care process.
    """

    __tablename__ = "RelatedPerson"
    
    address = Column(primitives.StringField,
                     ForeignKey('Address.id'))
    """ Address where the related person can be contacted or visited.
        List of `Address` items (represented as `dict` in JSON). """
    
    birthDate = Column(primitives.DateField)
    """ The date on which the related person was born.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    gender = Column(primitives.StringField)
    """ male | female | other | unknown.
        Type `str`. """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ A human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    name = Column(primitives.StringField,
                  ForeignKey('HumanName.id'))
    """ A name associated with the person.
        Type `HumanName` (represented as `dict` in JSON). """
    
    # todo patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    patient = Column(primitives.StringField)
    """ The patient this person is related to.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    period = Column(primitives.StringField,
                    ForeignKey('Period.id'))
    """ Period of time that this relationship is considered valid.
        Type `Period` (represented as `dict` in JSON). """
    
    photo = Column(primitives.StringField,
                   ForeignKey('Attachment.id'))
    """ Image of the person.
        List of `Attachment` items (represented as `dict` in JSON). """
    
    relationship = Column(primitives.StringField,
                          ForeignKey('CodeableConcept.id'))
    """ The nature of the relationship.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    telecom = Column(primitives.StringField,
                     ForeignKey('ContactPoint.id'))
    """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, address, birthDate, gender, identifier,
                 name, patient, period, photo, relationship, telecom,):
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