#2.Write a program that defines a function compute() that calculates the value of n + nn + nnn + nnnn, where n is digit received by the function.
#  test the function for digits 4 to 7.

def compute(n):
    
    str_n = str(n)
   
    result = n + int(str_n * 2) + int(str_n * 3) + int(str_n * 4)
    return result

for i in range(4, 8):
    print(f"compute({i}) = {compute(i)}")
