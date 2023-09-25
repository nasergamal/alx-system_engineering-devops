#!/usr/bin/python3
'''api test'''
import urllib.request
from sys import argv
import json


def get(u):
    '''get url content'''
    s = urllib.request.urlopen(u)
    return json.load(s)


url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
d = get(url)
url += '/todos'
tasks = get(url)
cm = 0
cm_tasks = []

for task in tasks:
    if task['completed'] is True:
        cm += 1
        cm_tasks.append(task['title'])

print(f'Employee {d["name"]} is done with tasks({cm}/{len(tasks)})')
[print(c) for c in cm_tasks]
