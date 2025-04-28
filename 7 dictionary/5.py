
#5.Create two dictionaries – one containing grocery items and their prices and another containing grocery items and quantity purchased.
#  By using the values from these two dictionaries compute the total bill.

prices = {
    "apple": 100,
    "banana": 30,
    "orange": 50,
    "milk": 36,
    "bread": 65
}

quantities = {
    "apple": 4,
    "banana": 6,
    "orange": 3,
    "milk": 2,
    "bread": 1
}

total_bill = 0

for item in prices:
    total_bill += prices[item] * quantities.get(item, 0)

print("Total Bill(in rupees):", total_bill)
