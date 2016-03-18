#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR {{ info.version }} on {{ info.date }}.
#  {{ info.year }}, SMART Health IT.

from . import element


class FHIRElementFactory(object):
    """ Factory class to instantiate resources by resource name.
    """
    
    @classmethod
    def instantiate(cls, resource_name, jsondict):
        """ Instantiate a resource of the type correlating to "resource_name".
        
        :param str resource_name: The name/type of the resource to instantiate
        :param dict jsondict: The JSON dictionary to use for data
        :returns: A resource of the respective type or `Element`
        """
        {%- for klass in classes %}{% if klass.resource_name %}
        if "{{ klass.resource_name }}" == resource_name:
            from . import {{ klass.module }}
            return {{ klass.module }}.{{ klass.name }}(jsondict)
        {%- endif %}{% endfor %}
        return element.Element(json)

