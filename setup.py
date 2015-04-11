#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
from setuptools import setup

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

with open("test-requirements.txt") as f:
    tests_require = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

setup(
    name="plugin-loader",
    version="0.1.0dev",
    description="importing helper for your app's plugin",
    long_description=long_description,
    author="airtoxin",
    author_email="airtoxin@icloud.com",
    url="https://github.com/airtoxin/plugin-loader",
    py_modules=["plugin_loader"],
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    license="MIT",
    keywords="",
    zip_safe=False,
    classifiers=[
        "development Status :: 1 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ]
)
