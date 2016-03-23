#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/NutritionOrder)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement


class NutritionOrderEnteralFormulaAdministration(backboneelement.BackboneElement):
    """ Formula feeding instruction as structured data.

    Formula administration instructions as structured data.  This repeating
    structure allows for changing the administration rate or volume over time
    for both bolus and continuous feeding.  An example of this would be an
    instruction to increase the rate of continuous feeding every 2 hours.
    """

    __tablename__ = "NutritionOrderEnteralFormulaAdministration"

    quantity = Column(primitives.StringField,
                      ForeignKey('Quantity.id'))
    """ The volume of formula to provide.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    rateQuantity = Column(primitives.StringField,
                          ForeignKey('Quantity.id'))
    """ Speed with which the formula is provided per period of time.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    rateRatio = Column(primitives.StringField,
                       ForeignKey('Ratio.id'))
    """ Speed with which the formula is provided per period of time.
        Type `Ratio` (represented as `dict` in JSON). """

    schedule = Column(primitives.StringField,
                      ForeignKey('Timing.id'))
    """ Scheduled frequency of enteral feeding.
        Type `Timing` (represented as `dict` in JSON). """

    def __init__(self, quantity, rateQuantity, rateRatio, schedule,):
        """ Initialize all valid properties.
        """
        self.quantity = quantity
        self.rateQuantity = rateQuantity
        self.rateRatio = rateRatio
        self.schedule = schedule

    def __repr__(self):
        return '<NutritionOrderEnteralFormulaAdministration %r>' % 'self.property'  # replace self.property


class NutritionOrderOralDietNutrient(backboneelement.BackboneElement):
    """ Required  nutrient modifications.

    Class that defines the quantity and type of nutrient modifications required
    for the oral diet.
    """

    __tablename__ = "NutritionOrderOralDietNutrient"

    amount = Column(primitives.StringField,
                    ForeignKey('Quantity.id'))
    """ Quantity of the specified nutrient.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    modifier = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Type of nutrient that is being modified.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, amount, modifier,):
        """ Initialize all valid properties.
        """
        self.amount = amount
        self.modifier = modifier

    def __repr__(self):
        return '<NutritionOrderOralDietNutrient %r>' % 'self.property'  # replace self.property


class NutritionOrderOralDietTexture(backboneelement.BackboneElement):
    """ Required  texture modifications.

    Class that describes any texture modifications required for the patient to
    safely consume various types of solid foods.
    """

    __tablename__ = "NutritionOrderOralDietTexture"

    foodType = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Concepts that are used to identify an entity that is ingested for
        nutritional purposes.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    modifier = Column(primitives.StringField,
                      ForeignKey('CodeableConcept.id'))
    """ Code to indicate how to alter the texture of the foods, e.g. pureed.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, foodType, modifier,):
        """ Initialize all valid properties.
        """
        self.foodType = foodType
        self.modifier = modifier

    def __repr__(self):
        return '<NutritionOrderOralDietTexture %r>' % 'self.property'  # replace self.property


class NutritionOrderSupplement(backboneelement.BackboneElement):
    """ Supplement components.

    Oral nutritional products given in order to add further nutritional value
    to the patient's diet.
    """

    __tablename__ = "NutritionOrderSupplement"

    instruction = Column(primitives.StringField)
    """ Instructions or additional information about the oral supplement.
        Type `str`. """

    productName = Column(primitives.StringField)
    """ Product or brand name of the nutritional supplement.
        Type `str`. """

    quantity = Column(primitives.StringField,
                      ForeignKey('Quantity.id'))
    """ Amount of the nutritional supplement.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    schedule = Column(primitives.StringField,
                      ForeignKey('Timing.id'))
    """ Scheduled frequency of supplement.
        List of `Timing` items (represented as `dict` in JSON). """

    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Type of supplement product requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, instruction, productName, quantity, schedule, type,):
        """ Initialize all valid properties.
        """
        self.instruction = instruction
        self.productName = productName
        self.quantity = quantity
        self.schedule = schedule
        self.type = type

    def __repr__(self):
        return '<NutritionOrderSupplement %r>' % 'self.property'  # replace self.property


class NutritionOrderOralDiet(backboneelement.BackboneElement):
    """ Oral diet components.

    Diet given orally in contrast to enteral (tube) feeding.
    """

    __tablename__ = "NutritionOrderOralDiet"

    fluidConsistencyType = Column(primitives.StringField,
                                  ForeignKey('CodeableConcept.id'))
    """ The required consistency of fluids and liquids provided to the
        patient.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    instruction = Column(primitives.StringField)
    """ Instructions or additional information about the oral diet.
        Type `str`. """

    nutrient = Column(primitives.StringField,
                      ForeignKey('NutritionOrderOralDietNutrient.id'))
    """ Required  nutrient modifications.
        List of `NutritionOrderOralDietNutrient` items (represented as `dict` in JSON). """

    schedule = Column(primitives.StringField,
                      ForeignKey('Timing.id'))
    """ Scheduled frequency of diet.
        List of `Timing` items (represented as `dict` in JSON). """

    texture = Column(primitives.StringField,
                     ForeignKey('NutritionOrderOralDietTexture.id'))
    """ Required  texture modifications.
        List of `NutritionOrderOralDietTexture` items (represented as `dict` in JSON). """

    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Type of oral diet or diet restrictions that describe what can be
        consumed orally.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

    def __init__(self, fluidConsistencyType, instruction, nutrient, schedule, texture, type,):
        """ Initialize all valid properties.
        """
        self.fluidConsistencyType = fluidConsistencyType
        self.instruction = instruction
        self.nutrient = nutrient
        self.schedule = schedule
        self.texture = texture
        self.type = type

    def __repr__(self):
        return '<NutritionOrderOralDiet %r>' % 'self.property'  # replace self.property


class NutritionOrderEnteralFormula(backboneelement.BackboneElement):
    """ Enteral formula components.

    Feeding provided through the gastrointestinal tract via a tube, catheter,
    or stoma that delivers nutrition distal to the oral cavity.
    """

    __tablename__ = "NutritionOrderEnteralFormula"

    additiveProductName = Column(primitives.StringField)
    """ Product or brand name of the modular additive.
        Type `str`. """

    additiveType = Column(primitives.StringField,
                          ForeignKey('CodeableConcept.id'))
    """ Type of modular component to add to the feeding.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    administration = Column(primitives.StringField,
                            ForeignKey('NutritionOrderEnteralFormulaAdministration.id'))
    """ Formula feeding instruction as structured data.
        List of `NutritionOrderEnteralFormulaAdministration` items (represented as `dict` in JSON). """

    administrationInstruction = Column(primitives.StringField)
    """ Formula feeding instructions expressed as text.
        Type `str`. """

    baseFormulaProductName = Column(primitives.StringField)
    """ Product or brand name of the enteral or infant formula.
        Type `str`. """

    baseFormulaType = Column(primitives.StringField,
                             ForeignKey('CodeableConcept.id'))
    """ Type of enteral or infant formula.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    caloricDensity = Column(primitives.StringField,
                            ForeignKey('Quantity.id'))
    """ Amount of energy per specified volume that is required.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    maxVolumeToDeliver = Column(primitives.StringField,
                                ForeignKey('Quantity.id'))
    """ Upper limit on formula volume per unit of time.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    routeofAdministration = Column(primitives.StringField,
                                   ForeignKey('CodeableConcept.id'))
    """ How the formula should enter the patient's gastrointestinal tract.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, additiveProductName, additiveType,
                 administration, administrationInstruction,
                 baseFormulaProductName, baseFormulaType,
                 caloricDensity, maxVolumeToDeliver,
                 routeofAdministration,):
        """ Initialize all valid properties.
        """
        self.additiveProductName = additiveProductName
        self.additiveType = additiveType
        self.administration = administration
        self.administrationInstruction = administrationInstruction
        self.baseFormulaProductName = baseFormulaProductName
        self.baseFormulaType = baseFormulaType
        self.caloricDensity = caloricDensity
        self.maxVolumeToDeliver = maxVolumeToDeliver
        self.routeofAdministration = routeofAdministration

    def __repr__(self):
        return '<NutritionOrderEnteralFormula %r>' % 'self.property'  # replace self.property


class NutritionOrder(domainresource.DomainResource):
    """ A request for a diet, formula or nutritional supplement.

    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
    """

    __tablename__ = "NutritionOrder"
    
    # todo allergyIntolerance = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    allergyIntolerance = Column(primitives.StringField)
    """ List of the patient's food and nutrition-related allergies and
        intolerances.
        List of `FHIRReference` items referencing `AllergyIntolerance`
        (represented as `dict` in JSON). """
    
    dateTime = Column(primitives.DateTimeField)
    """ Date and time the nutrition order was requested.
        Type `FHIRDate` (represented as `str` in JSON). """
    
    # todo encounter = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    encounter = Column(primitives.StringField)
    """ The encounter associated with this nutrition order.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
    
    enteralFormula = Column(primitives.StringField,
                            ForeignKey(
                                'NutritionOrderEnteralFormula.id'))
    """ Enteral formula components.
        Type `NutritionOrderEnteralFormula` (represented as `dict` in JSON). """
    
    excludeFoodModifier = Column(primitives.StringField,
                                 ForeignKey('CodeableConcept.id'))
    """ Order-specific modifier about the type of food that should not be
        given.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    foodPreferenceModifier = Column(primitives.StringField,
                                    ForeignKey('CodeableConcept.id'))
    """ Order-specific modifier about the type of food that should be given.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Identifiers assigned to this order.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    oralDiet = Column(primitives.StringField,
                      ForeignKey('NutritionOrderOralDiet.id'))
    """ Oral diet components.
        Type `NutritionOrderOralDiet` (represented as `dict` in JSON). """
    
    # todo orderer = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    orderer = Column(primitives.StringField)
    """ Who ordered the diet, formula or nutritional supplement.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
    
    # todo patient = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    patient = Column(primitives.StringField)
    """ The person who requires the diet, formula or nutritional supplement.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ proposed | draft | planned | requested | active | on-hold |
        completed | cancelled.
        Type `str`. """
    
    supplement = Column(primitives.StringField,
                        ForeignKey('NutritionOrderSupplement.id'))
    """ Supplement components.
        List of `NutritionOrderSupplement` items (represented as `dict` in JSON). """

    def __init__(self, allergyIntolerance, dateTime, encounter, enteralFormula,
                 excludeFoodModifier, foodPreferenceModifier, identifier,
                 oralDiet, orderer, patient, status, supplement,):
        """ Initialize all valid properties.
        """
        self.allergyIntolerance = allergyIntolerance
        self.dateTime = dateTime
        self.encounter = encounter
        self.enteralFormula = enteralFormula
        self.excludeFoodModifier = excludeFoodModifier
        self.foodPreferenceModifier = foodPreferenceModifier
        self.identifier = identifier
        self.oralDiet = oralDiet
        self.orderer = orderer
        self.patient = patient
        self.status = status
        self.supplement = supplement

    def __repr__(self):
        return '<NutritionOrder %r>' % 'self.property'  # replace self.property
