#1. 1. Check if the number is prime
# A prime number has only two factors: 1 and itself 
n = int(input("Enter a number: "))
if n <= 1:
    print("1. Prime Check: Not a prime number")
else:
    prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime = False  # Found a factor, not prime
            break
    if prime:
        print("1. Prime Check: Yes, it's a prime number")
    else:
        print("1. Prime Check: No, it's not a prime number")


# 2. Find the factorial of the number
# Factorial means multiplying all numbers from 1 to n
# Factorial of a number
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial of", n, "is:", fact))


# 3. Print Fibonacci series up to n terms
# Fibonacci starts with 0 and 1, then adds previous two numbers
# Fibonacci series up to n terms
n = int(input("Enter how many terms of Fibonacci you want: "))
a = 0
b = 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


# 4. Find the sum of digits
# Example: 123 → 1 + 2 + 3 = 6
temp = n
sum_digits = 0
while temp > 0:
    digit = temp % 10       # Get last digit
    sum_digits = sum_digits + digit
    temp = temp // 10       # Remove last digit
print("4. Sum of digits of", n, "is:", sum_digits)


# 5. Reverse the digits of the number
#Example: 123 → 321
temp = n
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10
print("5. Reversed number is:", reverse)
