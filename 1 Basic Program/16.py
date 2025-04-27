#16. Calculate interest where I = PRN/100

p = int(input("Enter principal to calculate interrst: "))
r = int(input("Enter Rate to calculate interrst: "))
n = int(input("Enter num. of years to calculate interrst: "))

i = p*r*n/100
print("The interset is: ",i)
