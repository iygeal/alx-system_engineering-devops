#!/usr/bin/python3
"""Module that defines a script to print
  sorted keyword counts from hot posts recursively
"""

from requests import get


def count_words(subreddit, word_list, hot_list=[], after=None, word_count={}):
    """Function that counts keywords in hot posts recursively"""

    if not isinstance(subreddit, str) or not isinstance(
            word_list, list) or subreddit is None:
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
        for post in posts["data"]["children"]:
            # Convert titles to lowercase
            hot_list.append(post["data"]["title"].lower())

        # Get the value of "after" for pagination
        after = posts["data"]["after"]
        if after:
            return count_words(
                subreddit, word_list, hot_list, after, word_count)

        # Count occurrences of each keyword in hot_list
        for word in word_list:
            word_lower = word.lower()
            count = sum(title.split().count(word_lower) for title in hot_list)
            if word_lower in word_count:
                word_count[word_lower] += count
            else:
                word_count[word_lower] = count

        # Sort word_count by count (descending) and then alphabetically
        sorted_word_count = sorted(
            word_count.items(), key=lambda item: (-item[1], item[0]))

        for word, count in sorted_word_count:
            if count > 0:
                print(f"{word}: {count}")

    except Exception as e:
        print(e)
        return None
