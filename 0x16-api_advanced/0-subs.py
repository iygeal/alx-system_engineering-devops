#!/usr/bin/python3
"""Module that defines a function used to query Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subreddit subscribers"""
    if not isinstance(subreddit, str) or subreddit.strip() == "":
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:app_iygeal:1.0.0 (by /u/iygeal)"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return 0
        else:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers

    except requests.RequestException as e:
        print(f"Error fetching data for subreddit '{subreddit}': {e}")
        return 0
