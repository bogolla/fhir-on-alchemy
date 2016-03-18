#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Subscription)
#  Date: 2016-03-18.


from . import domainresource

class Subscription(domainresource.DomainResource):
    """ A server push subscription criteria.

    The subscription resource is used to define a push based subscription from
    a server to another system. Once a subscription is registered with the
    server, the server checks every resource that is created or updated, and if
    the resource matches the given criteria, it sends a message on the defined
    "channel" so that another system is able to take an appropriate action.
    """

    __tablename__ = "Subscription"

    channel = Column()
    """ The channel on which to report matches to the criteria.
        Type `SubscriptionChannel` (represented as `dict` in JSON). """

    contact = Column(ContactPoint)
    """ Contact details for source (e.g. troubleshooting).
        List of `ContactPoint` items (represented as `dict` in JSON). """

    criteria = Column()
    """ Rule for server push criteria.
        Type `str`. """

    end = Column()
    """ When to automatically delete the subscription.
        Type `FHIRDate` (represented as `str` in JSON). """

    error = Column()
    """ Latest error note.
        Type `str`. """

    reason = Column()
    """ Description of why this subscription was created.
        Type `str`. """

    status = Column()
    """ requested | active | error | off.
        Type `str`. """

    tag = Column(Coding)
    """ A tag to add to matching resources.
        List of `Coding` items (represented as `dict` in JSON). """

    def __init__(self, channel, contact, criteria, end, error, reason, status, tag,):
        """ Initialize all valid properties.
        """
        self.channel = channel
        self.contact = contact
        self.criteria = criteria
        self.end = end
        self.error = error
        self.reason = reason
        self.status = status
        self.tag = tag

    def __repr__(self):
        return '<Subscription %r>' % 'self.property'  # replace self.property


from . import backboneelement

class SubscriptionChannel(backboneelement.BackboneElement):
    """ The channel on which to report matches to the criteria.

    Details where to send notifications when resources are received that meet
    the criteria.
    """

    __tablename__ = "SubscriptionChannel"

    endpoint = Column()
    """ Where the channel points to.
        Type `str`. """

    header = Column()
    """ Usage depends on the channel type.
        Type `str`. """

    payload = Column()
    """ Mimetype to send, or blank for no payload.
        Type `str`. """

    type = Column()
    """ rest-hook | websocket | email | sms | message.
        Type `str`. """

    def __init__(self, endpoint, header, payload, type,):
        """ Initialize all valid properties.
        """
        self.endpoint = endpoint
        self.header = header
        self.payload = payload
        self.type = type

    def __repr__(self):
        return '<SubscriptionChannel %r>' % 'self.property'  # replace self.property


from . import coding
from . import contactpoint
from . import fhirdate