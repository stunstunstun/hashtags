# -*- coding: utf-8 -*-
import unittest

from tests.helper import ICON, attach_rank
from hashtags.github import Github


class TestGithub(unittest.TestCase):

    def setUp(self):
        self.github = Github()

    def test_trend_repositories(self):
        repositories = self.github.trend_repositories(since='weekly', count=5)
        contents = '''이 주의 Github Trending! {}\n\n{}'''.format(
            ICON['SMILE'],
            '\n'.join([attach_rank(index) + ' ' + item['title'] + ' ' + item['lang'] + ' ' + ICON['STAR'] + ' ' + item['stars'] + '\n- ' + item['url'] + '\n' for index, item in enumerate(repositories)]))
        print(contents)
        self.assertEqual(len(repositories), 5)

