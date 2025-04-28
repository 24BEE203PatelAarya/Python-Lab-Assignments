#1.Create a list of 5 odd integers using random nos. Similarly create a list of 4 even integers using random nos.
#   Replace the third element of odd integers with  a list of 4 even integers. Flattern, sort and print the list.
#   Provide appropriate message at each stage.

odd_integers = [1,3,5,7,9]
print('Odd integers are: ',odd_integers)

even_integers = [2,4,6,8]
print('Even integers are: ',even_integers)

odd_integers[2] = even_integers
print(odd_integers)

flattend_list=[]
for item in odd_integers:
    if isinstance(item, list):
        flattend_list.extend(item)  
    else:
        flattend_list.append(item)  
print("Flattend list:", flattend_list)

flattend_list.sort()
print('Sorted Flattend list: ',flattend_list)
