# -*- coding: utf-8 -*-
"""PAPAGO Translate API for Python
"""
import os
try:
    from pathlib import Path
except ImportError:
    print('PY2 could not import pathlib.')

from dotenv import load_dotenv
from hashtags.compat import PY3

import hashtags

NAVER_API_CLIENT_ID = 'KBq2FQcv89nHzBILpQ4X'
NAVER_API_CLIENT_SECRET = 'NtYHpSHSUh'
NAVER_SEARCH_BOOK = 'https://openapi.naver.com/v1/search/book_adv.json'
PUBLISHERS = ['위키북스', '한빛미디어', '인사이트', '길벗', '에이콘', '제이펍', '이지스퍼블리싱']

REDDIT_API = 'https://www.reddit.com/r/programming/top/.json?'
GITHUB_API = 'https://github.com/trending'

DEFAULT_ENV = 'dev'
VERSION = hashtags.__version__
ENV = os.environ.get('PYTHON_ENV', DEFAULT_ENV) 
if ENV == DEFAULT_ENV:
    FILE_NAME = '.env'
    ENV_PATH = Path('..') / FILE_NAME if PY3 else os.path.join(os.getcwd(), '..', FILE_NAME)
else:
    FILE_NAME = '{env}.env'.format(env=ENV)
    ENV_PATH = Path('..') / FILE_NAME if PY3 else os.path.join(os.getcwd(), '..', FILE_NAME)

load_dotenv(dotenv_path=ENV_PATH)

MONGO_URI = os.getenv('MONGO_URI')