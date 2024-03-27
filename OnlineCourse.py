
class OnlineCourse:
    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor
        self.students = []
    
    def entroll_students(self, student):
        self.students.append(student)
        print(f"{student.name} has been entrolled in the {self.course} course")
        
    
    def course_details(self):
        print(f"CourseL {self.course}")
        print(f"Intructor Name: {self.instructor}")
        print(f"Entrolled Students")
        
        for student in self.students:
            print(student.name)
        
        
        
    def completed_course(self, name):
        for student in self.student:
            if student.name in name:
                self.students.remove(student)
                print(f"{name} has completed the course!")
        
        print(f"{name} is not entrolled in this course ")
                
                
    def avg_grade(self, grades):
        total=sum(student.grades)
        average=total / len(student.grades)
        
        print(f"The average grade is: {average}")
        
        
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
            
course_input=input("Enter a course :").lower()
name=input("Enter a Instructor: ").lower()
student=input("Enter a name:").lower()

course=OnlineCourse(course_input, name)

grades=[83, 57, 87, 90]

course.avg_grade(grades)
course.entroll_students(student)
course.course_details()



num_students=int(input("Enter number of students:"))

for _ in range(num_students):
    student_name=input("Enter name of student:").lowe()
    grades=[]
    for _ in range(3):
        grade=int(input("Enter student grade :"))
        grades.append(grade)
        
    student=Student(student_name,grades)
    
    
    course.entroll_students(student)

    course.avg_grade(student)
    
course.course_details()


    
    