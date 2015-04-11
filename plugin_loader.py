#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pkgutil, re, importlib

u"""
* is wildcard
ex)
myapp_plugin_*
"""
def load_plugin(plugin_naming_rule):
    prepat = "^" + re.escape(plugin_naming_rule).replace("\\*", "[a-zA-Z0-9_]+") + "$"
    pat = re.compile(prepat)
    return [
        importlib.import_module(m[1])
        for m in pkgutil.iter_modules()
        if pat.match(m[1])
    ]
