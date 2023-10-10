#!/usr/bin/python3
'''get all posts titles in a subreddit (recursion)'''
import requests


def count_words(subreddit, word_list, after=""):
    '''get all post titles from reddit api'''
    if after == "":
        word_list = {x.lower(): 0 for x in word_list}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after}
    x = requests.get(url, headers={'User-agent': 'testfile'}, params=params)
    if x.status_code == 200:
        data = x.json()
        for datum in data['data']['children']:
            title = datum['data']['title'].lower().split()
            for key in word_list:
                word_list[key] += title.count(key)
        after = data['data']['after']
        if after:
            count_words(subreddit, word_list, data['data']['after'])
        else:
            for k, v in word_list.items():
                print(f'{k}: {v}')
