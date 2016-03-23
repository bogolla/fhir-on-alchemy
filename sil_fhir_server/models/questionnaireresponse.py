#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource

class QuestionnaireResponse(domainresource.DomainResource):
    """ A structured set of questions and their answers.

    A structured set of questions and their answers. The questions are ordered
    and grouped into coherent subsets, corresponding to the structure of the
    grouping of the underlying questions.
    """

    __tablename__ = "QuestionnaireResponse"
    
    author = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Person who received and recorded the answers.
        Type `FHIRReference` referencing `Device, Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """
    
    authored = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ Date this version was authored.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Primary encounter during which the answers were collected.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
    
    group = Column(primitives.StringField, ForeignKey('QuestionnaireResponseGroup.id'))
    """ Grouped questions.
        Type `QuestionnaireResponseGroup` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField, ForeignKey('Identifier.id'))
    """ Unique id for this set of answers.
        Type `Identifier` (represented as `dict` in JSON). """
    
    questionnaire = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Form being answered.
        Type `FHIRReference` referencing `Questionnaire` (represented as `dict` in JSON). """
    
    source = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ The person who answered the questions.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ in-progress | completed | amended.
        Type `str`. """
    
    subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ The subject of the questions.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    def __init__(self, author, authored, encounter, group, identifier, questionnaire, source, status, subject,):
        """ Initialize all valid properties.
        """
        self.author = author
        self.authored = authored
        self.encounter = encounter
        self.group = group
        self.identifier = identifier
        self.questionnaire = questionnaire
        self.source = source
        self.status = status
        self.subject = subject

    def __repr__(self):
        return '<QuestionnaireResponse %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import backboneelement

class QuestionnaireResponseGroup(backboneelement.BackboneElement):
    """ Grouped questions.

    A group of questions to a possibly similarly grouped set of questions in
    the questionnaire response.
    """

    __tablename__ = "QuestionnaireResponseGroup"
    
    group = Column(primitives.StringField, ForeignKey('QuestionnaireResponseGroup.id'))
    """ Nested questionnaire response group.
        List of `QuestionnaireResponseGroup` items (represented as `dict` in JSON). """
    
    linkId = Column(primitives.StringField)
    """ Corresponding group within Questionnaire.
        Type `str`. """
    
    question = Column(primitives.StringField, ForeignKey('QuestionnaireResponseGroupQuestion.id'))
    """ Questions in this group.
        List of `QuestionnaireResponseGroupQuestion` items (represented as `dict` in JSON). """
    
    subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ The subject this group's answers are about.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
    
    text = Column(primitives.StringField)
    """ Additional text for the group.
        Type `str`. """
    
    title = Column(primitives.StringField)
    """ Name for this group.
        Type `str`. """

    def __init__(self, group, linkId, question, subject, text, title,):
        """ Initialize all valid properties.
        """
        self.group = group
        self.linkId = linkId
        self.question = question
        self.subject = subject
        self.text = text
        self.title = title

    def __repr__(self):
        return '<QuestionnaireResponseGroup %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
class QuestionnaireResponseGroupQuestion(backboneelement.BackboneElement):
    """ Questions in this group.

    Set of questions within this group. The order of questions within the group
    is relevant.
    """

    __tablename__ = "QuestionnaireResponseGroupQuestion"
    
    answer = Column(primitives.StringField, ForeignKey('QuestionnaireResponseGroupQuestionAnswer.id'))
    """ The response(s) to the question.
        List of `QuestionnaireResponseGroupQuestionAnswer` items (represented as `dict` in JSON). """
    
    linkId = Column(primitives.StringField)
    """ Corresponding question within Questionnaire.
        Type `str`. """
    
    text = Column(primitives.StringField)
    """ Text of the question as it is shown to the user.
        Type `str`. """

    def __init__(self, answer, linkId, text,):
        """ Initialize all valid properties.
        """
        self.answer = answer
        self.linkId = linkId
        self.text = text

    def __repr__(self):
        return '<QuestionnaireResponseGroupQuestion %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
class QuestionnaireResponseGroupQuestionAnswer(backboneelement.BackboneElement):
    """ The response(s) to the question.

    The respondent's answer(s) to the question.
    """

    __tablename__ = "QuestionnaireResponseGroupQuestionAnswer"
    
    group = Column(primitives.StringField, ForeignKey('QuestionnaireResponseGroup.id'))
    """ Nested questionnaire group.
        List of `QuestionnaireResponseGroup` items (represented as `dict` in JSON). """
    
    valueAttachment = Column(primitives.StringField, ForeignKey('Attachment.id'))
    """ Single-valued answer to the question.
        Type `Attachment` (represented as `dict` in JSON). """
    
    valueBoolean = Column(primitives.BooleanField)
    """ Single-valued answer to the question.
        Type `bool`. """
    
    valueCoding = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Single-valued answer to the question.
        Type `Coding` (represented as `dict` in JSON). """
    
    valueDate = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    valueDateTime = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    valueDecimal = Column(primitives.DecimalField)
    """ Single-valued answer to the question.
        Type `float`. """
    
    valueInstant = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    valueInteger = Column(primitives.IntegerField)
    """ Single-valued answer to the question.
        Type `int`. """
    
    valueQuantity = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ Single-valued answer to the question.
        Type `Quantity` (represented as `dict` in JSON). """
    
    valueReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    """ Single-valued answer to the question.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
    
    valueString = Column(primitives.StringField)
    """ Single-valued answer to the question.
        Type `str`. """
    
    valueTime = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    valueUri = Column(primitives.StringField)
    """ Single-valued answer to the question.
        Type `str`. """

    def __init__(self, group, valueAttachment, valueBoolean, valueCoding, valueDate, valueDateTime, valueDecimal, valueInstant, valueInteger, valueQuantity, valueReference, valueString, valueTime, valueUri,):
        """ Initialize all valid properties.
        """
        self.group = group
        self.valueAttachment = valueAttachment
        self.valueBoolean = valueBoolean
        self.valueCoding = valueCoding
        self.valueDate = valueDate
        self.valueDateTime = valueDateTime
        self.valueDecimal = valueDecimal
        self.valueInstant = valueInstant
        self.valueInteger = valueInteger
        self.valueQuantity = valueQuantity
        self.valueReference = valueReference
        self.valueString = valueString
        self.valueTime = valueTime
        self.valueUri = valueUri

    def __repr__(self):
        return '<QuestionnaireResponseGroupQuestionAnswer %r>' % 'self.property'  # replace self.property