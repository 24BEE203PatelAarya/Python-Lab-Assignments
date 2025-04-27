#23.Calculate average of three subjects along with their total.

maths = float(input("Enter marks for maths: "))
python = float(input("Enter marks for python: "))
eee = float(input("Enter marks for EEE: "))

total_marks = maths+python+eee

average_marks = total_marks / 3

print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
