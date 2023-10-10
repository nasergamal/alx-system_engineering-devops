#!/usr/bin/python3
'''get top ten posts in a subreddit'''
import requests


def top_ten(subreddit):
    '''request top 10 from reddit api'''
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    h = {'User-agent': 'testfile'}
    x = requests.get(url, headers=h, params={'limit': 10})
    data = x.json()
    try:
        for datum in data['data']['children']:
            print(datum['data']['title'])
    except KeyError:
        print("None")
