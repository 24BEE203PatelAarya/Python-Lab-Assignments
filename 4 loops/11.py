#11.Calculate sin(x); x is a radian value.

import math

x = float(input("Enter the value of x (in radians): "))

sin_x = 0
terms = 10 

for n in range(terms):
    
    power = 2 * n + 1  
    sign = (-1) ** n  
    term = sign * (x ** power) / math.factorial(power)
    
    sin_x += term
print(f"The approximate value of sin({x}) is {sin_x}")

