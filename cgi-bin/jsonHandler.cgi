#!/usr/bin/env python3
import sys
from os import environ
import json
semesterList = {}
semesterListButtons = ''
courseList = []
with open('../json/data.json') as f:
    semesterList = json.load(f)
if semesterList:
    for data in semesterList['Semester']:
        semesterListButtons += '<button id=\'' + data['id'] + '\'>' + data['name'] + '</button></br>'
        courseList.append(data['id'])

categoryListButtons = ''
subcategoryList = {}
courseListButtons = ''

# hello world
print("Content-Type: text/html\n\n")
print("""
<html>
    <header><title>Hello</title></header>
<body>
<form>
""")
print(semesterListButtons)
print(courseListButtons)

print("""
</form>
    <h2>hello world</h2>
</body>
</html>
""")
