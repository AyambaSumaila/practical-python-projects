""""
Problem Statement:

You need to develop a program that manages employee data using the Employee class. 
The program should have two main functionalities: displaying employee data and performing employee management operations.

Employee Class:
Implement a class called Employee that represents an employee. 
The Employee class should have the following attributes: name, ID number, department, and job title.

Employee Data Display:
Write a program that creates three instances of the Employee class to store the following data:
Employee 1:

Name: Susan Meyers
ID Number: 47899
Department: Accounting
Job Title: Vice President
Employee 2:

Name: Mark Jones
ID Number: 39119
Department: IT
Job Title: Programmer
Employee 3:

Name: Joy Rogers
ID Number: 81774
Department: Manufacturing
Job Title: Engineer
The program should create three Employee objects and display the data for each employee on the screen.

Employee Management System:
Enhance the program to include an employee management system using a dictionary.
 The dictionary should use the employee ID number as the key.
The program should present a menu to the user with the following options:

Look up an employee in the dictionary
Add a new employee to the dictionary
Change the details (name, department, job title) of an existing employee in the dictionary
Delete an employee from the dictionary
Quit the program
When the program terminates, it should serialize (pickle) the dictionary and save it to a file.
 When the program starts, it should attempt to load the serialized dictionary from the file
. If the file does not exist, the program should start with an empty dictionary.
"""

import pickle
import os
import re

class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

def save_employees(employees):
    with open('employees.pkl', 'wb') as file:
        pickle.dump(employees, file)

def load_employees():
    if os.path.exists('employees.pkl'):
        with open('employees.pkl', 'rb') as file:
            return pickle.load(file)
    else:
        return {}

def lookup_employee(employees):
    id_number = input("Enter the ID number of the employee: ")
    if id_number in employees:
        employee = employees[id_number]
        print("Employee found:")
        print("Name:", employee.name)
        print("ID Number:", employee.id_number)
        print("Department:", employee.department)
        print("Job Title:", employee.job_title)
    else:
        print("Employee not found.")

def add_employee(employees):
    name = input("Enter the name of the employee: ")
    while not re.match(r"^(?![0-9]$)(?!\s$).{2,}$", name):
        print("Invalid name. Please enter a name that is not a number, a single character, or whitespace.")
        name = input("Enter the name of the employee: ")
    
    id_number = input("Enter the ID number of the employee: ")
    while not re.match(r"^(?![a-zA-Z\s]$).+$", id_number):
        print("Invalid ID number. Please enter an ID number that is not only strings, characters, or whitespace.")
        id_number = input("Enter the ID number of the employee: ")
    
    department = input("Enter the department of the employee: ")
    while not re.match(r"^(?![0-9]$)(?!\s$).{2,}$", department):
        print("Invalid department. Please enter a department that is not a number, a single character, or whitespace.")
        department = input("Enter the department of the employee: ")
    
    job_title = input("Enter the job title of the employee: ")
    employee = Employee(name, id_number, department, job_title)
    employees[id_number] = employee
    print("Employee added successfully.")

def update_employee(employees):
    id_number = input("Enter the ID number of the employee to update: ")
    if id_number in employees:
        employee = employees[id_number]
        print("Employee found. Enter new details:")
        
        name = input("Enter the new name: ")
        while not re.match(r"^(?![0-9]$)(?!\s$).{2,}$", name):
            print("Invalid name. Please enter a name that is not a number, a single character, or whitespace.")
            name = input("Enter the new name: ")
        
        department = input("Enter the new department: ")
        while not re.match(r"^(?![0-9]$)(?!\s$).{2,}$", department):
            print("Invalid department. Please enter a department that is not a number, a single character, or whitespace.")
            department = input("Enter the new department: ")
        
        job_title = input("Enter the new job title: ")
        employee.name = name
        employee.department = department
        employee.job_title = job_title
        print("Employee details updated successfully.")
    else:
        print("Employee not found.")

def delete_employee(employees):
    id_number = input("Enter the ID number of the employee to delete: ")
    if id_number in employees:
        del employees[id_number]
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")

def display_employees(employees):
    print("\nAll Employees:")
    if employees:
        for id_number, employee in employees.items():
            print("ID Number:", id_number)
            print("Name:", employee.name)
            print("Department:", employee.department)
            print("Job Title:", employee.job_title)
            print()
    else:
        print("No employees found.")

def display_menu():
    print("\nEmployee Management System Menu:")
    print("1. Look up an employee")
    print("2. Add a new employee")
    print("3. Update an employee's details")
    print("4. Delete an employee")
    print("5. Display all employees")
    print("6. Quit")

# Load employees from the file
employees = load_employees()

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        lookup_employee(employees)
    elif choice == '2':
        add_employee(employees)
    elif choice == '3':
        update_employee(employees)
    elif choice == '4':
        delete_employee(employees)
    elif choice == '5':
        display_employees(employees)
    elif choice == '6':
        save_employees(employees)
        print("Employee data saved. Quitting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
