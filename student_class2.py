class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        
        
        
    def result(self):
        
        if self.marks >= 400:
            return 'Passed!'
        
        else:
            return 'Failed'
        
        
stud=Student('Paul', 790)

stud=Student('Pious', 71)
stud2=Student('Osman', 162)
stud3=Student('Talata', 899)
stud4=Student('Yussif', 1000)


student_objects=[stud, stud2, stud3, stud4]

passStudList=[]

failStudList=[]

students_result_list={}

for x in student_objects:
    if x.result() == 'Passed!':
        passStudList.append(x.name)
        students_result_list['Pass Students']=passStudList
        
    else:
        failStudList.append(x.name)
        students_result_list['Failed Students']=failStudList
        
        
        
a=students_result_list

print(a)
