#14.Accept marks of three subjects. Print total and average along with whether a candidate has 
#  passed or fail. If student secures <= 39 marks in any subject, consider him as fail. Also assigned a 
#  subject wise grade based on the following table:.

sub1 = int(input("Enter marks of python: "))
sub2 = int(input("Enter marks of maths: "))
sub3 = int(input("Enter marks of Electrical & Electronics: "))

total_marks= sub1 + sub2 + sub3
avg_marks = total_marks/3

if 80<=avg_marks<=100:
    print("O Grade")
elif 70<=avg_marks<=79:
        print("A+ Grade")
elif 60<=avg_marks<=69:
        print("A Grade")
elif 55<=avg_marks<=59:
        print("B+ Grade")
elif 50<=avg_marks<=54:
        print("B Grade")
elif 45<=avg_marks<=49:
        print("C Grade")
elif 40<=avg_marks<=44:
        print("P Grade")
elif 0<=avg_marks<=39:
        print("F Grade")
