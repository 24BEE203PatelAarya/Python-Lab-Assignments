#4.Consider the following list:
#  lst = ['madam','Python',"malayalam",12321]
#  Write a program to print those strings which are palindromes.

def is_palindrome(item):
    item_str = str(item)
    return item_str == item_str[::-1]

lst = ['madam', 'Python', 'malayalam', 12321]
palindrome = [item for item in lst if is_palindrome(item)]

print(palindrome)

