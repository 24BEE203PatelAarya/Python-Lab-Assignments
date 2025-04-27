#2.Write your own functions (without using built-in functions) to convert all characters of a string into lower case/upper case/toggle case.

string2 = input("Enter a string: ")
lcase = ''
for char in string2:
    if('A'<=char<='Z'):
        lcase +=chr(ord(char)+32)
    else:
        lcase += char
print("The lower case is: ",lcase)

ucase = ''
for char in string2:
    if('a'<=char<='z'):
        ucase +=chr(ord(char)-32)
    else:
        ucase += char
print("The upper case is: ",ucase)

tcase = ''

for char in string2:
    if('a'<=char<='z'):
        tcase +=chr(ord(char)-32)
    elif('A'<=char<='Z'):
        tcase += chr(ord(char)+32)
    else:
        tcase += char
        
print("The toggle case is: ",tcase)
