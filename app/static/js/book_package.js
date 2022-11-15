var numberOfPeople = document.getElementById('addperson')
var peopleFields=document.getElementById('peopleDetails')
numberOfPeople.addEventListener('change',addFields)
function addFields() {
    peopleFields.innerHTML=""
    var number=numberOfPeople.value
    for (let index = 1; index <= number; index++) {
        content="<hr><h5>Person "+ index+"</h5><p><b>Name</b></p><input type=\"text\" name=\"name\"><br><p><b>Age</b></p><input type=\"number\" name=\"age\"><br><p><b>Gender</b></p><select name=\"gender\" ><option value=\"M\">Male</option><option value=\"F\">Female</option><option value=\"others\">Other</option></select>"
        peopleFields.innerHTML+=content
    }
}

