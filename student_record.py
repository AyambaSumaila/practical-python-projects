student_record={}
name=input('Enter name:')
student_record.get(name)
age=int(input('Enter age:'))
student_record.get(age)

marks=int(input('Enter marks:'))
student_record.get(marks)

for i in name:
    for j in age:
        for k in marks:
            
            print(student_record(i, j, k))