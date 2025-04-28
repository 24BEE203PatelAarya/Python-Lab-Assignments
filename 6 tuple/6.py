#6.Modify an element of a tuple.

tuple1 = ("Book", 120, "Stationary")

new_list = list(tuple1)

new_list[1] = 150  

modified_tuple = tuple(new_list)

print("Modified tuple:", modified_tuple)
