#!/usr/bin/env python3
import sys
from os import environ
import json
jsonData = {}
jsonDataButtons = ''
courseList = []
with open('../json/data.json') as f:
    jsonData = json.load(f)
if jsonData:
    for data in jsonData['Semester']:
        jsonDataButtons += '<button id=\'' + data['id'] + '\'>' + data['name'] + '</button></br>'

print("Content-Type: text/html\n\n")
print("""
<html>
<body>

EVERYTHING FROM PAUL HERE


""")
print(jsonDataButtons)

print("""
<script type="text/javascript">
var jsonData = JSON.parse({0});

</script>
</body>
</html>
""".format(jsonData))
