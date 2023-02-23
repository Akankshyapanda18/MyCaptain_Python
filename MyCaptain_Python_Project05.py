# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 00:53:56 2023

@author: Khushi
"""

students = []

def add_student():
    print("Enter the student details:")
    name = input("Name: ")
    age = input("Age: ")
    grade = input("Grade: ")
    student = {"Name": name, "Age": age, "Grade": grade}
    students.append(student)
    print("Student record added successfully.")

def view_students():
    if len(students) == 0:
        print("No student records found.")
        return
    print("Student Records:")
    for student in students:
        print(f"Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}")

def search_student():
    name = input("Enter the name of the student to search: ")
    for student in students:
        if student["Name"].lower() == name.lower():
            print(f"Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}")
            return
    print(f"No student record found with the name {name}.")

def update_student():
    name = input("Enter the name of the student to update: ")
    for student in students:
        if student["Name"].lower() == name.lower():
            print(f"Current details: Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}")
            student["Name"] = input("Enter new name (leave blank to keep current name): ") or student["Name"]
            student["Age"] = input("Enter new age (leave blank to keep current age): ") or student["Age"]
            student["Grade"] = input("Enter new grade (leave blank to keep current grade): ") or student["Grade"]
            print("Student record updated successfully.")
            return
    print(f"No student record found with the name {name}.")

def delete_student():
    name = input("Enter the name of the student to delete: ")
    for student in students:
        if student["Name"].lower() == name.lower():
            students.remove(student)
            print("Student record deleted successfully.")
            return
    print(f"No student record found with the name {name}.")

while True:
    print("\nWelcome to the School Administration Program!")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Search for a student")
    print("4. Update a student record")
    print("5. Delete a student record")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you for using the School Administration Program!")
        break
    else:
        print("Invalid choice. Please enter a valid choice.")