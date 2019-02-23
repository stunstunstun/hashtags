#!/bin/bash

python setup.py egg_info
python setup.py sdist
twine upload dist/hashtags-*.tar.gz
rm -rf dist
