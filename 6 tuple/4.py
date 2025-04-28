#4.Create a list of tuples containing a food item and its price. Sort the tuples in descending order by 
#  price.

food_items = [
    ("Burger", 110),
    ("Sandwich", 140),
    ("Pizza", 200),
    ("Ice Cream", 90),
    ("Salad", 150)
]
def get_price(item):
    return item[1]

sorted_food_items = sorted(food_items, key=get_price, reverse=True)

for item, price in sorted_food_items:
    print(f"{item}: ₹{price}")


