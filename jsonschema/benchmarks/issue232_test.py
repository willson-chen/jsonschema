#!/usr/bin/env python
"""
A performance benchmark using the example from issue #232.

See https://github.com/Julian/jsonschema/pull/232.
"""
from pathlib import Path

from pyperf import Runner
from pyrsistent import m

from jsonschema.tests._suite import Version
import jsonschema

issue232 = Version(
    path=Path(__file__).parent / "issue232_test",
    remotes=m(),
    name="issue232_test",
)

class PeakmemSuite:

    def peakmem_issue(self):
        issue232.benchmark(
            runner=Runner(),
            Validator=jsonschema.Draft4Validator,
        )
