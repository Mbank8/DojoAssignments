students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }



def studentList(arr):
    for student in students:
        print student["first_name"], student["last_name"]

def userList(users):
    for role in users:
        counter = 0
        print role
        for person in users[role]:
            counter += 1
            first = person["first_name"].upper()
            last = person["last_name"].upper()
            length = len(first) + len(last)
            print counter,"-", first, last,"-", length
studentList(students)
userList(users)

