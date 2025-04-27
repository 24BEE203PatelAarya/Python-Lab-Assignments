#2.Write a program to create a set containing 10 random numbers in the range 15 to 45. Count how 
#  many of these numbers are less than 30. Delete all numbers that are greater than 35.

import random

random_number = {random.randint(15,45) for _ in range(10)}

print(random_number)

less_than_30 = 0 
for num in random_number:
    if num<30:
        less_than_30 += 1

random_number = {num for num in random_number if num<35}
    
        
print("Numbers less than 30: ",less_than_30)
print("List of numbers less than 35: ",random_number)
