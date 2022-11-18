var numberOfPeople = document.getElementById('addperson')
var peopleFields=document.getElementById('peopleDetails')
numberOfPeople.addEventListener('change',addFields)
function addFields() {
    peopleFields.innerHTML=""
    var number=numberOfPeople.value
    for (let index = 1; index <= number; index++) {
        // content="<hr><h5>Person "+ index+"</h5><p><b>Name</b></p><input type=\"text\" name=\"name\"><br><p><b>Age</b></p><input type=\"number\" name=\"age\"><br><p><b>Gender</b></p><select name=\"gender\" ><option value=\"M\">Male</option><option value=\"F\">Female</option><option value=\"others\">Other</option></select>"
        
    var content = '<div class="oneperson border-4 border-purple-200 p-10 m-2 rounded-md">'+
    '                        <label " class="block mb-2 text-md font-medium text-gray-900 dark:text-white">Person '+index+'</label>'+
    '                        <div class="mb-6">'+
    '                            <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Name</label>'+
    '                            <input type="text" name="name" id="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"  required>'+
    '                        </div>'+
    '                        <div class="mb-6">'+
    '                            <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Age</label>'+
    '                            <input type="number" name="age" id="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"   required>'+
    '                        </div>'+
    '                        <div class="mb-6">'+
    '                            <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Gender</label>'+
    '                            <input type="text" name="sex" id="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"  required>'+
    '                        </div>'+
    '                    </div>';
        

        peopleFields.innerHTML+=content
    }
}

