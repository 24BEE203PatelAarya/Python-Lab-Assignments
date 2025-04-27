#4.Check whether a given number is prime, is perfect, is Armstrong, is palindrome, is automorphic.

num = int(input("Enter a number: "))

# Check if the number is prime
if num <= 1:
    prime = False
else:
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

# Check if the number is perfect
sum_of_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i
perfect = (sum_of_divisors == num)

# Check if the number is Armstrong
num_str = str(num)
num_digits = len(num_str)
sum_of_powers = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10
armstrong = (sum_of_powers == num)

# Check if the number is palindrome
temp = num
reversed_num = 0
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
palindrome = (reversed_num == num)

# Check if the number is automorphic
square = num * num
num_digits = len(str(num))
last_digits = square % (10 ** num_digits)
automorphic = (last_digits == num)

print(f"Is {num} prime? {'Yes' if prime else 'No'}")
print(f"Is {num} perfect? {'Yes' if perfect else 'No'}")
print(f"Is {num} Armstrong? {'Yes' if armstrong else 'No'}")
print(f"Is {num} palindrome? {'Yes' if palindrome else 'No'}")
print(f"Is {num} automorphic? {'Yes' if automorphic else 'No'}")
