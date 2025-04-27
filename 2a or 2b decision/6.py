#6.Accept a number from the user. And print number of digits in it.

num = int(input("Enter a number to count digits: "))

if(num<10):
    print("It has one digits")
elif(num<100):
    print("It has two digits")
elif(num<1000):
    print("It has three digits")
else:
    print("It has 4 or more than 4 digit")
