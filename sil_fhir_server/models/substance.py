#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Substance)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class SubstanceIngredient(backboneelement.BackboneElement):
    """ Composition information about the substance.

    A substance can be composed of other substances.
    """

    __tablename__ = "SubstanceIngredient"

    quantity = Column(primitives.StringField,
                      ForeignKey('Ratio.id'))
    """ Optional amount (concentration).
        Type `Ratio` (represented as `dict` in JSON). """

    # todo substance = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    substance = Column(primitives.StringField)
    """ A component of the substance.
        Type `FHIRReference` referencing `Substance` (represented as `dict` in JSON). """

    def __init__(self, quantity, substance,):
        """ Initialize all valid properties.
        """
        self.quantity = quantity
        self.substance = substance

    def __repr__(self):
        return '<SubstanceIngredient %r>' % 'self.property'  # replace self.property


class SubstanceInstance(backboneelement.BackboneElement):
    """ If this describes a specific package/container of the substance.

    Substance may be used to describe a kind of substance, or a specific
    package/container of the substance: an instance.
    """

    __tablename__ = "SubstanceInstance"

    expiry = Column(primitives.DateField)
    """ When no longer valid to use.
        Type `FHIRDate` (represented as `str` in JSON). """

    # todo identifier = Column(primitives.StringField, ForeignKey('Identifier.id'))
    identifier = Column(primitives.StringField)
    """ Identifier of the package/container.
        Type `Identifier` (represented as `dict` in JSON). """

    quantity = Column(primitives.StringField,
                      ForeignKey('Quantity.id'))
    """ Amount of substance in the package.
        Type `Quantity` referencing `SimpleQuantity`
        (represented as `dict` in JSON). """

    def __init__(self, expiry, identifier, quantity,):
        """ Initialize all valid properties.
        """
        self.expiry = expiry
        self.identifier = identifier
        self.quantity = quantity

    def __repr__(self):
        return '<SubstanceInstance %r>' % 'self.property'  # replace self.property


class Substance(domainresource.DomainResource):
    """ A homogeneous material with a definite composition.
    """

    __tablename__ = "Substance"
    
    category = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ What class/type of substance this is.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ What substance this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    description = Column(primitives.StringField)
    """ Textual description of the substance, comments.
        Type `str`. """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    ingredient = Column(primitives.StringField,
                        ForeignKey('SubstanceIngredient.id'))
    """ Composition information about the substance.
        List of `SubstanceIngredient` items (represented as `dict` in JSON). """
    
    instance = Column(primitives.StringField,
                      ForeignKey('SubstanceInstance.id'))
    """ If this describes a specific package/container of the substance.
        List of `SubstanceInstance` items (represented as `dict` in JSON). """

    def __init__(self, category, code, description, identifier,
                 ingredient, instance,):
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
