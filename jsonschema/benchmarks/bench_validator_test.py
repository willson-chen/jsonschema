from twisted.trial.unittest import SynchronousTestCase
from jsonschema import  TypeChecker, exceptions, validators


def startswith(validator, startswith, instance, schema):
    if not instance.startswith(startswith):
        yield exceptions.ValidationError(u"Whoops!")


class TimeSuite(SynchronousTestCase):
    def setUp(self):
        self.addCleanup(
            self.assertEqual,
            validators.meta_schemas,
            dict(validators.meta_schemas),
        )

        self.meta_schema = {u"$id": "some://meta/schema"}
        self.validators = {u"startswith": startswith}
        self.type_checker = TypeChecker()
        self.Validator = validators.create(
            meta_schema=self.meta_schema,
            validators=self.validators,
            type_checker=self.type_checker,
        )

    def time_attrs(self):
        self.assertEqual(
            (
                self.Validator.VALIDATORS,
                self.Validator.META_SCHEMA,
                self.Validator.TYPE_CHECKER,
            ), (
                self.validators,
                self.meta_schema,
                self.type_checker,
            ),
        )

    def time_init(self):
        schema = {u"startswith": u"foo"}
        self.Validator(schema).schema, schema

    def time_iter_errors(self):
        schema = {u"startswith": u"hel"}
        self.Validator(schema).iter_errors
