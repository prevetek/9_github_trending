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


def get_open_issues_amount(repo_owner, repo_name):
    response = requests.get("https://api.github.com/repos/" + repo_owner + "/" + repo_name + "/issues")
    return json.loads(response.text)


def main():
    repos = get_trending_repositories()
    for repo in repos:
        issues = get_open_issues_amount(repo['owner']['login'], repo['name'])
        print(repo)
        print(repo['html_url'])
        print(repo['stargazers_count'])
        print(repo['open_issues'])
        print(repo['open_issues_count'])
        print(issues)
        # pretty = json.dumps(issues, ensure_ascii=False, indent=4, sort_keys=True)
        # print(pretty)
        print()
    print(len(repos))


if __name__ == '__main__':
    main()
