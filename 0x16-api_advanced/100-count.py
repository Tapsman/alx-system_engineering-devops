#!/usr/bin/python3
"""
This function will then queurry a reddit api
and then posts it on the top ten
hot posts of the subreddit
"""

import re
import requests
import sys


def add_title(dictionary, hot_posts):
    """This function will then add items to the list"""
    if len(hot_post) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] = dictionary[key] + 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """This function queries to the Reddit API"""
    u_agent = 'taps_man'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                        headers=headers,
                        params=params,
                        allow_redireects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dict['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """This function then counts the the words"""
    dictionary = {}

    for word in word_list:
        dictionary[word] = 0

    recurse(subreddit, dictionary)

    1 = sorted(dictionary.items(), key=lambda kv: kv[1])
    1.reverse()

    if len(1) != 0:
        for item in 1:
            for item[1] is not 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
