#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Composition)
#  Date: 2016-03-18.


from . import domainresource

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

    attester = Column(CompositionAttester)
    """ Attests to accuracy of composition.
        List of `CompositionAttester` items (represented as `dict` in JSON). """

    author = Column(FHIRReference)
    """ Who and/or what authored the composition.
        List of `FHIRReference` items referencing `Practitioner, Device, Patient, RelatedPerson` (represented as `dict` in JSON). """

    class_fhir = Column()
    """ Categorization of Composition.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    confidentiality = Column()
    """ As defined by affinity domain.
        Type `str`. """

    custodian = Column()
    """ Organization which maintains the composition.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    date = Column()
    """ Composition editing time.
        Type `FHIRDate` (represented as `str` in JSON). """

    encounter = Column()
    """ Context of the Composition.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    event = Column(CompositionEvent)
    """ The clinical service(s) being documented.
        List of `CompositionEvent` items (represented as `dict` in JSON). """

    identifier = Column()
    """ Logical identifier of composition (version-independent).
        Type `Identifier` (represented as `dict` in JSON). """

    section = Column(CompositionSection)
    """ Composition is broken into sections.
        List of `CompositionSection` items (represented as `dict` in JSON). """

    status = Column()
    """ preliminary | final | amended | entered-in-error.
        Type `str`. """

    subject = Column()
    """ Who and/or what the composition is about.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    title = Column()
    """ Human Readable name/title.
        Type `str`. """

    type = Column()
    """ Kind of composition (LOINC if possible).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, attester, author, class_fhir, confidentiality, custodian, date, encounter, event, identifier, section, status, subject, title, type,):
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


from . import backboneelement

class CompositionAttester(backboneelement.BackboneElement):
    """ Attests to accuracy of composition.

    A participant who has attested to the accuracy of the composition/document.
    """

    __tablename__ = "CompositionAttester"

    mode = Column(str)
    """ personal | professional | legal | official.
        List of `str` items. """

    party = Column()
    """ Who attested the composition.
        Type `FHIRReference` referencing `Patient, Practitioner, Organization` (represented as `dict` in JSON). """

    time = Column()
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

    code = Column(CodeableConcept)
    """ Code(s) that apply to the event being documented.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    detail = Column(FHIRReference)
    """ The event(s) being documented.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """

    period = Column()
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

    code = Column()
    """ Classification of section (recommended).
        Type `CodeableConcept` (represented as `dict` in JSON). """

    emptyReason = Column()
    """ Why the section is empty.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    entry = Column(FHIRReference)
    """ A reference to data that supports this section.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """

    mode = Column()
    """ working | snapshot | changes.
        Type `str`. """

    orderedBy = Column()
    """ Order of section entries.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    section = Column(CompositionSection)
    """ Nested Section.
        List of `CompositionSection` items (represented as `dict` in JSON). """

    text = Column()
    """ Text summary of the section, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """

    title = Column()
    """ Label for section (e.g. for ToC).
        Type `str`. """

    def __init__(self, code, emptyReason, entry, mode, orderedBy, section, text, title,):
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


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import narrative
from . import period