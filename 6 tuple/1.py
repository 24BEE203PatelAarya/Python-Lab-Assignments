#1. A list contains names of boys and girls as its elements. Boys’ names are stored as tuples. Write a 
#  program to find out number of boys and girls in the list. (Hint: use isinstance(ele,tuple))

names = [("Aarya",),"Riya",("Rahul",),"Priya",("Rohan",),"Krishna",("Ritik",)]

boy_name = 0
girl_name= 0

for name in names:
    if isinstance(name, tuple):
        boy_name += 1
    elif isinstance(name, str):
        girl_name += 1

print("The number of boys are: ",boy_name)
print("The number of girls are: ",girl_name)
