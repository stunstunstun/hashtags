import requests
from bs4 import BeautifulSoup
from hashtags.contants import GITHUB_API


class Github:

    def __init__(self):
        self.headers = {}

    @classmethod
    def trend_repositories(cls, since='weekly', count=5):
        body = requests.get(GITHUB_API + '?since={}'.format(since))
        if body.status_code != 200:
            raise Exception('HTTP status code is not OK[{}]'.format(body.status_code))
        return GithubResponse(count).parse_html(body.text)


class GithubResponse:

    def __init__(self, count):
        self.count = count

    def parse_html(self, body):
        soup = BeautifulSoup(body, 'html.parser')
        div = soup.find_all('div', class_='explore-content')[0]
        items = div.find_all('li')[:self.count]
        return [GithubResponse.get_repository(item) for item in items]

    @classmethod
    def get_repository(cls, item):
        title = item.find('h3').find('a').get('href').split('/')[2]
        url = 'https://github.com{}'.format(item.find('h3').find('a').get('href'))
        stars = item.find('div', class_='f6 text-gray mt-2').find('span', class_='d-inline-block float-sm-right').text
        stars = stars.replace(' ', '').replace('starsthisweek', '').replace('\n', '')
        span = item.find('div', class_='f6 text-gray mt-2').find('span', class_='d-inline-block mr-3').find('span', itemprop='programmingLanguage')
        lang = 'None' if span is None else span.text.replace(' ', '').replace('\n', '')
        return {'title': title, 'url': url, 'stars': stars, 'lang': 'in ' + lang}

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u'GithubResponse(count={count})'.format(count=self.count)
