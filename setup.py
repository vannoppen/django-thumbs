import os
from setuptools import setup, find_packages

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')

description = 'Easy image thumbnails in Django.'

if os.path.exists(README_PATH):
    long_description = open(README_PATH).read()
else:
    long_description = description


setup(
    name='django-thumbs',
    version='1.0.0',
    install_requires=[
        'django >= 1.2'
    ],
    description=description,
    long_description=long_description,
    author='VanNoppen',
    author_email='dev@vannoppen.com',
    url='http://github.com/vannoppen/django-vannoppen/',
    packages=['thumbs'],
)
