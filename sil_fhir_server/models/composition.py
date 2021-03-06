#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Composition)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class CompositionAttester(backboneelement.BackboneElement):
    """ Attests to accuracy of composition.

    A participant who has attested to the accuracy of the composition/document.
    """

    __tablename__ = "CompositionAttester"

    mode = Column(primitives.StringField)
    """ personal | professional | legal | official.
        List of `str` items. """

    # todo party = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    party = Column(primitives.StringField)
    """ Who attested the composition.
        Type `FHIRReference` referencing `Patient, Practitioner,
        Organization` (represented as `dict` in JSON). """

    time = Column(primitives.DateTimeField)
    """ When composition attested.
        Type `FHIRDate` (represented as `str` in JSON). """

    def __init__(self, mode, party, time,):
        """ Initialize all valid properties.
        """
        self.mode = mode
        self.party = party
        self.time = time

    def __repr__(self):
        return '<CompositionAttester %r>' % 'self.property'  # replace self.property


class CompositionEvent(backboneelement.BackboneElement):
    """ The clinical service(s) being documented.

    The clinical service, such as a colonoscopy or an appendectomy, being
    documented.
    """

    __tablename__ = "CompositionEvent"

    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Code(s) that apply to the event being documented.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    # todo detail = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    detail = Column(primitives.StringField)
    """ The event(s) being documented.
        List of `FHIRReference` items referencing `Resource`
        (represented as `dict` in JSON). """

    period = Column(primitives.StringField,
                    ForeignKey('Period.id'))
    """ The period covered by the documentation.
        Type `Period` (represented as `dict` in JSON). """

    def __init__(self, code, detail, period,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.detail = detail
        self.period = period

    def __repr__(self):
        return '<CompositionEvent %r>' % 'self.property'  # replace self.property


class CompositionSection(backboneelement.BackboneElement):
    """ Composition is broken into sections.

    The root of the sections that make up the composition.
    """

    __tablename__ = "CompositionSection"

    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Classification of section (recommended).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    emptyReason = Column(primitives.StringField,
                         ForeignKey('CodeableConcept.id'))
    """ Why the section is empty.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    # todo entry = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    entry = Column(primitives.StringField)
    """ A reference to data that supports this section.
        List of `FHIRReference` items referencing `Resource`
        (represented as `dict` in JSON). """

    mode = Column(primitives.StringField)
    """ working | snapshot | changes.
        Type `str`. """

    orderedBy = Column(primitives.StringField,
                       ForeignKey('CodeableConcept.id'))
    """ Order of section entries.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    section = Column(primitives.StringField,
                     ForeignKey('CompositionSection.id'))
    """ Nested Section.
        List of `CompositionSection` items (represented as `dict` in JSON). """

    text = Column(primitives.StringField,
                  ForeignKey('Narrative.id'))
    """ Text summary of the section, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """

    title = Column(primitives.StringField)
    """ Label for section (e.g. for ToC).
        Type `str`. """

    def __init__(self, code, emptyReason, entry, mode,
                 orderedBy, section, text, title,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.emptyReason = emptyReason
        self.entry = entry
        self.mode = mode
        self.orderedBy = orderedBy
        self.section = section
        self.text = text
        self.title = title

    def __repr__(self):
        return '<CompositionSection %r>' % 'self.property'  # replace self.property


class Composition(domainresource.DomainResource):
    """ A set of resources composed into a single coherent clinical statement with
    clinical attestation.

    A set of healthcare-related information that is assembled together into a
    single logical document that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation with
    regard to who is making the statement. While a Composition defines the
    structure, it does not actually contain the content: rather the full
    content of a document is contained in a Bundle, of which the Composition is
    the first resource contained.
    """

    __tablename__ = "Composition"
    
    attester = Column(primitives.StringField,
                      ForeignKey('CompositionAttester.id'))
    """ Attests to accuracy of composition.
        List of `CompositionAttester` items (represented as `dict` in JSON). """
    
    # todo author = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    author = Column(primitives.StringField)
    """ Who and/or what authored the composition.
        List of `FHIRReference` items referencing `Practitioner,
        Device, Patient, RelatedPerson` (represented as `dict` in JSON). """
    
    class_fhir = Column(primitives.StringField,
                        ForeignKey('CodeableConcept.id'))
    """ Categorization of Composition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    confidentiality = Column(primitives.StringField)
    """ As defined by affinity domain.
        Type `str`. """
    
    # todo custodian = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    custodian = Column(primitives.StringField)
    """ Organization which maintains the composition.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
    
    date = Column(primitives.DateTimeField)
    """ Composition editing time.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    # todo encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ Context of the Composition.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
    
    event = Column(primitives.StringField,
                   ForeignKey('CompositionEvent.id'))
    """ The clinical service(s) being documented.
        List of `CompositionEvent` items (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Logical identifier of composition (version-independent).
        Type `Identifier` (represented as `dict` in JSON). """
    
    section = Column(primitives.StringField,
                     ForeignKey('CompositionSection.id'))
    """ Composition is broken into sections.
        List of `CompositionSection` items (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ preliminary | final | amended | entered-in-error.
        Type `str`. """
    
    # todo subject = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    subject = Column(primitives.StringField)
    """ Who and/or what the composition is about.
        Type `FHIRReference` referencing `Resource`
        (represented as `dict` in JSON). """
    
    title = Column(primitives.StringField)
    """ Human Readable name/title.
        Type `str`. """
    
    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Kind of composition (LOINC if possible).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, attester, author, class_fhir, confidentiality,
                 custodian, date, encounter, event, identifier,
                 section, status, subject, title, type,):
        """ Initialize all valid properties.
        """
        self.attester = attester
        self.author = author
        self.class_fhir = class_fhir
        self.confidentiality = confidentiality
        self.custodian = custodian
        self.date = date
        self.encounter = encounter
        self.event = event
        self.identifier = identifier
        self.section = section
        self.status = status
        self.subject = subject
        self.title = title
        self.type = type

    def __repr__(self):
        return '<Composition %r>' % 'self.property'  # replace self.property
