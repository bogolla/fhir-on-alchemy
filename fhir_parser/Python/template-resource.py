#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR {{ info.version }} ({{ profile.url }})
#  Date: {{ info.date }}.

{%- set imported = {} %}
{%- for klass in classes %}


{% if klass.superclass in imports and klass.superclass.module not in imported -%}
from . import {{ klass.superclass.module }}
{% set _ = imported.update({klass.superclass.module: True}) %}
{% endif -%}

class {{ klass.name }}({% if klass.superclass in imports %}{{ klass.superclass.module }}.{% endif -%}
    {{ klass.superclass.name|default('object')}}):
    """ {{ klass.short|wordwrap(width=75, wrapstring="\n    ") }}.
{%- if klass.formal %}

    {{ klass.formal|wordwrap(width=75, wrapstring="\n    ") }}
{%- endif %}
    """
{%- if klass.resource_name %}

    __tablename__ = "{{ klass.resource_name }}"
{%- endif %}
{%- for prop in klass.properties %}

    {{ prop.name }} = Column({% if prop.is_array %}{{ prop.class_name }}{% endif %})
    """ {{ prop.short|wordwrap(67, wrapstring="\n        ") }}.
        {% if prop.is_array %}List of{% else %}Type{% endif %} `{{ prop.class_name }}`{% if prop.is_array %} items{% endif %}
        {%- if prop.reference_to_names|length > 0 %} referencing `{{ prop.reference_to_names|join(', ') }}`{% endif %}
        {%- if prop.json_class != prop.class_name %} (represented as `{{ prop.json_class }}` in JSON){% endif %}. """
{%- endfor %}

    def __init__(self, {%- for prop in klass.properties %} {{ prop.name }}, {%- endfor %}):
        """ Initialize all valid properties.
        """

    {%- for prop in klass.properties %}
        self.{{ prop.name }} = {{ prop.name }}
    {%- endfor %}

    def __repr__(self):
        return '<{{ klass.resource_name }} %r>' % 'self.property'  # replace self.property

{%- endfor %}

{% for imp in imports %}{% if imp.module not in imported %}
from . import {{ imp.module }}
{%- endif %}{% endfor %}
