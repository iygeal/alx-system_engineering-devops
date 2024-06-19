#!/usr/bin/python3
""""Module that defines a function used to query Reddit API"""

from requests import get


def number_of_subscribers(subreddit):
    """Returns the number of subreddit subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    if subreddit is None or type(subreddit) is not str:
        return 0

    headers = {"User-Agent": "python:app_iygeal:1.0.0 (by /u/iygeal)"}

    try:
        response = get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        else:
            res_data = response.json()
            subscribers = res_data["data"]["subscribers"]
            return subscribers

    except Exception:
        return 0
