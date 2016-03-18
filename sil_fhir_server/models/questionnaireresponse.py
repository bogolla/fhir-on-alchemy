#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse)
#  Date: 2016-03-18.


from . import domainresource

class QuestionnaireResponse(domainresource.DomainResource):
    """ A structured set of questions and their answers.

    A structured set of questions and their answers. The questions are ordered
    and grouped into coherent subsets, corresponding to the structure of the
    grouping of the underlying questions.
    """

    __tablename__ = "QuestionnaireResponse"

    author = Column()
    """ Person who received and recorded the answers.
        Type `FHIRReference` referencing `Device, Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """

    authored = Column()
    """ Date this version was authored.
        Type `FHIRDate` (represented as `str` in JSON). """

    encounter = Column()
    """ Primary encounter during which the answers were collected.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    group = Column()
    """ Grouped questions.
        Type `QuestionnaireResponseGroup` (represented as `dict` in JSON). """

    identifier = Column()
    """ Unique id for this set of answers.
        Type `Identifier` (represented as `dict` in JSON). """

    questionnaire = Column()
    """ Form being answered.
        Type `FHIRReference` referencing `Questionnaire` (represented as `dict` in JSON). """

    source = Column()
    """ The person who answered the questions.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """

    status = Column()
    """ in-progress | completed | amended.
        Type `str`. """

    subject = Column()
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


from . import backboneelement

class QuestionnaireResponseGroup(backboneelement.BackboneElement):
    """ Grouped questions.

    A group of questions to a possibly similarly grouped set of questions in
    the questionnaire response.
    """

    __tablename__ = "QuestionnaireResponseGroup"

    group = Column(QuestionnaireResponseGroup)
    """ Nested questionnaire response group.
        List of `QuestionnaireResponseGroup` items (represented as `dict` in JSON). """

    linkId = Column()
    """ Corresponding group within Questionnaire.
        Type `str`. """

    question = Column(QuestionnaireResponseGroupQuestion)
    """ Questions in this group.
        List of `QuestionnaireResponseGroupQuestion` items (represented as `dict` in JSON). """

    subject = Column()
    """ The subject this group's answers are about.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    text = Column()
    """ Additional text for the group.
        Type `str`. """

    title = Column()
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


class QuestionnaireResponseGroupQuestion(backboneelement.BackboneElement):
    """ Questions in this group.

    Set of questions within this group. The order of questions within the group
    is relevant.
    """

    __tablename__ = "QuestionnaireResponseGroupQuestion"

    answer = Column(QuestionnaireResponseGroupQuestionAnswer)
    """ The response(s) to the question.
        List of `QuestionnaireResponseGroupQuestionAnswer` items (represented as `dict` in JSON). """

    linkId = Column()
    """ Corresponding question within Questionnaire.
        Type `str`. """

    text = Column()
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


class QuestionnaireResponseGroupQuestionAnswer(backboneelement.BackboneElement):
    """ The response(s) to the question.

    The respondent's answer(s) to the question.
    """

    __tablename__ = "QuestionnaireResponseGroupQuestionAnswer"

    group = Column(QuestionnaireResponseGroup)
    """ Nested questionnaire group.
        List of `QuestionnaireResponseGroup` items (represented as `dict` in JSON). """

    valueAttachment = Column()
    """ Single-valued answer to the question.
        Type `Attachment` (represented as `dict` in JSON). """

    valueBoolean = Column()
    """ Single-valued answer to the question.
        Type `bool`. """

    valueCoding = Column()
    """ Single-valued answer to the question.
        Type `Coding` (represented as `dict` in JSON). """

    valueDate = Column()
    """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """

    valueDateTime = Column()
    """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """

    valueDecimal = Column()
    """ Single-valued answer to the question.
        Type `float`. """

    valueInstant = Column()
    """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """

    valueInteger = Column()
    """ Single-valued answer to the question.
        Type `int`. """

    valueQuantity = Column()
    """ Single-valued answer to the question.
        Type `Quantity` (represented as `dict` in JSON). """

    valueReference = Column()
    """ Single-valued answer to the question.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    valueString = Column()
    """ Single-valued answer to the question.
        Type `str`. """

    valueTime = Column()
    """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """

    valueUri = Column()
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


from . import attachment
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity