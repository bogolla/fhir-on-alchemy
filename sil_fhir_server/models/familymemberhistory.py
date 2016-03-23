#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource

class FamilyMemberHistory(domainresource.DomainResource):
    """ Information about patient's relatives, relevant for patient.

    Significant health events and conditions for a person related to the
    patient relevant in the context of care for the patient.
    """

    __tablename__ = "FamilyMemberHistory"
    
    ageQuantity = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ (approximate) age.
        Type `Quantity` referencing `Age` (represented as `dict` in JSON). """
    
    ageRange = Column(primitives.StringField, ForeignKey('Range.id'))
    """ (approximate) age.
        Type `Range` (represented as `dict` in JSON). """
    
    ageString = Column(primitives.StringField)
    """ (approximate) age.
        Type `str`. """
    
    bornDate = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ (approximate) date of birth.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    bornPeriod = Column(primitives.StringField, ForeignKey('Period.id'))
    """ (approximate) date of birth.
        Type `Period` (represented as `dict` in JSON). """
    
    bornString = Column(primitives.StringField)
    """ (approximate) date of birth.
        Type `str`. """
    
    condition = Column(primitives.StringField, ForeignKey('FamilyMemberHistoryCondition.id'))
    """ Condition that the related person had.
        List of `FamilyMemberHistoryCondition` items (represented as `dict` in JSON). """
    
    date = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ When history was captured/updated.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    deceasedBoolean = Column(primitives.BooleanField)
    """ Dead? How old/when?.
        Type `bool`. """
    
    deceasedDate = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ Dead? How old/when?.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    deceasedQuantity = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ Dead? How old/when?.
        Type `Quantity` referencing `Age` (represented as `dict` in JSON). """
    
    deceasedRange = Column(primitives.StringField, ForeignKey('Range.id'))
    """ Dead? How old/when?.
        Type `Range` (represented as `dict` in JSON). """
    
    deceasedString = Column(primitives.StringField)
    """ Dead? How old/when?.
        Type `str`. """
    
    gender = Column(primitives.StringField)
    """ male | female | other | unknown.
        Type `str`. """
    
    identifier = Column(primitives.StringField, ForeignKey('Identifier.id'))
    """ External Id(s) for this record.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    name = Column(primitives.StringField)
    """ The family member described.
        Type `str`. """
    
    note = Column(primitives.StringField, ForeignKey('Annotation.id'))
    """ General note about related person.
        Type `Annotation` (represented as `dict` in JSON). """
    
    patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Patient history is about.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    relationship = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ Relationship to the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ partial | completed | entered-in-error | health-unknown.
        Type `str`. """

    def __init__(self, ageQuantity, ageRange, ageString, bornDate, bornPeriod, bornString, condition, date, deceasedBoolean, deceasedDate, deceasedQuantity, deceasedRange, deceasedString, gender, identifier, name, note, patient, relationship, status,):
        """ Initialize all valid properties.
        """
        self.ageQuantity = ageQuantity
        self.ageRange = ageRange
        self.ageString = ageString
        self.bornDate = bornDate
        self.bornPeriod = bornPeriod
        self.bornString = bornString
        self.condition = condition
        self.date = date
        self.deceasedBoolean = deceasedBoolean
        self.deceasedDate = deceasedDate
        self.deceasedQuantity = deceasedQuantity
        self.deceasedRange = deceasedRange
        self.deceasedString = deceasedString
        self.gender = gender
        self.identifier = identifier
        self.name = name
        self.note = note
        self.patient = patient
        self.relationship = relationship
        self.status = status

    def __repr__(self):
        return '<FamilyMemberHistory %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import backboneelement

class FamilyMemberHistoryCondition(backboneelement.BackboneElement):
    """ Condition that the related person had.

    The significant Conditions (or condition) that the family member had. This
    is a repeating section to allow a system to represent more than one
    condition per resource, though there is nothing stopping multiple resources
    - one per condition.
    """

    __tablename__ = "FamilyMemberHistoryCondition"
    
    code = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ Condition suffered by relation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    note = Column(primitives.StringField, ForeignKey('Annotation.id'))
    """ Extra information about condition.
        Type `Annotation` (represented as `dict` in JSON). """
    
    onsetPeriod = Column(primitives.StringField, ForeignKey('Period.id'))
    """ When condition first manifested.
        Type `Period` (represented as `dict` in JSON). """
    
    onsetQuantity = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ When condition first manifested.
        Type `Quantity` referencing `Age` (represented as `dict` in JSON). """
    
    onsetRange = Column(primitives.StringField, ForeignKey('Range.id'))
    """ When condition first manifested.
        Type `Range` (represented as `dict` in JSON). """
    
    onsetString = Column(primitives.StringField)
    """ When condition first manifested.
        Type `str`. """
    
    outcome = Column(primitives.StringField, ForeignKey('CodeableConcept.id'))
    """ deceased | permanent disability | etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, code, note, onsetPeriod, onsetQuantity, onsetRange, onsetString, outcome,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.note = note
        self.onsetPeriod = onsetPeriod
        self.onsetQuantity = onsetQuantity
        self.onsetRange = onsetRange
        self.onsetString = onsetString
        self.outcome = outcome

    def __repr__(self):
        return '<FamilyMemberHistoryCondition %r>' % 'self.property'  # replace self.property