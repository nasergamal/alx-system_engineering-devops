#!/usr/bin/python3
'''get all users tasks'''
import json
import urllib.request


def get(u):
    '''get url content'''
    s = urllib.request.urlopen(u)
    return json.load(s)


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users/"
    users = get(url)
    complete_dic = {}
    for user in users:
        ur = url + f'{user["id"]}/todos'
        tasks = get(ur)
        st = []
        for task in tasks:
            dic = {"username": user["username"], "task": task['title'],
                   "completed": task['completed']}
            st.append(dic)
        complete_dic[user["id"]] = st
    with open('todo_all_employees.json', 'w') as f:
        json.dump(complete_dic, f)
