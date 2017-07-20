/* given the following array
var students = [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}

     Create a program that outputs:

Michael Jordan
John Rosales
Mark Guillen
KB Tonel
]*/

// var students = [ 
//      {first_name:  'Michael', last_name : 'Jordan'},
//      {first_name : 'John', last_name : 'Rosales'},
//      {first_name : 'Mark', last_name : 'Guillen'},
//      {first_name : 'KB', last_name : 'Tonel'}
// ];
// for (var fullname in students) {
//     console.log(students[fullname].first_name, students[fullname].last_name);
// }


var users = {
 'Students': [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }

var num = 1;
 console.log("Students"); 
for (var student_name in users.Students){
    console.log(num + " - " + users.Students[student_name].first_name, users.Students[student_name].last_name + " - " + (users.Students[student_name].first_name + users.Students[student_name].last_name).length);
    num++;
}

var number = 1;
console.log("Instructors");
for(var instructors_name in users.Instructors){
    console.log(number + " - " + users.Instructors[instructors_name].first_name, users.Instructors[instructors_name].last_name + " - " + (users.Instructors[instructors_name].first_name +  users.Instructors[instructors_name].last_name).length);
    number++;
}