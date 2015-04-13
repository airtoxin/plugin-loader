#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
from setuptools import setup

with open("README") as f:
    long_description = f.read()

setup(
    name="plugin-loader",
    version="0.1.1",
    description="import helper for your app's plugin.",
    long_description=long_description,
    author="airtoxin",
    author_email="airtoxin@icloud.com",
    url="https://github.com/airtoxin/plugin-loader",
    py_modules=["plugin_loader"],
    include_package_data=True,
    install_requires=[],
    tests_require=[
        "Flask",
        "Flask-Dropbox",
        "Flask-ErrorHandler",
        "Flask-HTTPAuth",
        "nose"
    ],
    license="MIT",
    keywords="",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Utilities"
    ]
)
