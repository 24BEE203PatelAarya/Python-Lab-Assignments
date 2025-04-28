#4.Generate 30 random numbers and put them in a list. Create two more lists – one containing only +ve numbers and another with –ve nos.

import random

random_numbers = []

for _ in range(30):
    random_numbers.append(random.randint(-15, 15))

positive_numbers = []
negative_numbers = []

for num in random_numbers:
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)

print("Random Numbers:", random_numbers)
print("Positive Numbers:", positive_numbers)
print("Negative Numbers:", negative_numbers)
