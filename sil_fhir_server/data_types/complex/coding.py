#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Coding)
#  Date: 2016-03-18.


from sqlalchemy import Column
from sil_fhir_server.data_types import primitives
from . import complex_dt


class Coding(complex_dt.ComplexElement):
    """ A reference to a code defined by a terminology system. """

    __tablename__ = "Coding"

    code = Column(primitives.StringField)
    """ Symbol in syntax defined by the system.
        Type `str`. """

    display = Column(primitives.StringField)
    """ Representation defined by the system.
        Type `str`. """

    system = Column(primitives.StringField)
    """ Identity of the terminology system.
        Type `str`. """

    userSelected = Column(primitives.BooleanField)
    """ If this coding was chosen directly by the user.
        Type `bool`. """

    version = Column(primitives.StringField)
    """ Version of the system - if relevant.
        Type `str`. """

    def __init__(self, code, display, system, userSelected, version):
        """ Initialize all valid properties.
        """
        self.code = code
        self.display = display
        self.system = system
        self.userSelected = userSelected
        self.version = version

    def __repr__(self):
        return '<Coding %r>' % self.display
