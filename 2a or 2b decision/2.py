#2.Print the largest value out of three

a1 = int(input("Enter A: "))
b1 = int(input("Enter B: "))
c1 = int(input("Enter C: "))      

if(a1>b1 and a1>c1):
    print("A is biggest among them and A is: ",a1)
elif(b1>a1 and b1>c1):
        print("B is biggest among them and B is: ",b1)
else:
            print("C is biggest among them and C is: ",c1)
            
