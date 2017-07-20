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

var students = [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
];
for (var fullname in students) {
    console.log(students[fullname].first_name, students[fullname].last_name);
}