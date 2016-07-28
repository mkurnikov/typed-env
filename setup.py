#!/usr/bin/env python
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = open('README.md').read()

requirements = []

test_requirements = [
    'twine==1.7.4',
    'pandoc==1.0.0b2',
    'bumpversion==0.5.3'
]

setup(
    name='typed-env',
    version='0.1.1',
    description="Fast-fail environment variable library.",
    long_description=long_description,
    author="Maxim Kurnikov",
    author_email='maxim.kurnikov@gmail.com',
    url='https://github.com/mkurnikov/typed-env',
    license="MIT",

    install_requires=requirements,
    tests_require=test_requirements,
    packages=find_packages(exclude=['typed_env.tests'])
)
