import requests
from nicolas.compat import json
from nicolas.contants import NAVER_SEARCH_BOOK_API, DEFAULT_CONTENT_TYPE

client_id = None
client_secret = None


class Book:

    @classmethod
    def list(cls, publisher, numbers=1):
        query = 'd_publ={}&d_catg=280020020&display={}&sort=date&start=1'.format(publisher, numbers)
        headers = {
            'X-Naver-Client-Id': client_id,
            'X-Naver-Client-Secret': client_secret,
            'Content-Type': DEFAULT_CONTENT_TYPE
        }

        body = requests.get(NAVER_SEARCH_BOOK_API + "?" + query, headers=headers)
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
