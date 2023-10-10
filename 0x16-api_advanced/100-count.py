#!/usr/bin/python3
'''get all posts titles in a subreddit (recursion)'''
import requests


def count_words(subreddit, word_list, word_count={}, after=""):
    '''get all post titles from reddit api'''
    if after == "":
        word_lower = [x.lower() for x in word_list]
        word_count = {x.lower(): word_lower.count(x.lower())
                      for x in word_lower}
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
            count_words(subreddit, word_list, word_count, after)
        else:
            for k, v in word_list.items():
                word_list[k] = v * word_count[k]
            s_word_list = dict(sorted(word_list.items(),
                               key=lambda x: (-x[1], x[0])))
            for k, v in s_word_list.items():
                if v == 0:
                    continue
                print(f'{k}: {v}')
