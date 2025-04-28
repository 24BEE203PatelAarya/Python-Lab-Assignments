#3.Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list.

import random

random_numbers = [random.randint(1, 30) for _ in range(50)]

unique_numbers = list(set(random_numbers))

print("Unique random numbers:", unique_numbers)
    
