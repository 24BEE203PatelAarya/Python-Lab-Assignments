#2.Read the data stored in MS-Excel file and convert it into a dictionary. The record contains rollno, name of student, marks of three subjects. Also calculate total.
#  Display the dictionary data on the monitor.

import csv

file_name = 'students_data.csv'

students_data = []

with open(file_name, mode='r') as file:
    csv_reader = csv.reader(file)
    
    next(csv_reader)
    
    for row in csv_reader:
       
        rollno = row[0]
        name = row[1]
        subject1 = int(row[2]) 
        subject2 = int(row[3])
        subject3 = int(row[4])
        
        total = subject1 + subject2 + subject3
        
        student_dict = {
            'RollNo': rollno,
            'Name': name,
            'Subject1': subject1,
            'Subject2': subject2,
            'Subject3': subject3,
            'Total': total
        }
        
        students_data.append(student_dict)

for student in students_data:
    print(student)
