# a student database the whole program based on 
students = [
    {'name': 'fares', 'age': '19', 'grade': '12', 'favourite color': 'black'},
    {'name': 'abi', 'age': '20', 'grade': '12', 'favourite color': None}
]

        
#a functinon to add a new student from user info    
def new_adds():
    name = input('Name:')
    age = int(input('Age:'))
    grade = int(input('Grade:'))
    favcolor = str(input('Favourite Color:'))
    add_student = {'name': name, 'age': age, 'grade': grade, 'favourite color': favcolor}
    students.append(add_student)
    print('successfully adde a student')
    print(students)

 
# to show specific a student by using values

def view_student(key, value):
    for student in students:
        if student['name'] == value:
            return student
    return None

value = input('search by name:')  
found_student = view_student('name', value)

if found_student:
    print('Student:', found_student)
else:
    print('student not found')


#delete a specific student

def find_student_index(key, value):
    for i, student in enumerate(students):
        if student['name'] == value:
            return i
    return None

value = input('Enter a Name: ')

student_index = find_student_index("name", value)
if student_index is not None:
    del students[student_index]
    print('student removed')
    print(students)
else:
    print('student not found')


#update a specific student database

def student_database(key, value):
    for student in students:
        if student['name'] == value:
            return student
        return None
    
value = input('Enter a Name: ')

foundd_student = student_database('name', value)

if foundd_student:
    new_age = int(input('Enter new age:'))
    new_grade = input('new grade: ')
    new_favcolor = input('new favourite color: ')
    foundd_student['age'] = new_age
    foundd_student['grade'] = new_grade
    foundd_student['favourite color'] = new_favcolor
    print('student info updated')
    print(students)
else:
    print('student not found')

#a function that will take values and display another function

def cwords():
    ckeys = int(input('Add(1), view(2), list(3), update(4), delete(5)'))
    if ckeys == 1:
        new_adds()
    elif ckeys == 2:
        view_student('name', value)
    elif ckeys == 3:
        print(students)
    elif ckeys == 4:
        student_database(key, value)
    elif ckeys == 5:
        find_student_index('name', value)
        


def main():
    print('welcome')
    cwords()


main()










    

    










