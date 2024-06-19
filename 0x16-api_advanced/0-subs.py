#!/usr/bin/python3
""""Module that defines a function used to query Reddit API"""

from requests import get


def number_of_subscribers(subreddit):
    """Returns the number of subreddit subscribers"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = get(url)
    if response.status_code != 200:
        return 0

    results = response.json()
    try:
        return results.get("data").get("subscribers")

    except Exception:
        return 0
