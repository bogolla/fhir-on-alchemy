Python FHIR Parser
==================

A Python FHIR specification parser for model class generation.

### Tech ###

The _generate.py_ script downloads [FHIR specification][fhir] files, parses the profiles (using _fhirspec.py_) and represents them as `FHIRClass` instances with `FHIRClassProperty` properties (found in _fhirclass.py_).
Additionally, `FHIRUnitTest` (in _fhirunittest.py_) instances get created that can generate unit tests from provided FHIR examples.
These representations are then used by [Jinja][] templates to create classes in certain programming languages, mentioned below.

This script does its job for the most part, but it doesn't yet handle all FHIR pecularities and there's no guarantee the output is correct or complete.
Unless you have a desire to understand how parsing works, you should be able to play with _Lang/settings.py_, _Lang/mappings.py_ and _Lang/templates*_ to achieve what you need.

### Use ###

1. Copy the file `settings.py` from the language's subdirectory into the project's root directory, then
2. Adjust settings, especially those determining where the generated classes will be copied to, found at the top of `settings.py`.
3. Install requirements by running `pip3` (or `pip`):
    ```bash
    pip3 install -r requirements.txt
    ```

4. Run the script:
    ```bash
    ./generate.py
    ```
    This will use Python _3_, issue `python generate.py` if you don't have Python 3 yet.
    Supply the `-f` flag to force a re-download of the spec.

> NOTE that the script currently overwrites existing files without asking and without regret.


### Requirements ###

The generated Python classes require the following packages to be installed:

```text
isodate
```


Tech Details
------------

This parser still applies some tricks, stemming from the evolving nature of FHIR's profile definitions.
Some tricks may have become obsolete and should be cleaned up.

### How are property names determined?

Every “property” of a class, meaning every `element` in a profile snapshot, is represented as a `FHIRStructureDefinitionElement` instance.
If an element itself defines a class, e.g. `Patient.animal`, calling the instance's `as_properties()` method returns a list of `FHIRClassProperty` instances – usually only one – that indicates a class was found in the profile.
The class of this property is derived from `element.type`, which is expected to only contain one entry, in this matter:

- If _type_ is `BackboneElement`, a class name is constructed from the parent element (in this case _Patient_) and the property name (in this case _animal_), camel-cased (in this case _PatientAnimal_).
- If _type_ is `*`, a class for all classes found in settings` `star_expand_types` is created
- Otherwise, the type is taken as-is (e.g. _CodeableConcept_) and mapped according to mappings' `classmap`, which is expected to be a valid FHIR class.

> TODO: should `http://hl7.org/fhir/StructureDefinition/structuredefinition-explicit-type-name` be respected?


[license]: ./LICENSE.txt
[fhir]: http://www.hl7.org/implement/standards/fhir/
[jinja]: http://jinja.pocoo.org
[client-py]: https://github.com/smart-on-fhir/client-py
