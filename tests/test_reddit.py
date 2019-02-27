# -*- coding: utf-8 -*-
import unittest
from tests.helper import ICON, attach_rank
from hashtags.reddit import Reddit
from googletrans import Translator


class TestReddit(unittest.TestCase):

    def setUp(self):
        self.reddit = Reddit()

    def test_top_week(self):
        posts = self.reddit.top_posts()
        translator = Translator()
        for post in posts:
            print(post['data']['title'])
            result = translator.translate(text=post['data']['title'], src='en', dest='ko')
            post['data']['title_kr'] = result.text

        contents = '''이 주의 글로벌 HOT 이슈! {}\n\n{}'''.format(
            ICON['SMILE'],
            '\n'.join([attach_rank(index) + ' ' + post['data']['title_kr'] + '\n- ' + post['data']['url'] + '\n'
                       for index, post in enumerate(posts)]))

        print(contents)
        self.assertEqual(len(posts), 5)

    def test_top_today(self):
        posts = self.reddit.top_posts(time='today')
        translator = Translator()
        for post in posts:
            print(post['data']['title'])
            result = translator.translate(text=post['data']['title'], src='en', dest='ko')
            post['data']['title_kr'] = result.text

        contents = '''오늘의 레딧 HOT 이슈! {}\n\n{}'''.format(
            ICON['SMILE'],
            '\n'.join([attach_rank(index) + ' ' + item['data']['title_kr'] + '\n- ' + item['data']['url'] + '\n'
                      for index, item in enumerate(posts)]))

        print(contents)
        self.assertEqual(len(posts), 5)

