#4.Write a program that reads a string from the keyboard and creates dictionary containing frequency of each character occurring in the string.

input_string = input("Enter a string: ")

frequency = {}

for char in input_string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequencies: ")
for char, freq in frequency.items():
    print(f"'{char}': {freq}")
