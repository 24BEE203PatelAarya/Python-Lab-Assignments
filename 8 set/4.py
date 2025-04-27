#4.A set contains names which begin either with A or with B. Write a program to separate out the 
#  names into two sets, one containing names beginning with A and another with B.

names = {'Aarya','Bob','Aarav','Babil','Akshar','Ben','Aagam'}
print(names)

a_name = set()
b_name = set()

for name in names:
    if name[0] == 'A':
        a_name.add(name)
    else:
        b_name.add(name)

print("Names starting with A: ",a_name)
print("Names starting with B: ",b_name)
