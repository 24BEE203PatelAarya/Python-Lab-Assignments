#3.Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find the number of 
#  days between the two dates.

from datetime import date

date1_tuple = (18, 11, 2020)
date2_tuple = (25, 3, 2022)

date1 = date(date1_tuple[2], date1_tuple[1], date1_tuple[0])
date2 = date(date2_tuple[2], date2_tuple[1], date2_tuple[0])

difference = abs(date2 - date1)

print(f"Number of days between {date1} and {date2}: {difference.days} days")
