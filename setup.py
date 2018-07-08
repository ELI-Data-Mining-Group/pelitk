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
    name='pelitk',
    version='0.1.3',
    description='Package for processing text to measure lexical diversity.',
    long_description=readme,
    author='Daniel Zheng',
    author_email='daniel.zheng@pitt.edu',
    url='https://github.com/ELI-Data-Mining-Group/pelitk',
    license=license,
    install_requires=['nltk', 'scipy', 'numpy'],
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'pelitk': ['data/wordlists/*.txt', 'data/*.pkl']},
    include_package_data=True
)

import nltk
if 'install' in sys.argv:
    nltk.download('wordnet')
