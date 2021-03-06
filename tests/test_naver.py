# -*- coding: utf-8 -*-
import unittest
import re
import random
from tests.helper import ICON, attach_rank
from hashtags import naver
from hashtags.constants import PUBLISHERS


class TestBook(unittest.TestCase):
    def test_book_list(self):
        books = [naver.Book.list(publisher=publisher, numbers=1)[0] for publisher in random.sample(PUBLISHERS, 5)]
        contents = re.sub(r'\([^)]*\)', '', '이 주의 프로그래밍 신간! {}\n\n{}'.format(
            ICON['BOOK'],
            '\n\n'.join([attach_rank(index) + ' ' + item['title'] + '\n- ' + item['link'] for index, item in enumerate(books)])))
        print(contents)

        self.assertEqual(len(books), 5)

