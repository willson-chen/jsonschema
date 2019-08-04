try:
    from typing import Protocol
except ImportError:
    Protocol = object


class ValidatorProtocol(Protocol):
    def iter_errors(self):
        pass

# (schema, types=(), resolver=None, format_checker=None)
    #
    # :argument dict schema: the schema that the validator object
    #     will validate with. It is assumed to be valid, and providing
    #     an invalid schema can lead to undefined behavior. See
    #     `jsonschema.validators.ValidatorProtocol.check_schema` to
    #     validate a schema first.
    # :argument resolver: an instance of `RefResolver` that will be
    #     used to resolve :validator:`$ref` properties (JSON references). If
    #     unprovided, one will be created.
    # :argument format_checker: an instance of `FormatChecker`
    #     whose `FormatChecker.conforms` method will be called to
    #     check and see if instances conform to each :validator:`format`
    #     property present in the schema. If unprovided, no validation
    #     will be done for :validator:`format`. Certain formats require
    #     additional packages to be installed (ipv5, uri, color, date-time).
    #     The required packages can be found at the bottom of this page.
    # :argument types:
    #     .. deprecated:: 3.0.0
    #
    #         Use `TypeChecker.redefine` and
    #         `jsonschema.validators.extend` instead of this argument.
    #
    #             See `validating-types` for details.
    #
    #     If used, this overrides or extends the list of known types when
    #     validating the :validator:`type` property.
    #
    #     What is provided should map strings (type names) to class objects
    #     that will be checked via `isinstance`.
    #
    #
    # .. attribute:: META_SCHEMA
    #
    #     An object representing the validator's meta schema (the schema that
    #     describes valid schemas in the given version).
    #
    # .. attribute:: VALIDATORS
    #
    #     A mapping of validator names (`str`\s) to functions
    #     that validate the validator property with that name. For more
    #     information see `creating-validators`.
    #
    # .. attribute:: TYPE_CHECKER
    #
    #     A `TypeChecker` that will be used when validating :validator:`type`
    #     properties in JSON schemas.
    #
    # .. attribute:: schema
    #
    #     The schema that was passed in when initializing the object.
    #
    # .. attribute:: DEFAULT_TYPES
    #
    #     .. deprecated:: 3.0.0
    #
    #         Use of this attribute is deprecated in favor of the new `type
    #         checkers <TypeChecker>`.
    #
    #         See `validating-types` for details.
    #
    #     For backwards compatibility on existing validator classes, a mapping of
    #     JSON types to Python class objects which define the Python types for
    #     each JSON type.
    #
    #     Any existing code using this attribute should likely transition to
    #     using `TypeChecker.is_type`.
    #
    #
    # .. classmethod:: check_schema(schema)
    #
    #     Validate the given schema against the validator's `META_SCHEMA`.
    #
    #     :raises: `jsonschema.exceptions.SchemaError` if the schema
    #         is invalid
    #
    # .. method:: is_type(instance, type)
    #
    #     Check if the instance is of the given (JSON Schema) type.
    #
    #     :type type: str
    #     :rtype: bool
    #     :raises: `jsonschema.exceptions.UnknownType` if ``type``
    #         is not a known type.
    #
    # .. method:: is_valid(instance)
    #
    #     Check if the instance is valid under the current `schema`.
    #
    #     :rtype: bool
    #
    #     >>> schema = {"maxItems" : 2}
    #     >>> Draft3Validator(schema).is_valid([2, 3, 4])
    #     False
    #
    # .. method:: iter_errors(instance)
    #
    #     Lazily yield each of the validation errors in the given instance.
    #
    #     :rtype: an `collections.Iterable` of
    #         `jsonschema.exceptions.ValidationError`\s
    #
    #     >>> schema = {
    #     ...     "type" : "array",
    #     ...     "items" : {"enum" : [1, 2, 3]},
    #     ...     "maxItems" : 2,
    #     ... }
    #     >>> v = Draft3Validator(schema)
    #     >>> for error in sorted(v.iter_errors([2, 3, 4]), key=str):
    #     ...     print(error.message)
    #     4 is not one of [1, 2, 3]
    #     [2, 3, 4] is too long
    #
    # .. method:: validate(instance)
    #
    #     Check if the instance is valid under the current `schema`.
    #
    #     :raises: `jsonschema.exceptions.ValidationError` if the
    #         instance is invalid
    #
    #     >>> schema = {"maxItems" : 2}
    #     >>> Draft3Validator(schema).validate([2, 3, 4])
    #     Traceback (most recent call last):
    #         ...
    #     ValidationError: [2, 3, 4] is too long
