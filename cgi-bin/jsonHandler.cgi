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
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="../css/styles.css" rel="stylesheet" typ="style-css">
    <title>Document</title>
</head>
<body>
    <div class = "gradesTable">
        <div class="semesterCol">
                <p>Semesters</p>
                <div id="semBtnGroup">
                    <button>Winter 2018</button>
                    <button>Fall   2018</button>
                </div>
            </div>
        
            <div class="courseCol">
                <p>Courses</p>
                <div id="courseBtnGroup">
                    <button>Comp 1010</button>
                    <button>Comp 2190</button>
                    <button>Comp 3370</button>
                </div>
            </div>
        
            <div class = "categoryCol">
                <p>Categories</p>
                <div id="categoryBtnGroup">
                    <button>Assignments</button>
                    <button>Exams</button>
                    <button>Labs</button>
                    <button>Presentations</button>
                </div>
        
            </div>
        
            <div class = "subCategoryCol">
                <p>Sub Categories</p>
                <div class="subCategoryBtnGroup">
                    <button>A1</button>
                    <button>A2</button>
                    <button>A3</button>
                    <button>A4</button>
                    <button>A5</button>
                </div>
            </div>
    </div>
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
