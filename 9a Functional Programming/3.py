#3.Generate the list of 10 different random numbers between -15 and 15. Create a new list by obtaining square of all numbers in a list.

import random

range_start= -15
range_end = 15

random_numbers = []

while len(random_numbers) < 10:
    num = random.randint(range_start, range_end)
    if num not in random_numbers:
        random_numbers.append(num)

squared_numbers = [x ** 2 for x in random_numbers]

print("Random Numbers: ", random_numbers)
print("Squared Numbers: ", squared_numbers)

