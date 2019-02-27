# -*- coding: utf-8 -*-
import requests
from hashtags.compat import json
from hashtags.constants import NAVER_API_CLIENT_ID, NAVER_API_CLIENT_SECRET, NAVER_SEARCH_BOOK

DEFAULT_CONTENT_TYPE = 'application/x-www-form-urlencoded; charset=UTF-8'
BOOK_CATEGORY = 280020020

class Book:

    @classmethod
    def list(cls, publisher, numbers=1):
        query = 'd_catg={book_category}&d_publ={publisher}&display={numbers}&sort=date&start=1'.format(book_category=BOOK_CATEGORY, publisher=publisher, numbers=numbers)
        headers = {
            'X-Naver-Client-Id': NAVER_API_CLIENT_ID,
            'X-Naver-Client-Secret': NAVER_API_CLIENT_SECRET,
            'Content-Type': DEFAULT_CONTENT_TYPE
        }

        body = requests.get(NAVER_SEARCH_BOOK + "?" + query, headers=headers)
        if body.status_code != 200:
            raise Exception('HTTP status code is not OK[{}]'.format(body.status_code))
        return BookResponse.parse_book(body.text)


class BookResponse:

    @classmethod
    def parse_book(cls, body):
        """
        Get an instance from JSON string
        """
        json_dict = json.loads(body)
        books = json_dict['items']
        return books
