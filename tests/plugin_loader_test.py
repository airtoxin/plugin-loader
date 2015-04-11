#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from unittest import TestCase
from nose.tools import ok_, eq_
from plugin_loader import load_plugin

class PluginLoaderTestCase(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_load(self):
        import nose
        plugin_rule = "nose"
        eq_(
            load_plugin(plugin_rule),
            [nose]
        )

    def test_noplugin(self):
        plugin_rule = "@&%$)((0$&&%"
        eq_(
            load_plugin(plugin_rule),
            []
        )

    def test_wildcard(self):
        import xmllib, xmlrpclib
        plugin_rule = "xml*"
        eq_(
            load_plugin(plugin_rule),
            [xmllib, xmlrpclib]
        )

    def test_flask_plugin(self):
        plugin_rule = "flask_*"
        import flask_dropbox, flask_errorhandler, flask_httpauth
        eq_(
            load_plugin(plugin_rule),
            [flask_dropbox, flask_errorhandler, flask_httpauth]
        )
