#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Timing)
#  Date: 2016-03-18.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from sil_fhir_server.data_types.complex import complex_dt


class TimingRepeat(complex_dt.ComplexElement):
    """ When the event is to occur.

    A set of rules that describe when the event should occur.
    """

    __tablename__ = "TimingRepeat"

    boundsPeriod = Column(primitives.StringField,
                          ForeignKey('Period.id'))
    """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Period` (represented as `dict` in JSON). """

    boundsQuantity = Column(primitives.StringField,
                            ForeignKey('Quantity.id'))
    """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Quantity` referencing `Duration` (represented as `dict` in JSON). """

    boundsRange = Column(primitives.StringField,
                         ForeignKey('Range.id'))
    """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Range` (represented as `dict` in JSON). """

    count = Column(primitives.IntegerField)
    """ Number of times to repeat.
        Type `int`. """

    duration = Column(primitives.DecimalField)
    """ How long when it happens.
        Type `float`. """

    durationMax = Column(primitives.DecimalField)
    """ How long when it happens (Max).
        Type `float`. """

    durationUnits = Column(primitives.StringField)
    """ s | min | h | d | wk | mo | a - unit of time (UCUM).
        Type `str`. """

    frequency = Column(primitives.IntegerField)
    """ Event occurs frequency times per period.
        Type `int`. """

    frequencyMax = Column(primitives.IntegerField)
    """ Event occurs up to frequencyMax times per period.
        Type `int`. """

    period = Column(primitives.DecimalField)
    """ Event occurs frequency times per period.
        Type `float`. """

    periodMax = Column(primitives.DecimalField)
    """ Upper limit of period (3-4 hours).
        Type `float`. """

    periodUnits = Column(primitives.StringField)
    """ s | min | h | d | wk | mo | a - unit of time (UCUM).
        Type `str`. """

    when = Column(primitives.StringField)
    """ Regular life events the event is tied to.
        Type `str`. """

    def __init__(self, boundsPeriod, boundsQuantity, boundsRange,
                 count, duration, durationMax, durationUnits,
                 frequency, frequencyMax, period, periodMax,
                 periodUnits, when):
        """ Initialize all valid properties.
        """
        self.boundsPeriod = boundsPeriod
        self.boundsQuantity = boundsQuantity
        self.boundsRange = boundsRange
        self.count = count
        self.duration = duration
        self.durationMax = durationMax
        self.durationUnits = durationUnits
        self.frequency = frequency
        self.frequencyMax = frequencyMax
        self.period = period
        self.periodMax = periodMax
        self.periodUnits = periodUnits
        self.when = when

    def __repr__(self):
        return '<TimingRepeat %r>' % 'self.property'  # replace self.property


class Timing(complex_dt.ComplexElement):
    """ A timing schedule that specifies an event that may occur multiple times.

    Specifies an event that may occur multiple times. Timing schedules are used
    to record when things are expected or requested to occur. The most common
    usage is in dosage instructions for medications. They are also used when
    planning care of various kinds.
    """

    __tablename__ = "Timing"

    code = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ QD | QOD | Q4H | Q6H | BID | TID | QID | AM | PM +.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    event = Column(primitives.DateTimeField)
    """ When the event occurs.
        List of `FHIRDate` items (represented as `str` in JSON). """

    repeat = Column(primitives.StringField,
                  ForeignKey('TimingRepeat.id'))
    """ When the event is to occur.
        Type `TimingRepeat` (represented as `dict` in JSON). """

    def __init__(self, code, event, repeat):
        """ Initialize all valid properties.
        """
        self.code = code
        self.event = event
        self.repeat = repeat

    def __repr__(self):
        return '<Timing %r>' % 'self.property'  # replace self.property
