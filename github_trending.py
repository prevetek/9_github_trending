import requests
import json
from datetime import timedelta, datetime


def get_date_days_ago(days=0):
    days_ago = datetime.now() - timedelta(days)
    return days_ago.strftime("%Y-%m-%d")


def get_trending_repositories(page_size=100):
    date_week_ago = get_date_days_ago(7)
    payload = {'q': 'created:>' + date_week_ago,
               'sort': 'stars',
               'per_page': page_size}
    response = requests.get("https://api.github.com/search/repositories", params=payload)
    return json.loads(response.text)['items']


def printing(repositories):
    for repo in repositories:
        print('Repo name: {0}\n'
              '  URL:     {1}\n'
              '  Stars:   {2}\n'
              '  Issues:  {3}\n'
              ''.format(repo['name'], repo['html_url'], repo['stargazers_count'], repo['open_issues'])
              )


if __name__ == '__main__':
    page_size = 20
    repositories = get_trending_repositories(page_size)
    printing(repositories)
