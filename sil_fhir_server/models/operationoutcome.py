#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/OperationOutcome)
#  Date: 2016-03-18.


from . import domainresource

class OperationOutcome(domainresource.DomainResource):
    """ Information about the success/failure of an action.

    A collection of error, warning or information messages that result from a
    system action.
    """

    __tablename__ = "OperationOutcome"

    issue = Column(OperationOutcomeIssue)
    """ A single issue associated with the action.
        List of `OperationOutcomeIssue` items (represented as `dict` in JSON). """

    def __init__(self, issue,):
        """ Initialize all valid properties.
        """
        self.issue = issue

    def __repr__(self):
        return '<OperationOutcome %r>' % 'self.property'  # replace self.property


from . import backboneelement

class OperationOutcomeIssue(backboneelement.BackboneElement):
    """ A single issue associated with the action.

    An error, warning or information message that results from a system action.
    """

    __tablename__ = "OperationOutcomeIssue"

    code = Column()
    """ Error or warning code.
        Type `str`. """

    details = Column()
    """ Additional details about the error.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    diagnostics = Column()
    """ Additional diagnostic information about the issue.
        Type `str`. """

    location = Column(str)
    """ XPath of element(s) related to issue.
        List of `str` items. """

    severity = Column()
    """ fatal | error | warning | information.
        Type `str`. """

    def __init__(self, code, details, diagnostics, location, severity,):
        """ Initialize all valid properties.
        """
        self.code = code
        self.details = details
        self.diagnostics = diagnostics
        self.location = location
        self.severity = severity

    def __repr__(self):
        return '<OperationOutcomeIssue %r>' % 'self.property'  # replace self.property


from . import codeableconcept