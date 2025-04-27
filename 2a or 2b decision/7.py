#7. Accept a year value from the user. Check whether it is a leap year or not.

year = int(input("Enter year to check if it is leap year or not: "))

if(year %4==0):
    if(year %100==0):
        if(year %400==0):
            print("It is a leap year")
        else:
                print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")

