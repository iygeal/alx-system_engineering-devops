#!/usr/bin/python3
"""Module that defines a script to print hot posts recursively"""

from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """Function that prints hot posts recursively"""

    if not isinstance(subreddit, str) or subreddit is None:
        return None

    # Construct the URL with the after parameter if it exists
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"

    headers = {"User-Agent": "python:app_iygeal:1.0.0 (by /u/iygeal)"}

    try:
        response = get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return None

        posts = response.json()
        for post in posts["data"]["children"]:  # Get the list of posts
            hot_list += [post["data"]["title"]]  # Add the title to the list

        # Get the value of "after" for pagination
        after = posts["data"]["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    except Exception:
        return None
