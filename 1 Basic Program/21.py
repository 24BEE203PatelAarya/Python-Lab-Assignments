#21.Calculate net salary  where net salary = gross salary + allowance – deduction. 
#   Allowances are 10% while deductions are 3% of gross salary.

gross_salary = int(input("Enter your salary: "))

allowance_percentage = 10  
deduction_percentage = 3   

allowance = (allowance_percentage / 100) * gross_salary
deduction = (deduction_percentage / 100) * gross_salary

net_salary = gross_salary + allowance - deduction

print(f"Gross Salary: ₹{gross_salary}")
print(f"Allowance (10%): ₹{allowance}")
print(f"Deduction (3%): ₹{deduction}")
print(f"Net Salary: ₹{net_salary}")
