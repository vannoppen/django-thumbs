#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- mode: python -*-
# vi: set ft=python :


import os
from setuptools import setup, find_packages


README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README')
DESCRIPTION = 'Easy image thumbnails in Django.'
if os.path.exists(README_PATH): LONG_DESCRIPTION = open(README_PATH).read()
else: LONG_DESCRIPTION = DESCRIPTION


setup(
    name='django-thumbs',
    version='1.0.0',
    install_requires=['django', 'south'],
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='VanNoppen Marketing',
    author_email='dev@vannoppen.com',
    url='https://github.com/vannoppen/django-thumbs/',
    packages=['thumbs'],
)
