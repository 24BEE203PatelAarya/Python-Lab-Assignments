#3.Create an empty set. Write a program that adds five new names to this set, modifies one existing 
#  name and deletes two names from it.

set1 = set()
print("Empty set: ",set1)

set1.add("Aarya")
set1.add("Rahul")
set1.add("Rohan")
set1.add("Anshu")
set1.add("Riya")
set1.add("Priya")

print("Adding names: ",set1)

set1.remove("Rohan")
set1.add("Bob")
print("Modifing set: ",set1)

set1.remove('Riya')
set1.remove('Anshu')
print('Deleting name: ',set1)
