#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/OperationDefinition)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class OperationDefinitionContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    __tablename__ = "OperationDefinitionContact"

    name = Column(primitives.StringField)
    """ Name of a individual to contact.
        Type `str`. """

    telecom = Column(primitives.StringField,
                     ForeignKey('ContactPoint.id'))
    """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """

    def __init__(self, name, telecom,):
        """ Initialize all valid properties.
        """
        self.name = name
        self.telecom = telecom

    def __repr__(self):
        return '<OperationDefinitionContact %r>' % 'self.property'  # replace self.property


class OperationDefinitionParameterBinding(backboneelement.BackboneElement):
    """ ValueSet details if this is coded.

    Binds to a value set if this parameter is coded (code, Coding,
    CodeableConcept).
    """

    __tablename__ = "OperationDefinitionParameterBinding"

    strength = Column(primitives.StringField)
    """ required | extensible | preferred | example.
        Type `str`. """

    # todo valueSetReference = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    valueSetReference = Column(primitives.StringField)
    """ Source of value set.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """

    valueSetUri = Column(primitives.StringField)
    """ Source of value set.
        Type `str`. """

    def __init__(self, strength, valueSetReference, valueSetUri,):
        """ Initialize all valid properties.
        """
        self.strength = strength
        self.valueSetReference = valueSetReference
        self.valueSetUri = valueSetUri

    def __repr__(self):
        return '<OperationDefinitionParameterBinding %r>' % 'self.property'  # replace self.property


class OperationDefinitionParameter(backboneelement.BackboneElement):
    """ Parameters for the operation/query.

    The parameters for the operation/query.
    """

    __tablename__ = "OperationDefinitionParameter"

    binding = Column(primitives.StringField,
                     ForeignKey(
                         'OperationDefinitionParameterBinding.id'))
    """ ValueSet details if this is coded.
        Type `OperationDefinitionParameterBinding` (represented as `dict` in JSON). """

    documentation = Column(primitives.StringField)
    """ Description of meaning/use.
        Type `str`. """

    max = Column(primitives.StringField)
    """ Maximum Cardinality (a number or *).
        Type `str`. """

    min = Column(primitives.IntegerField)
    """ Minimum Cardinality.
        Type `int`. """

    name = Column(primitives.StringField)
    """ Name in Parameters.parameter.name or in URL.
        Type `str`. """

    part = Column(primitives.StringField,
                  ForeignKey('OperationDefinitionParameter.id'))
    """ Parts of a Tuple Parameter.
        List of `OperationDefinitionParameter` items
        (represented as `dict` in JSON). """

    # todo profile = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    profile = Column(primitives.StringField)
    """ Profile on the type.
        Type `FHIRReference` referencing `StructureDefinition`
        (represented as `dict` in JSON). """

    type = Column(primitives.StringField)
    """ What type this parameter has.
        Type `str`. """

    use = Column(primitives.StringField)
    """ in | out.
        Type `str`. """

    def __init__(self, binding, documentation, max, min, name, part,
                 profile, type, use,):
        """ Initialize all valid properties.
        """
        self.binding = binding
        self.documentation = documentation
        self.max = max
        self.min = min
        self.name = name
        self.part = part
        self.profile = profile
        self.type = type
        self.use = use

    def __repr__(self):
        return '<OperationDefinitionParameter %r>' % 'self.property'  # replace self.property


class OperationDefinition(domainresource.DomainResource):
    """ Definition of an operation or a named query.

    A formal computable definition of an operation (on the RESTful interface)
    or a named query (using the search interaction).
    """

    __tablename__ = "OperationDefinition"
    
    # todo base = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    base = Column(primitives.StringField)
    """ Marks this as a profile of the base.
        Type `FHIRReference` referencing `OperationDefinition`
        (represented as `dict` in JSON). """
    
    code = Column(primitives.StringField)
    """ Name used to invoke the operation.
        Type `str`. """
    
    contact = Column(primitives.StringField,
                     ForeignKey('OperationDefinitionContact.id'))
    """ Contact details of the publisher.
        List of `OperationDefinitionContact` items (represented as `dict` in JSON). """
    
    date = Column(primitives.DateTimeField)
    """ Date for this version of the operation definition.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    description = Column(primitives.StringField)
    """ Natural language description of the operation.
        Type `str`. """
    
    experimental = Column(primitives.BooleanField)
    """ If for testing purposes, not real usage.
        Type `bool`. """
    
    idempotent = Column(primitives.BooleanField)
    """ Whether content is unchanged by operation.
        Type `bool`. """
    
    instance = Column(primitives.BooleanField)
    """ Invoke on an instance?.
        Type `bool`. """
    
    kind = Column(primitives.StringField)
    """ operation | query.
        Type `str`. """
    
    name = Column(primitives.StringField)
    """ Informal name for this operation.
        Type `str`. """
    
    notes = Column(primitives.StringField)
    """ Additional information about use.
        Type `str`. """
    
    parameter = Column(primitives.StringField,
                       ForeignKey('OperationDefinitionParameter.id'))
    """ Parameters for the operation/query.
        List of `OperationDefinitionParameter` items (represented as `dict` in JSON). """
    
    publisher = Column(primitives.StringField)
    """ Name of the publisher (Organization or individual).
        Type `str`. """
    
    requirements = Column(primitives.StringField)
    """ Why is this needed?.
        Type `str`. """
    
    status = Column(primitives.StringField)
    """ draft | active | retired.
        Type `str`. """
    
    system = Column(primitives.BooleanField)
    """ Invoke at the system level?.
        Type `bool`. """
    
    type = Column(primitives.StringField)
    """ Invoke at resource level for these type.
        List of `str` items. """
    
    url = Column(primitives.StringField)
    """ Logical URL to reference this operation definition.
        Type `str`. """
    
    version = Column(primitives.StringField)
    """ Logical id for this version of the operation definition.
        Type `str`. """

    def __init__(self, base, code, contact, date, description, experimental,
                 idempotent, instance, kind, name, notes, parameter,
                 publisher, requirements, status, system, type, url, version,):
        """ Initialize all valid properties.
        """
        self.base = base
        self.code = code
        self.contact = contact
        self.date = date
        self.description = description
        self.experimental = experimental
        self.idempotent = idempotent
        self.instance = instance
        self.kind = kind
        self.name = name
        self.notes = notes
        self.parameter = parameter
        self.publisher = publisher
        self.requirements = requirements
        self.status = status
        self.system = system
        self.type = type
        self.url = url
        self.version = version

    def __repr__(self):
        return '<OperationDefinition %r>' % 'self.property'  # replace self.property
