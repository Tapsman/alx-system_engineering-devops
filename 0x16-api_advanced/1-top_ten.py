#!/usr/bin/python3
"""
Queries Reddit API and prints top 10 titles
"""
import requests
from sys import argv


def top_ten(subreddit):
    """
    This function the returns the top 10 provided subreddit
    """
    user = {'User-Agent': 'taps_man'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
