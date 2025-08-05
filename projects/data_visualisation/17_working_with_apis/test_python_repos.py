import pytest
import requests


@pytest.fixture
def github_api_response():
    """ Fixture to fetch the GitHUb API response. """
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)
    return response

def test_status_code(github_api_response):
    """ Assert that the value of status_code is 200. """
    assert github_api_response.status_code == 200

def test_items_count(github_api_response):
    """ Assert that the number of items is expected """
    response_dict = github_api_response.json()
    assert len(response_dict['items']) == 30

def test_total_repositories(github_api_response):
    """ Assert that the total number of repositories is greater than 200 """
    response_dict = github_api_response.json()
    assert response_dict['total_count'] > 200
    