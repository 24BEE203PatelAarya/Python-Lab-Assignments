#5.A list contains names of Faculty Members. Write a program to filter out those names whose length is more than 8 characters.

faculty_name = ['Dr. Jitendra Jamamnani', 'Dr. Chintan Bhatt', 'Dr. Alok', 'Dr. Aarya Patel','Dr. Uday']

new_name = [name for name in faculty_name if len(name) > 8]

print("Faculty members with names longer than 8 characters: ",new_name)


