students = {
    "Ana": [8, 7, 9],
    "Luis": [6, 5, 7],
    "Sofia": [10, 9, 10]
}

students['Andres'] = students.get('Andres', [])
students['Andres'].append(10)
students['Andres'].append(9)
students['Andres'].append(9)

name = 'Ana'

if name in students:
    student_grade = students[name]
    total_grade = (student_grade[0] + student_grade[1] + student_grade[2]) / 3

    if total_grade >= 6.0:
        print(f'{name} aprobo con un promedio de: {total_grade:.2f} ')
    else:
        print(f'{name}  reprobo con un promedio de: {total_grade:.2f} ')
else:
    print('El nombre no existe')

print(students)