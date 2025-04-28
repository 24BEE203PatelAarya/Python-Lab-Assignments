#1.Write a program to create three dictionaries and concatenate them to create fourth dictionary.

dict1 = {'aarya': 1, 'rahul': 2}
dict2 = {'rohan': 3, 'riya': 4}
dict3 = {'priya': 5}

dict4 = {}

dict4.update(dict1)
dict4.update(dict2)
dict4.update(dict3)
        
print("Concatenated dictionary:", dict4)
