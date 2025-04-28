#2. A list contains tuples containing roll no., name and age of student. Write a python program to create 
#  three lists separately for roll no., name and age.

students= [(100,"Aarya",19),(101,"Rahul",17),(102,"Rohan",18)]

roll_no = []
names = []
ages = []

for student in students:
    rollno, name, age = student
    roll_no.append(rollno)
    names.append(name)
    ages.append(age)

print('Roll Number: ',roll_no)
print('Names: ',names)
print('Age: ',ages)
