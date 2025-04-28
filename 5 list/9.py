#9.Take two lists of numbers. Create third list of numbers for only those numbers from first list which are not there in 2nd list (use list comprehension).

lst1 = [1,2,3,4,5,6,7,8]
lst2 = [3,5,8,9,0]

lst3 = [item for item in lst1 if item not in lst2]

print(lst3)
 
