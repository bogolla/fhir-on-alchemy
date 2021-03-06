#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Location)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import domainresource
from . import backboneelement

class LocationPosition(backboneelement.BackboneElement):
    """ The absolute geographic location.

    The absolute geographic location of the Location, expressed using the WGS84
    datum (This is the same co-ordinate system used in KML).
    """

    __tablename__ = "LocationPosition"

    altitude = Column(primitives.DecimalField)
    """ Altitude with WGS84 datum.
        Type `float`. """

    latitude = Column(primitives.DecimalField)
    """ Latitude with WGS84 datum.
        Type `float`. """

    longitude = Column(primitives.DecimalField)
    """ Longitude with WGS84 datum.
        Type `float`. """

    def __init__(self, altitude, latitude, longitude,):
        """ Initialize all valid properties.
        """
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return '<LocationPosition %r>' % 'self.property'  # replace self.property


class Location(domainresource.DomainResource):
    """ Details and position information for a physical place.

    Details and position information for a physical place where services are
    provided  and resources and participants may be stored, found, contained or
    accommodated.
    """

    __tablename__ = "Location"
    
    address = Column(primitives.StringField,
                     ForeignKey('Address.id'))
    """ Physical location.
        Type `Address` (represented as `dict` in JSON). """
    
    description = Column(primitives.StringField)
    """ Description of the location.
        Type `str`. """
    
    identifier = Column(primitives.StringField,
                        ForeignKey('Identifier.id'))
    """ Unique code or number identifying the location to its users.
        List of `Identifier` items (represented as `dict` in JSON). """
    
    # todo managingOrganization = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    managingOrganization = Column(primitives.StringField)
    """ Organization responsible for provisioning and upkeep.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
    
    mode = Column(primitives.StringField)
    """ instance | kind.
        Type `str`. """
    
    name = Column(primitives.StringField)
    """ Name of the location as used by humans.
        Type `str`. """
    
    # todo partOf = Column(primitives.StringField, ForeignKey('FHIRReference.id'))
    partOf = Column(primitives.StringField)
    """ Another Location this one is physically part of.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
    
    physicalType = Column(primitives.StringField,
                          ForeignKey('CodeableConcept.id'))
    """ Physical form of the location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
    
    position = Column(primitives.StringField,
                      ForeignKey('LocationPosition.id'))
    """ The absolute geographic location.
        Type `LocationPosition` (represented as `dict` in JSON). """
    
    status = Column(primitives.StringField)
    """ active | suspended | inactive.
        Type `str`. """
    
    telecom = Column(primitives.StringField,
                     ForeignKey('ContactPoint.id'))
    """ Contact details of the location.
        List of `ContactPoint` items (represented as `dict` in JSON). """
    
    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Type of function performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, address, description, identifier,
                 managingOrganization, mode, name, partOf,
                 physicalType, position, status, telecom, type,):
        """ Initialize all valid properties.
        """
        self.address = address
        self.description = description
        self.identifier = identifier
        self.managingOrganization = managingOrganization
        self.mode = mode
        self.name = name
        self.partOf = partOf
        self.physicalType = physicalType
        self.position = position
        self.status = status
        self.telecom = telecom
        self.type = type

    def __repr__(self):
        return '<Location %r>' % 'self.property'  # replace self.property
