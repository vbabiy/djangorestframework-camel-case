#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

readme = open("README.rst").read()
history = open("HISTORY.rst").read().replace(".. :changelog:", "")
import djangorestframework_camel_case

def extract_requires():
    with Path('requirements.txt').open() as reqs:
        return [req.strip() for req in reqs if not req.startswith(("#", "--", "-r")) and req.strip()]

setup(
    name="djangorestframework-camel-case",
    version=djangorestframework_camel_case.__version__,
    description="Camel case JSON support for Django REST framework.",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    author="Vitaly Babiy",
    author_email="vbabiy86@gmail.com",
    url="https://github.com/vbabiy/djangorestframework-camel-case",
    packages=["djangorestframework_camel_case"],
    package_dir={"djangorestframework_camel_case": "djangorestframework_camel_case"},
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=extract_requires(),
    license="BSD",
    zip_safe=False,
    keywords="djangorestframework_camel_case",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    test_suite="tests",
)
