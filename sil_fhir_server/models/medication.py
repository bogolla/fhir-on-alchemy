#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Medication)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class MedicationPackageContent(backboneelement.BackboneElement):
    """ What is  in the package.

    A set of components that go to make up the described item.
    """

    __tablename__ = "MedicationPackageContent"

    amount = Column(primitives.StringField,
                    ForeignKey('Quantity.id'))
    """ Quantity present in the package.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    # todo item = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    item = Column(primitives.StringField)
    """ A product in the package.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """

    def __init__(self, amount, item,):
        """ Initialize all valid properties.
        """
        self.amount = amount
        self.item = item

    def __repr__(self):
        return '<MedicationPackageContent %r>' % 'self.property'  # replace self.property


class MedicationPackage(backboneelement.BackboneElement):
    """ Details about packaged medications.

    Information that only applies to packages (not products).
    """

    __tablename__ = "MedicationPackage"

    container = Column(primitives.StringField,
                       ForeignKey('CodeableConcept.id'))
    """ E.g. box, vial, blister-pack.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    content = Column(primitives.StringField,
                     ForeignKey('MedicationPackageContent.id'))
    """ What is  in the package.
        List of `MedicationPackageContent` items (represented as `dict` in JSON). """

    def __init__(self, container, content,):
        """ Initialize all valid properties.
        """
        self.container = container
        self.content = content

    def __repr__(self):
        return '<MedicationPackage %r>' % 'self.property'  # replace self.property


class MedicationProductBatch(backboneelement.BackboneElement):
    """ None.

    Information about a group of medication produced or packaged from one
    production run.
    """

    __tablename__ = "MedicationProductBatch"

    expirationDate = Column(primitives.DateTimeField)
    """ None.
        Type `FHIRDate` (represented as `str` in JSON). """

    lotNumber = Column(primitives.StringField)
    """ None.
        Type `str`. """

    def __init__(self, expirationDate, lotNumber,):
        """ Initialize all valid properties.
        """
        self.expirationDate = expirationDate
        self.lotNumber = lotNumber

    def __repr__(self):
        return '<MedicationProductBatch %r>' % 'self.property'  # replace self.property


class MedicationProductIngredient(backboneelement.BackboneElement):
    """ Active or inactive ingredient.

    Identifies a particular constituent of interest in the product.
    """

    __tablename__ = "MedicationProductIngredient"

    amount = Column(primitives.StringField,
                    ForeignKey('Ratio.id'))
    """ Quantity of ingredient present.
        Type `Ratio` (represented as `dict` in JSON). """

    # todo item = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    item = Column(primitives.StringField)
    """ The product contained.
        Type `FHIRReference` referencing `Substance, Medication`
        (represented as `dict` in JSON). """

    def __init__(self, amount, item,):
        """ Initialize all valid properties.
        """
        self.amount = amount
        self.item = item

    def __repr__(self):
        return '<MedicationProductIngredient %r>' % 'self.property'  # replace self.property


class MedicationProduct(backboneelement.BackboneElement):
    """ Administrable medication details.

    Information that only applies to products (not packages).
    """

    __tablename__ = "MedicationProduct"

    batch = Column(primitives.StringField,
                   ForeignKey('MedicationProductBatch.id'))
    """ None.
        List of `MedicationProductBatch` items
        (represented as `dict` in JSON). """

    form = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ powder | tablets | carton +.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    ingredient = Column(primitives.StringField,
                        ForeignKey('MedicationProductIngredient.id'))
    """ Active or inactive ingredient.
        List of `MedicationProductIngredient` items (represented as `dict` in JSON). """

    def __init__(self, batch, form, ingredient,):
        """ Initialize all valid properties.
        """
        self.batch = batch
        self.form = form
        self.ingredient = ingredient

    def __repr__(self):
        return '<MedicationProduct %r>' % 'self.property'  # replace self.property


class Medication(domainresource.DomainResource):
    """ Definition of a Medication.

    This resource is primarily used for the identification and definition of a
    medication. It covers the ingredients and the packaging for a medication.
    """

    __tablename__ = "Medication"
    
    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Codes that identify this medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    isBrand = Column(primitives.BooleanField)
    """ True if a brand.
        Type `bool`. """
    
    # todo manufacturer = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    manufacturer = Column(primitives.StringField)
    """ Manufacturer of the item.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
    
    package = Column(primitives.StringField,
                     ForeignKey('MedicationPackage.id'))
    """ Details about packaged medications.
        Type `MedicationPackage` (represented as `dict` in JSON). """
    
    product = Column(primitives.StringField,
                     ForeignKey('MedicationProduct.id'))
    """ Administrable medication details.
        Type `MedicationProduct` (represented as `dict` in JSON). """

    def __init__(self, code, isBrand, manufacturer, package, product):
        """ Initialize all valid properties.
        """
        self.code = code
        self.isBrand = isBrand
        self.manufacturer = manufacturer
        self.package = package
        self.product = product

    def __repr__(self):
        return '<Medication %r>' % 'self.property'  # replace self.property
