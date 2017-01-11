import requests
import json
from datetime import timedelta, datetime


def get_date_days_ago(days=0):
    days_ago = datetime.now() - timedelta(days)
    return days_ago.strftime("%Y-%m-%d")


def get_trending_repositories(page_size=100):
    days_per_week = 7
    date_week_ago = get_date_days_ago(days_per_week)
    payload = {'q': 'created:>{}'.format(date_week_ago),
               'sort': 'stars',
               'per_page': page_size}
    response = requests.get("https://api.github.com/search/repositories", params=payload)
    list_repositories = json.loads(response.text)['items']
    return list_repositories


def printing(repositories):
    for repo in repositories:
        printing_str = """\
Repo name: {0}
 URL:      {1}
 Stars:    {2}
 Issues:   {3}
"""
        print(printing_str.format(repo['name'], repo['html_url'], repo['stargazers_count'], repo['open_issues']))


if __name__ == '__main__':
    page_size = 20
    repositories = get_trending_repositories(page_size)
    printing(repositories)
