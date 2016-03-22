#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Attachment)
#  Date: 2016-03-18.


from sqlalchemy import Column
from sil_fhir_server.data_types import primitives
from . import complex_dt


class Attachment(complex_dt.ComplexElement):
    """ Content in a format defined elsewhere.

    For referring to data content defined in other formats.
    """

    __tablename__ = "Attachment"

    contentType = Column(primitives.StringField)
    """ Mime type of the content, with charset etc..
        Type `str`. """

    creation = Column(primitives.DateTimeField)
    """ Date attachment was first created.
        Type `FHIRDate` (represented as `str` in JSON). """

    data = Column(primitives.StringField)
    """ Data inline, base64ed.
        Type `str`. """

    hash = Column(primitives.StringField)
    """ Hash of the data (sha-1, base64ed).
        Type `str`. """

    language = Column(primitives.StringField)
    """ Human language of the content (BCP-47).
        Type `str`. """

    size = Column(primitives.IntegerField)
    """ Number of bytes of content (if url provided).
        Type `int`. """

    title = Column(primitives.StringField)
    """ Label to display in place of the data.
        Type `str`. """

    url = Column(primitives.StringField)
    """ Uri where the data can be found.
        Type `str`. """

    def __init__(self, contentType, creation, data, hash, language,
                 size, title, url):
        """ Initialize all valid properties. """
        self.contentType = contentType
        self.creation = creation
        self.data = data
        self.hash = hash
        self.language = language
        self.size = size
        self.title = title
        self.url = url

    def __repr__(self):
        return '<Attachment %r>' % self.title
