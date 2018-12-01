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

</br>
</br>

<div id=semBtnGroup></div>

</br>
</br>

""")
print("""
<script type="text/javascript">
var jsonData = {0};
""".format(jsonData))
print("""
onloadEvent();
function onloadEvent() {
    if(!(jsonData)) {
        return;
    }
    var semester = document.getElementById('semBtnGroup');
    semester.innerHTML = '';
    for( var i = 0; i < jsonData['Semester'].length; i++) {

        var btn = document.createElement("button");
        btn.innerHTML = jsonData['Semester'][i]['name'];
        semester.appendChild(btn);

    }



    var course = document.getElementById('courseBtnGroup');
    var category = document.getElementById('categoryBtnGroup');
    var subcategory = document.getElementById('subCategoryBtnGroup');

}

</script>
</body>
</html>
""")
