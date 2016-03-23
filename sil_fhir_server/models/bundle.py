#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Bundle)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import resource
from . import backboneelement


class BundleLink(backboneelement.BackboneElement):
    """ Links related to this Bundle.

    A series of links that provide context to this bundle.
    """

    __tablename__ = "BundleLink"

    relation = Column(primitives.StringField)
    """ http://www.iana.org/assignments/link-relations/link-relations.xhtml.
        Type `str`. """

    url = Column(primitives.StringField)
    """ Reference details for the link.
        Type `str`. """

    def __init__(self, relation, url,):
        """ Initialize all valid properties.
        """
        self.relation = relation
        self.url = url

    def __repr__(self):
        return '<BundleLink %r>' % 'self.property'  # replace self.property


class BundleEntryRequest(backboneelement.BackboneElement):
    """ Transaction Related Information.

    Additional information about how this entry should be processed as part of
    a transaction.
    """

    __tablename__ = "BundleEntryRequest"

    ifMatch = Column(primitives.StringField)
    """ For managing update contention.
        Type `str`. """

    ifModifiedSince = Column(primitives.DateTimeField)
    """ For managing update contention.
        Type `FHIRDate` (represented as `str` in JSON). """

    ifNoneExist = Column(primitives.StringField)
    """ For conditional creates.
        Type `str`. """

    ifNoneMatch = Column(primitives.StringField)
    """ For managing cache currency.
        Type `str`. """

    method = Column(primitives.StringField)
    """ GET | POST | PUT | DELETE.
        Type `str`. """

    url = Column(primitives.StringField)
    """ URL for HTTP equivalent of this entry.
        Type `str`. """

    def __init__(self, ifMatch, ifModifiedSince, ifNoneExist,
                 ifNoneMatch, method, url,):
        """ Initialize all valid properties.
        """
        self.ifMatch = ifMatch
        self.ifModifiedSince = ifModifiedSince
        self.ifNoneExist = ifNoneExist
        self.ifNoneMatch = ifNoneMatch
        self.method = method
        self.url = url

    def __repr__(self):
        return '<BundleEntryRequest %r>' % 'self.property'  # replace self.property


class BundleEntryResponse(backboneelement.BackboneElement):
    """ Transaction Related Information.

    Additional information about how this entry should be processed as part of
    a transaction.
    """

    __tablename__ = "BundleEntryResponse"

    etag = Column(primitives.StringField)
    """ The etag for the resource (if relevant).
        Type `str`. """

    lastModified = Column(primitives.DateTimeField)
    """ Server's date time modified.
        Type `FHIRDate` (represented as `str` in JSON). """

    location = Column(primitives.StringField)
    """ The location, if the operation returns a location.
        Type `str`. """

    status = Column(primitives.StringField)
    """ Status return code for entry.
        Type `str`. """

    def __init__(self, etag, lastModified, location, status,):
        """ Initialize all valid properties.
        """
        self.etag = etag
        self.lastModified = lastModified
        self.location = location
        self.status = status

    def __repr__(self):
        return '<BundleEntryResponse %r>' % 'self.property'  # replace self.property


class BundleEntrySearch(backboneelement.BackboneElement):
    """ Search related information.

    Information about the search process that lead to the creation of this
    entry.
    """

    __tablename__ = "BundleEntrySearch"

    mode = Column(primitives.StringField)
    """ match | include | outcome - why this is in the result set.
        Type `str`. """

    score = Column(primitives.DecimalField)
    """ Search ranking (between 0 and 1).
        Type `float`. """

    def __init__(self, mode, score,):
        """ Initialize all valid properties.
        """
        self.mode = mode
        self.score = score

    def __repr__(self):
        return '<BundleEntrySearch %r>' % 'self.property'  # replace self.property


class BundleEntry(backboneelement.BackboneElement):
    """ Entry in the bundle - will have a resource, or information.

    An entry in a bundle resource - will either contain a resource, or
    information about a resource (transactions and history only).
    """

    __tablename__ = "BundleEntry"

    fullUrl = Column(primitives.StringField)
    """ Absolute URL for resource (server address, or UUID/OID).
        Type `str`. """

    link = Column(primitives.StringField, ForeignKey('BundleLink.id'))
    """ Links related to this entry.
        List of `BundleLink` items (represented as `dict` in JSON). """

    request = Column(primitives.StringField,
                     ForeignKey('BundleEntryRequest.id'))
    """ Transaction Related Information.
        Type `BundleEntryRequest` (represented as `dict` in JSON). """

    # todo resource = Column(primitives.StringField,
    #                   ForeignKey('Resource.id'))
    resource = Column(primitives.StringField)
    """ A resource in the bundle.
        Type `Resource` (represented as `dict` in JSON). """

    response = Column(primitives.StringField,
                      ForeignKey('BundleEntryResponse.id'))
    """ Transaction Related Information.
        Type `BundleEntryResponse` (represented as `dict` in JSON). """

    search = Column(primitives.StringField,
                    ForeignKey('BundleEntrySearch.id'))
    """ Search related information.
        Type `BundleEntrySearch` (represented as `dict` in JSON). """

    def __init__(self, fullUrl, link, request, resource, response, search,):
        """ Initialize all valid properties.
        """
        self.fullUrl = fullUrl
        self.link = link
        self.request = request
        self.resource = resource
        self.response = response
        self.search = search

    def __repr__(self):
        return '<BundleEntry %r>' % 'self.property'  # replace self.property


class Bundle(resource.Resource):
    """ Contains a collection of resources.

    A container for a collection of resources.
    """

    __tablename__ = "Bundle"
    
    entry = Column(primitives.StringField,
                   ForeignKey('BundleEntry.id'))
    """ Entry in the bundle - will have a resource, or information.
        List of `BundleEntry` items (represented as `dict` in JSON). """
    
    link = Column(primitives.StringField,
                  ForeignKey('BundleLink.id'))
    """ Links related to this Bundle.
        List of `BundleLink` items (represented as `dict` in JSON). """
    
    signature = Column(primitives.StringField,
                       ForeignKey('Signature.id'))
    """ Digital Signature.
        Type `Signature` (represented as `dict` in JSON). """
    
    total = Column(primitives.IntegerField)
    """ If search, the total number of matches.
        Type `int`. """
    
    type = Column(primitives.StringField)
    """ document | message | transaction | transaction-response | batch |
        batch-response | history | searchset | collection.
        Type `str`. """

    def __init__(self, entry, link, signature, total, type,):
        """ Initialize all valid properties.
        """
        self.entry = entry
        self.link = link
        self.signature = signature
        self.total = total
        self.type = type

    def __repr__(self):
        return '<Bundle %r>' % 'self.property'  # replace self.property
