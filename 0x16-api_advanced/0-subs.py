#!/usr/bin/python3

"""Get the number of subscribers from the Reddit API"""

import json
import requests


def number_of_subscribers(subreddit):
    """Return number of subs of the subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        val = requests.get(url).json()
    except json.decoder.JSONDecodeError:
        return 0
    if 'data' not in val.keys():
        return 0

    return val.data.subscribers

    for k in d.keys():
        if k == 'data':
            print(d[k].get('subscribers'))

    return 1
