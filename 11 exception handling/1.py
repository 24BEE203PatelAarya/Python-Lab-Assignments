#1.Write a program that receives an integer an input. If a string is entered instead of an integer, then 
#  report an error and give another chance to user to enter an integer. Continue this process till correct 
#  input is supplied.

while True:
    user_input = input("Please enter an integer: ")
    
    try:
        number = int(user_input)
        print(f"Thank you! You entered the integer: ",number)

        break  

    except ValueError:
        print("Error! That's not a valid integer. Please try again.")
