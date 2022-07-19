# -*- coding: utf-8 -*-

from .context import fts

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(fts.hmm())


if __name__ == '__main__':
    unittest.main()
