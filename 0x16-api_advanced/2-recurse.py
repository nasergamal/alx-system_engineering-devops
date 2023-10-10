#!/usr/bin/python3
'''get all posts titles in a subreddit (recursion)'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''get all post titles from reddit api'''
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after}
    x = requests.get(url, headers={'User-agent': 'testfile'}, params=params)
    data = x.json()
    if x.status_code == 200:
        for datum in data['data']['children']:
            hot_list.append(datum['data']['title'])
        if 'after' in data['data']:
            recurse(subreddit, hot_list, data['data']['after'])
        return hot_list
    else:
        return None
