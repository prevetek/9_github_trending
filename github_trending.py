import requests
import json
from datetime import timedelta, datetime


def get_trending_repositories(top_size=20):
    seven_days_ago = datetime.now() - timedelta(7)
    payload = {'q': 'created:>' + seven_days_ago.strftime("%Y-%m-%d"),
               'sort': 'stars',
               'per_page': top_size}
    response = requests.get("https://api.github.com/search/repositories", params=payload)
    return json.loads(response.text)['items']


def main():
    repos = get_trending_repositories()
    for repo in repos:
        print('Repo name: ', repo['name'])
        print('  URL:     ', repo['html_url'])
        print('  Stars:   ', repo['stargazers_count'])
        print('  Issues:  ', repo['open_issues'])
        print()


if __name__ == '__main__':
    main()
