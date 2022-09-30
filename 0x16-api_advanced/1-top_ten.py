#!/usr/bin/python3

"""Get the number of subscribers from the Reddit API"""

import json
import requests


def top_ten(subreddit):
    """Return number of subs of the subreddit"""

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {'User-Agent': 'Custom Agent',
              'From': '4517@holbertonstudents.com'}

    try:
        val = requests.get(url, headers=header).json()
    except json.decoder.JSONDecodeError:
        print(None)
        return
    if val.get('error') == 404:
        print(None)
        return

    children = val.get('data').get('children')
    for i in range(0, 10):
        if i > len(children):
            return
        print(children[i].get('data').get('title'))
