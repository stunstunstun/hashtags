import requests
from hashtags.compat import json
from hashtags.contants import REDDIT_API


class Reddit:
    """
    For Reddit
    """
    def __init__(self):
        self.headers = {'User-Agent': 'super happy flair bot by /u/spladug'}

    def top_posts(self, limit=5, time='week'):
        body = requests.get(REDDIT_API + 'limit={}&t={}'.format(limit, time), headers=self.headers)
        if body.status_code != 200:
            raise Exception('HTTP status code is not OK[{}]'.format(body.status_code))
        return RedditResponse.parse_posts(body.text)


class RedditResponse:
    """Result that is translated"""
    SUCCESS_CODE = 0

    def __init__(self, code=None, message=None):
        self.code = self.SUCCESS_CODE if code is None else code
        self.message = message

    @classmethod
    def parse_posts(cls, body):
        """
        Get an instance from JSON string
        """
        json_dict = json.loads(body)
        posts = json_dict['data']['children']
        return posts

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u'Response(code={code}, message={message})'.format(code=self.code, message=self.message)
