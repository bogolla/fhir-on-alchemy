#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Substance)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class Substance(domainresource.DomainResource):
    """ A homogeneous material with a definite composition.
    """

    __tablename__ = "Substance"

    category = Column(CodeableConcept)
    """ What class/type of substance this is.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    code = Column(CodeableConcept)
    """ What substance this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    description = Column(primitives.StringField)
    """ Textual description of the substance, comments.
        Type `str`. """

    identifier = Column(Identifier)
    """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

    ingredient = Column(SubstanceIngredient)
    """ Composition information about the substance.
        List of `SubstanceIngredient` items (represented as `dict` in JSON). """

    instance = Column(SubstanceInstance)
    """ If this describes a specific package/container of the substance.
        List of `SubstanceInstance` items (represented as `dict` in JSON). """

    def __init__(self, category, code, description, identifier, ingredient, instance,):
        """ Initialize all valid properties.
        """
        self.category = category
        self.code = code
        self.description = description
        self.identifier = identifier
        self.ingredient = ingredient
        self.instance = instance

    def __repr__(self):
        return '<Substance %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class SubstanceIngredient(backboneelement.BackboneElement):
    """ Composition information about the substance.

    A substance can be composed of other substances.
    """

    __tablename__ = "SubstanceIngredient"

    quantity = Column(Ratio)
    """ Optional amount (concentration).
        Type `Ratio` (represented as `dict` in JSON). """

    substance = Column(FHIRReference)
    """ A component of the substance.
        Type `FHIRReference` referencing `Substance` (represented as `dict` in JSON). """

    def __init__(self, quantity, substance,):
        """ Initialize all valid properties.
        """
        self.quantity = quantity
        self.substance = substance

    def __repr__(self):
        return '<SubstanceIngredient %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
class SubstanceInstance(backboneelement.BackboneElement):
    """ If this describes a specific package/container of the substance.

    Substance may be used to describe a kind of substance, or a specific
    package/container of the substance: an instance.
    """

    __tablename__ = "SubstanceInstance"

    expiry = Column(FHIRDate)
    """ When no longer valid to use.
        Type `FHIRDate` (represented as `str` in JSON). """

    identifier = Column(Identifier)
    """ Identifier of the package/container.
        Type `Identifier` (represented as `dict` in JSON). """

    quantity = Column(Quantity)
    """ Amount of substance in the package.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    def __init__(self, expiry, identifier, quantity,):
        """ Initialize all valid properties.
        """
        self.expiry = expiry
        self.identifier = identifier
        self.quantity = quantity

    def __repr__(self):
        return '<SubstanceInstance %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio