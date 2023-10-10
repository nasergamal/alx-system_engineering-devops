#!/usr/bin/python3
'''get subscribers count for a subreddit'''
import requests


def number_of_subscribers(subreddit):
    '''request to reddit api'''
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    x = requests.get(url, headers={'User-agent': 'testfile'})
    data = x.json()
    if 'error' in data:
        return 0
    try:
        return(data['data']['subscribers'])
    except KeyError:
        return 0
