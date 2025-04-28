#2.Generate 20 random integers and store them in a list.Accept a number from the user and print position of all occurrences of that number in the list.

import random

list1 = [random.randint(1,50) for _ in range(20)]
print('Random integers: ',list1)         

number = int(input('Enter a number to find its index: '))

positions = []
for index, num in enumerate(list1):
    if num == number:
        positions.append(index)

if positions:
    print(f"The number {number} is found at the following positions: {positions}")
else:
    print(f"The number {number} is not found in the list.")
