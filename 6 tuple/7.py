#7.Delete an element of a tuple.

tuple2 = ("Book", 120, "Fast food", 150)
new2_list = list(tuple2)

removed_item = new2_list.pop(1)

modified_tuple = tuple(new2_list)

print("Modified tuple:", modified_tuple)
print("Removed item:", removed_item)

