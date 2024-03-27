class Student:
    def __init__(self, name, roll_number, marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
        
        
        
student=Student("Sumaila", "PS/ITC/20/0001", 89)

print(f"The  student name is {student.name}  ID is {student.roll_number} and marks {student.marks}")