from setuptools import setup, find_packages

NAME = 'pyptools'
VERSION = '0.01'
DESCRIPTION = 'Tools for parsing line delimited log files'
URL = 'https://github.com/tandreas/pyptools'
AUTHOR = 'Trevor Andreas'
AUTHOR_EMAIL = 'tandreas@gmail.com'
LICENSE = 'MIT'
PACKAGES = find_packages(exclude=['tests', 'tests.*'])


params = {
    'name': NAME,
    'version': VERSION,
    'description': DESCRIPTION,
    'url': URL,
    'author': AUTHOR,
    'auhtor_email': AUTHOR_EMAIL,
    'license': LICENSE,
    'packages': PACKAGES,
}

setup(**params)
