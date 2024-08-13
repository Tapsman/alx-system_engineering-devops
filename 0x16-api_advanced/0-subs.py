#!/usr/bin/python3

"""
This script will querry the Reddit API, return number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """Function returns total num of subscribers on given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "taps-app/0.0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
