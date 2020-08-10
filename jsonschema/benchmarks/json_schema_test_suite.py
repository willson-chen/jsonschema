#!/usr/bin/env python
"""
A performance benchmark using the official test suite.

This benchmarks jsonschema using every valid example in the
JSON-Schema-Test-Suite. It will take some time to complete.
"""
import os

from pyperf import Runner

from jsonschema.tests._suite import Suite

class PeakmemSuite:

    def peakmem_json_schema(self):
        file = os.getenv("toxinidir") +"/json"
        os.environ["JSON_SCHEMA_TEST_SUITE"] = file
        Suite().benchmark(runner=Runner())
