# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys
from os import path

import nltk

here = path.abspath(path.dirname(__file__))

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pelitk',
    version='0.1.4',
    description='Package for processing text, especially texts in PELIC',
    long_description=readme,
    authors='Daniel Zheng, Na-Rae Han, Ben Naismith',
    author_email='naraehan@pitt.edu',
    url='https://github.com/ELI-Data-Mining-Group/pelitk',
    license=license,
    install_requires=['nltk', 'scipy', 'numpy'],
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'pelitk': ['lextools/wordlists/*.txt', 'lextools*.pkl']},
    include_package_data=True
)

if 'install' in sys.argv:
    nltk.download('wordnet')
