#!/usr/bin/python3
"""Module that defines a function used to query Reddit API"""

from requests import get


def number_of_subscribers(subreddit):
    """Returns the number of subreddit subscribers"""
    if not isinstance(subreddit, str) or subreddit is None:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:app_iygeal:1.0.0 (by /u/iygeal)"}

    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    subs = response.json()

    try:
        return subs.get('data').get('subscribers')
    except Exception:
        return 0
