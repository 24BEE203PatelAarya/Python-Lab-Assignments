#4.Write a function that removes one string from another string, if present.

original_string = input("Enter string: ")
removing_string = input("Enter string to remove: ")
modified_string = original_string.replace(removing_string, "")

print("The new string is: ",modified_string)

