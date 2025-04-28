
#5. Remove empty tuple(s) from the list of tuples.

my_list = [(), ('a', 'b'), (), ('c',),('d', 'e')]

filtered_list = []

for item in my_list:
    
    if item:
        
        filtered_list.append(item)

print("List after removing empty tuples:", filtered_list)
