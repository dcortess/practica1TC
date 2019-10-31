#!/usr/bin/env python3

import setuptools


with open('README.md') as f:
    long_description = ''.join(f.readlines())


setuptools.setup(
    name='Practica1: Ludus Strategy',
    version='1.0',
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,

    description='Learning complexity with Python (Pract 1)',
    long_description=long_description,
    author='Jordi Mateo',
    author_email='jordi.mateo@udl.cat',

    install_requires=[
        'matplotlib==3.1.1'
    ],

    extras_require={
        'devel': [
            'mypy==0.620',
            'pylint==2.1.1',
            'pytest==3.7.1',
        ],
    }
)