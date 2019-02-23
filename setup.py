#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
from setuptools import find_packages, setup


def long_description():
    with io.open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(name='nicolas',
      version='0.1.0',
      description='Hola Nicolas!',
      long_description=long_description(),
      url='https://github.com/stunstunstun/nicolas',
      author='stunstunstun',
      author_email='agileboys.com@gmail.com',
      license='MIT',
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7'],
      zip_safe=False,
      test_suite='tests')
