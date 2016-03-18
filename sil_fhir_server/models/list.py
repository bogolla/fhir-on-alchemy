#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/List)
#  Date: 2016-03-18.


from . import domainresource

class List(domainresource.DomainResource):
    """ Information summarized from a list of other resources.

    A set of information summarized from a list of other resources.
    """

    __tablename__ = "List"

    code = Column()
    """ What the purpose of this list is.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    date = Column()
    """ When the list was prepared.
        Type `FHIRDate` (represented as `str` in JSON). """

    emptyReason = Column()
    """ Why list is empty.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    encounter = Column()
    """ Context in which list created.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

    entry = Column(ListEntry)
    """ Entries in the list.
        List of `ListEntry` items (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    mode = Column()
    """ working | snapshot | changes.
        Type `str`. """

    note = Column()
    """ Comments about the list.
        Type `str`. """

    orderedBy = Column()
    """ What order the list has.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    source = Column()
    """ Who and/or what defined the list contents (aka Author).
        Type `FHIRReference` referencing `Practitioner, Patient, Device` (represented as `dict` in JSON). """

    status = Column()
    """ current | retired | entered-in-error.
        Type `str`. """

    subject = Column()
    """ If all resources have the same subject.
        Type `FHIRReference` referencing `Patient, Group, Device, Location` (represented as `dict` in JSON). """

    title = Column()
    """ Descriptive name for the list.
        Type `str`. """

    def __init__(self, code, date, emptyReason, encounter, entry, identifier, mode, note, orderedBy, source, status, subject, title,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.date = date
        self.emptyReason = emptyReason
        self.encounter = encounter
        self.entry = entry
        self.identifier = identifier
        self.mode = mode
        self.note = note
        self.orderedBy = orderedBy
        self.source = source
        self.status = status
        self.subject = subject
        self.title = title

    def __repr__(self):
        return '<List %r>' % 'self.property'  # replace self.property


from . import backboneelement

class ListEntry(backboneelement.BackboneElement):
    """ Entries in the list.

    Entries in this list.
    """

    __tablename__ = "ListEntry"

    date = Column()
    """ When item added to list.
        Type `FHIRDate` (represented as `str` in JSON). """

    deleted = Column()
    """ If this item is actually marked as deleted.
        Type `bool`. """

    flag = Column()
    """ Status/Workflow information about this item.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    item = Column()
    """ Actual entry.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

    def __init__(self, date, deleted, flag, item,):
        """ Initialize all valid properties.
        """
        self.date = date
        self.deleted = deleted
        self.flag = flag
        self.item = item

    def __repr__(self):
        return '<ListEntry %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier