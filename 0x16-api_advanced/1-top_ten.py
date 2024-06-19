#!/usr/bin/python3
"""Module that defines a scirpt used to query top 10 hot posts
    from a subreddit from the Reddit API
"""

from requests import get


def top_ten(subreddit):
    """Function that prints top 10 hot posts from a subreddit"""

    if not isinstance(subreddit, str) or subreddit is None:
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {"User-Agent": "python:app_iygeal:1.0.0 (by /u/iygeal)"}

    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    else:
        try:
            posts = response.json()

            for post in posts["data"]["children"]:
                print(post["data"]["title"])
        except Exception:
            print(None)
            return
