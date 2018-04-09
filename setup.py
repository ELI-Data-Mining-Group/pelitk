# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys
from os import path

here = path.abspath(path.dirname(__file__))

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='lextools',
    version='0.1.0',
    description='Package for processing text to measure lexical diversity.',
    long_description=readme,
    author='Daniel Zheng',
    author_email='daniel.zheng@pitt.edu',
    url='https://github.com/ELI-Data-Mining-Group/lextools',
    license=license,
    install_requires=['nltk'],
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'lextools': ['data/wordlists/*.txt', 'data/*.pkl']},
    include_package_data=True
)
