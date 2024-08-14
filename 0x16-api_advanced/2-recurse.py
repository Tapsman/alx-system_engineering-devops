#!/usr/bin/python3
"""
Recursive function that queri Redddit api
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """The function the returns all the list of titles per subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "taps_man"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=header, params=params,
                            allow_redirescts=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count = count + results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
