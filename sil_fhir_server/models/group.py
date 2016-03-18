#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Group)
#  Date: 2016-03-18.


from . import domainresource

class Group(domainresource.DomainResource):
    """ Group of multiple entities.

    Represents a defined collection of entities that may be discussed or acted
    upon collectively but which are not expected to act collectively and are
    not formally or legally recognized; i.e. a collection of entities that
    isn't an Organization.
    """

    __tablename__ = "Group"

    actual = Column()
    """ Descriptive or actual.
        Type `bool`. """

    characteristic = Column(GroupCharacteristic)
    """ Trait of group members.
        List of `GroupCharacteristic` items (represented as `dict` in JSON). """

    code = Column()
    """ Kind of Group members.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    identifier = Column(Identifier)
    """ Unique id.
        List of `Identifier` items (represented as `dict` in JSON). """

    member = Column(GroupMember)
    """ Who or what is in group.
        List of `GroupMember` items (represented as `dict` in JSON). """

    name = Column()
    """ Label for Group.
        Type `str`. """

    quantity = Column()
    """ Number of members.
        Type `int`. """

    type = Column()
    """ person | animal | practitioner | device | medication | substance.
        Type `str`. """

    def __init__(self, actual, characteristic, code, identifier, member, name, quantity, type,):
        """ Initialize all valid properties.
        """
        self.actual = actual
        self.characteristic = characteristic
        self.code = code
        self.identifier = identifier
        self.member = member
        self.name = name
        self.quantity = quantity
        self.type = type

    def __repr__(self):
        return '<Group %r>' % 'self.property'  # replace self.property


from . import backboneelement

class GroupCharacteristic(backboneelement.BackboneElement):
    """ Trait of group members.

    Identifies the traits shared by members of the group.
    """

    __tablename__ = "GroupCharacteristic"

    code = Column()
    """ Kind of characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    exclude = Column()
    """ Group includes or excludes.
        Type `bool`. """

    period = Column()
    """ Period over which characteristic is tested.
        Type `Period` (represented as `dict` in JSON). """

    valueBoolean = Column()
    """ Value held by characteristic.
        Type `bool`. """

    valueCodeableConcept = Column()
    """ Value held by characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    valueQuantity = Column()
    """ Value held by characteristic.
        Type `Quantity` (represented as `dict` in JSON). """

    valueRange = Column()
    """ Value held by characteristic.
        Type `Range` (represented as `dict` in JSON). """

    def __init__(self, code, exclude, period, valueBoolean, valueCodeableConcept, valueQuantity, valueRange,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.exclude = exclude
        self.period = period
        self.valueBoolean = valueBoolean
        self.valueCodeableConcept = valueCodeableConcept
        self.valueQuantity = valueQuantity
        self.valueRange = valueRange

    def __repr__(self):
        return '<GroupCharacteristic %r>' % 'self.property'  # replace self.property


class GroupMember(backboneelement.BackboneElement):
    """ Who or what is in group.

    Identifies the resource instances that are members of the group.
    """

    __tablename__ = "GroupMember"

    entity = Column()
    """ Reference to the group member.
        Type `FHIRReference` referencing `Patient, Practitioner, Device, Medication, Substance` (represented as `dict` in JSON). """

    inactive = Column()
    """ If member is no longer in group.
        Type `bool`. """

    period = Column()
    """ Period member belonged to the group.
        Type `Period` (represented as `dict` in JSON). """

    def __init__(self, entity, inactive, period,):
        """ Initialize all valid properties.
        """
        self.entity = entity
        self.inactive = inactive
        self.period = period

    def __repr__(self):
        return '<GroupMember %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range