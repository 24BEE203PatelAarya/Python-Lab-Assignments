#3.Count no. of alphabets and no. of digits in any given string.

input_string = input("Enter a string: ")

alphabet_count = 0
digit_count = 0

for char in input_string:
    if ('a' <= char <= 'z' or 'A' <= char <= 'Z'):  
        alphabet_count += 1
    elif ('0' <= char <= '9'):  
        digit_count += 1

print("Number of alphabets:", alphabet_count)
print("Number of digits:", digit_count)
