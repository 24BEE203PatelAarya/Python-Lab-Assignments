#1.Write a program that converts words present in a list into uppercase and stores them in a set.
words = ['aarya','rohan','rahul']

uppercase = {word.upper() for word in words}

print(uppercase)
