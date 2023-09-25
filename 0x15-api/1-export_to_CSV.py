#!/usr/bin/python3
'''access user todo list and create csv file'''
import csv
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
    with open(f'{argv[1]}.csv', 'w') as f:
        content = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            s = [argv[1], d["username"], task['completed'], task['title']]
            content.writerow(s)
