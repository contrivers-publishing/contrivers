#-*- coding: utf-8 -*-

import unittest

from .fixtures import _create_app

class JinjaTestCase(unittest.TestCase):
    """ Tests for the Jinja environment

    Tests
    Functions
    Filters
    Context variables
    """

    def create_app(self):
        return _create_app()

    def setUp(self):
        self.env = self.create_app().jinja_env

    def tearDown(self):
        del self.env

    def test_env_has_md_filter(self):
        """the jinja env should have a function called `md`"""
        self.assertIn('md', self.env.filters, "the jinja env should have a function called `md`")
