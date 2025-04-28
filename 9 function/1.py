#1.Write a program that defines a function count_lower_upper() that accepts a string and calculates the number of uppercase and lowercase alphabets in it.
#  It should return these values as a dictionary.
#  Call this function for some sample string.

def count_lower_upper(s):
    counts = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for char in s:
        if char.isupper():
            counts["UPPER_CASE"] += 1
        elif char.islower():
            counts["LOWER_CASE"] += 1
    return counts

sample_string = "Hello World?"


result = count_lower_upper(sample_string)
print(result)
