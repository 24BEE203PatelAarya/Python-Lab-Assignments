#1.Write a program to create a csv file that we can directly open in MS-Excel.
import csv

header = ['RollNo', 'Name', 'Subject1', 'Subject2', 'Subject3']  
students = [
    [101, 'Aarya', 85, 90, 88],
    [102, 'Rohan', 78, 82, 80],
    [103, 'Rahul', 92, 91, 94],
    [104, 'Priya', 75, 80, 72]
]

file_name = 'students_data.csv'

with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(header)
    
    writer.writerows(students)

print(f"CSV file '{file_name}' created successfully.")

