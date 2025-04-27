#5.Generate all Pythagorean Triplets with side length <= 30.

limit = 30

for a in range(1, limit + 1):
   
    for b in range(a, limit + 1):
        
        for c in range(b, limit + 1):
           
            if a * a + b * b == c * c:
                print(f"{a} {b} {c} ['A^2+B^2=C^2']")

