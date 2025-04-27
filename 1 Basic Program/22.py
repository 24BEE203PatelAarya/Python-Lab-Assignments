#22.Calculate net sales where net sales = gross sales – 10% discount of gross sales.

gross_sales = int(input("Enter gross sales: "))  
discount_percentage = 10 

discount_amount = (discount_percentage / 100) * gross_sales

net_sales = gross_sales - discount_amount

print(f"Gross Sales: ₹{gross_sales}")
print(f"Discount ({discount_percentage}%): ₹{discount_amount}")
print(f"Net Sales: ₹{net_sales}")
