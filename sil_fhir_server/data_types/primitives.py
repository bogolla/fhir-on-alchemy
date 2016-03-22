from sqlalchemy import types
from sqlalchemy_utils import EncryptedType


class BooleanField(types.Boolean):
    """
    true or false values (0 and 1 are not valid values) and
    should cater for optional boolean fields """

    # TODO extend this type to include null and blank fields
    # def __init__(self, *args, **kwargs):
    #     kwargs['null'] = kwargs.get('null', False)
    #     kwargs['blank'] = kwargs.get('blank', False)
    #     super(BooleanField, self).__init__(*args, **kwargs)


class IntegerField(types.Integer):
    """
    A signed 32-bit integer (for larger values, use decimal) """


class StringField(types.Text):
    """
    A sequence of Unicode characters. Note that strings SHALL NOT exceed 1MB
    in size """


class DecimalField(types.DECIMAL):
    """
    Rational numbers that have a decimal representation.
    Note: decimals may not use exponents, and leading 0 digits are not allowed
    """


class URIField(types.Text):  # TODO: rethink the URI field implementation
    """
    A Uniform Resource Identifier Reference (RFC 3986 ).
    Note: URIs are case sensitive. """


class Base64Field(EncryptedType):  # TODO test for all edge cases
    """
    A stream of bytes, base64 encoded (RFC 4648)
    """


class InstantField(types.DateTime):
    """ An instant in time - known at least to the second and always
    includes a time zone.

    Note: This is intended for precisely observed times (typically
    system logs etc.), and not human-reported times - for them, use
    date and dateTime. instant is a more constrained dateTime. This
    type is for system times, not human times (see date and
    dateTime below).
    """


class DateField(types.Date):
    """
    A date, or partial date (e.g. just year or year + month) as used
    in human communication.

    There is no time zone. Dates SHALL be valid dates.
    date is a union of the w3c schema types date, gYearMonth, and gYear
    """

    regex = (
        r'-?([1-9][0-9]{3}|0[0-9]{3})(-(0[1-9]|1[0-2])'
        r'(-(0[1-9]|[12][0-9]|3[01]))?)?'
    )


class DateTimeField(InstantField):
    """ A date, date-time or partial date (e.g. just year or year + month)
    as used in human communication.

    If hours and minutes are specified, a time zone SHALL be populated.
    Seconds must be provided due to schema type constraints but may be
    zero-filled and may be ignored. Dates SHALL be valid dates.
    The time "24:00" is not allowed
    """
    regex = (
        r'-?([1-9][0-9]{3}|0[0-9]{3})(-(0[1-9]|1[0-2])'
        r'(-(0[1-9]|[12][0-9]|3[01])(T(([01][0-9]|2[0-3])'
        r':[0-5][0-9]:[0-5][0-9](\.[0-9]+)?|(24:00:00(\.0+)?))(Z|(\+|-)'
        r'((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?)?)?)?'
    )


class TimeField(types.Time):
    """ A time during the day, with no date specified (can be converted
    to a Duration since midnight). Seconds must be provided due to schema
    type constraints but may be zero-filled and may be ignored. The time
    "24:00" is not allowed, and neither is a time zone
    """
    regex = (
        r'([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?)'
    )


class CodeField(types.String):
    """
    Indicates that the value is taken from a set of controlled strings defined
    elsewhere (see Using codes for further discussion). Technically, a code is
    restricted to a string which has at least one character and no leading or
    trailing whitespace, and where there is no whitespace other than single
    spaces in the contents
    """
    regex = r'[^\s]+([\s]+[^\s]+)*'


class IdField(types.String):
    """
    Any combination of upper or lower case ASCII letters
    ('A'..'Z', and 'a'..'z', numerals ('0'..'9'), '-' and '.', with a length
    limit of 64 characters. (This might be an integer, an un-prefixed OID,
    UUID or any other identifier pattern that meets these constraints.)
    """
    regex = r'[a-z0-9\-\.]{1,36}'


class OIDField(URIField):
    """
    An OID represented as a URI (RFC 3001): urn:oid:1.2.3.4.5
    """


class UUIDField(URIField):
    """
    A UUID, represented as a URI (RFC 4122):
    urn:uuid:a5afddf4-e880-459b-876e-e4591b0acc11.
    Note the RFC comments about case: UUID values SHALL be represented in
    lower case, but systems SHOULD interpret them case insensitively
    """
