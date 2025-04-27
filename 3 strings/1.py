#1.Count how many vowels are there in a string. Accept the string from the user.

string1 = input("Enter string to check number of vowels: ")

vowels_count = 0

vowels = 'aeiouAEIOU'

for char in string1:
    if char in vowels:
        vowels_count += 1

print("The number of vowels are: ",vowels_count)

