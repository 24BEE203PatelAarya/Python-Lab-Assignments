#3.Create a dictionary with dept no, employee roll no. and salary. Find out department wise min and maximum of salary.

employee = [
    {'dept_no': 1, 'emp_roll_no': 101, 'salary': 50000},
    {'dept_no': 1, 'emp_roll_no': 102, 'salary': 60000},
    {'dept_no': 2, 'emp_roll_no': 201, 'salary': 70000},
    {'dept_no': 2, 'emp_roll_no': 202, 'salary': 80000},
    {'dept_no': 3, 'emp_roll_no': 301, 'salary': 90000},
    {'dept_no': 3, 'emp_roll_no': 302, 'salary': 100000}
]

dept_salary = {}

for emp in employee:
    dept = emp['dept_no']
    salary = emp['salary']
    if dept not in dept_salary:
        dept_salary[dept] = []
    dept_salary[dept].append(salary)

for dept, salaries in dept_salary.items():
    min_salary = min(salaries)
    max_salary = max(salaries)
    print(f"Department {dept}: Min Salary = {min_salary}, Max Salary = {max_salary}")
