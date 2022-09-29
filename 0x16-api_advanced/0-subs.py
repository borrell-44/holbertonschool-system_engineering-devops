#!/usr/bin/python3

"""Get the number of subscribers from the Reddit API"""

import json
import requests


def number_of_subscribers(subreddit):
    """Return number of subs of the subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {'User-Agent': 'Custom Agent',
              'From': '4517@holbertonstudents.com'}

    try:
        val = requests.get(url, headers=header).json()
    except json.decoder.JSONDecodeError:
        return 0
    if val.get('error') == 404:
        return 0

    return val.get('data').get('subscribers')
