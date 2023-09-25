#!/usr/bin/python3
'''api test'''
import urllib.request
from sys import argv
import json
import csv


def get(u):
    '''get url content'''
    s = urllib.request.urlopen(u)
    return json.load(s)


url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
d = get(url)
url += '/todos'
tasks = get(url)
with open(f'{argv[1]}.csv', 'w') as f:
    content = csv.writer(f, quoting=csv.QUOTE_ALL)
    for task in tasks:
        s = [argv[1], d["name"], task['completed'], task['title']]
        content.writerow(s)
