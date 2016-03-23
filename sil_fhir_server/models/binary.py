#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Binary)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import resource


class Binary(resource.Resource):
    """ Pure binary content defined by some other format than FHIR.

    A binary resource can contain any content, whether text, image, pdf, zip
    archive, etc.
    """

    __tablename__ = "Binary"
    
    content = Column(primitives.StringField)
    """ The actual content.
        Type `str`. """
    
    contentType = Column(primitives.StringField)
    """ MimeType of the binary content.
        Type `str`. """

    def __init__(self, content, contentType,):
        """ Initialize all valid properties.
        """
        self.content = content
        self.contentType = contentType

    def __repr__(self):
        return '<Binary %r>' % 'self.property'  # replace self.property