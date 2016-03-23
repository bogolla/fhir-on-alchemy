#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Questionnaire)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class QuestionnaireGroup(backboneelement.BackboneElement):
    """ Grouped questions.

    A collection of related questions (or further groupings of questions).
    """

    __tablename__ = "QuestionnaireGroup"

    concept = Column(primitives.StringField,
                     ForeignKey('Coding.id'))
    """ Concept that represents this section in a questionnaire.
        List of `Coding` items (represented as `dict` in JSON). """

    group = Column(primitives.StringField,
                   ForeignKey('QuestionnaireGroup.id'))
    """ Nested questionnaire group.
        List of `QuestionnaireGroup` items (represented as `dict` in JSON). """

    linkId = Column(primitives.StringField)
    """ To link questionnaire with questionnaire response.
        Type `str`. """

    question = Column(primitives.StringField,
                      ForeignKey('QuestionnaireGroupQuestion.id'))
    """ Questions in this group.
        List of `QuestionnaireGroupQuestion` items (represented as `dict` in JSON). """

    repeats = Column(primitives.BooleanField)
    """ Whether the group may repeat.
        Type `bool`. """

    required = Column(primitives.BooleanField)
    """ Whether the group must be included in data results.
        Type `bool`. """

    text = Column(primitives.StringField)
    """ Additional text for the group.
        Type `str`. """

    title = Column(primitives.StringField)
    """ Name to be displayed for group.
        Type `str`. """

    def __init__(self, concept, group, linkId, question,
                 repeats, required, text, title,):
        """ Initialize all valid properties.
        """
        self.concept = concept
        self.group = group
        self.linkId = linkId
        self.question = question
        self.repeats = repeats
        self.required = required
        self.text = text
        self.title = title

    def __repr__(self):
        return '<QuestionnaireGroup %r>' % 'self.property'  # replace self.property


class QuestionnaireGroupQuestion(backboneelement.BackboneElement):
    """ Questions in this group.

    Set of questions within this group. The order of questions within the group
    is relevant.
    """

    __tablename__ = "QuestionnaireGroupQuestion"

    concept = Column(primitives.StringField,
                     ForeignKey('Coding.id'))
    """ Concept that represents this question on a questionnaire.
        List of `Coding` items (represented as `dict` in JSON). """

    group = Column(primitives.StringField,
                   ForeignKey('QuestionnaireGroup.id'))
    """ Nested questionnaire group.
        List of `QuestionnaireGroup` items (represented as `dict` in JSON). """

    linkId = Column(primitives.StringField)
    """ To link questionnaire with questionnaire response.
        Type `str`. """

    option = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Permitted answer.
        List of `Coding` items (represented as `dict` in JSON). """

    # todo options = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    options = Column(primitives.StringField)
    """ Valueset containing permitted answers.
        Type `FHIRReference` referencing `ValueSet`
        (represented as `dict` in JSON). """

    repeats = Column(primitives.BooleanField)
    """ Whether the question  can have multiple answers.
        Type `bool`. """

    required = Column(primitives.BooleanField)
    """ Whether the question must be answered in data results.
        Type `bool`. """

    text = Column(primitives.StringField)
    """ Text of the question as it is shown to the user.
        Type `str`. """

    type = Column(primitives.StringField)
    """ boolean | decimal | integer | date | dateTime +.
        Type `str`. """

    def __init__(self, concept, group, linkId, option, options,
                 repeats, required, text, type,):
        """ Initialize all valid properties.
        """
        self.concept = concept
        self.group = group
        self.linkId = linkId
        self.option = option
        self.options = options
        self.repeats = repeats
        self.required = required
        self.text = text
        self.type = type

    def __repr__(self):
        return '<QuestionnaireGroupQuestion %r>' % 'self.property'  # replace self.property


class Questionnaire(domainresource.DomainResource):
    """ A structured set of questions.

    A structured set of questions intended to guide the collection of answers.
    The questions are ordered and grouped into coherent subsets, corresponding
    to the structure of the grouping of the underlying questions.
    """

    __tablename__ = "Questionnaire"
    
    date = Column(primitives.StringField, ForeignKey('FHIRDate.id'))
    """ Date this version was authored.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    group = Column(primitives.StringField, ForeignKey('QuestionnaireGroup.id'))
    """ Grouped questions.
        Type `QuestionnaireGroup` (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField, ForeignKey('Identifier.id'))
    """ External identifiers for this questionnaire.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    publisher = Column(primitives.StringField)
    """ Organization/individual who designed the questionnaire.
        Type `str`. """
    
    status = Column(primitives.StringField)
    """ draft | published | retired.
        Type `str`. """
    
    subjectType = Column(primitives.StringField)
    """ Resource that can be subject of QuestionnaireResponse.
        List of `str` items. """
    
    telecom = Column(primitives.StringField, ForeignKey('ContactPoint.id'))
    """ Contact information of the publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
    
    version = Column(primitives.StringField)
    """ Logical identifier for this version of Questionnaire.
        Type `str`. """

    def __init__(self, date, group, identifier, publisher, status,
                 subjectType, telecom, version,):
        """ Initialize all valid properties.
        """
        self.date = date
        self.group = group
        self.identifier = identifier
        self.publisher = publisher
        self.status = status
        self.subjectType = subjectType
        self.telecom = telecom
        self.version = version

    def __repr__(self):
        return '<Questionnaire %r>' % 'self.property'  # replace self.property
