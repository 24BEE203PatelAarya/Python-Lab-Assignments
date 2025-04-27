#7.Print nCr and nPr.

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

nCr = 1
for i in range(1, r + 1):
    nCr *= (n - r + i) // i

nPr = 1
for i in range(n, n - r, -1):
    nPr *= i
    
print(f"{n}C{r} = {nCr}")
print(f"{n}P{r} = {nPr}")
