#!/usr/bin/python3
'''access users todo list and create json file'''
import json
from sys import argv
import urllib.request


def get(u):
    '''get url content'''
    s = urllib.request.urlopen(u)
    return json.load(s)


if __name__ == '__main__':
    url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    d = get(url)
    url += '/todos'
    tasks = get(url)
    st = []
    for task in tasks:
        dic = {"task": task['title'], "completed": task['completed'],
               "username": d["username"]}
        st.append(dic)
    dic = {argv[1]: st}
    with open(f'{argv[1]}.json', 'w') as f:
        json.dump(dic, f)
