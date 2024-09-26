# Find all prime numbers between 2 and n
"""
The standard definition of prime numbers applies only to
positive integers greater than 1. A prime number is defined
as a number that has only two distinct positive divisors: 1 and itself.
For example, 2, 3, 5, 7, 11, etc. are prime numbers
because they can only be divided evenly by 1 and themselves
without leaving a remainder.
"""

# Input: Upper limit 'n' for prime numbers
n = int(input("Enter the upper limit to find all prime numbers: "))

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Find and display all prime numbers between 2 and n
prime_numbers = [i for i in range(2, n + 1) if is_prime(i)]
print(f"Prime numbers between 2 and {n} are: {prime_numbers}")


# Print multiplication tables from 1 to n
"""
Let's say if user inputs 9, you need to generate 1 to 9 tables
"""

# Input: Upper limit 'n' for multiplication tables
n = int(input("Enter the number up to which you want multiplication tables: "))

# Generate and display multiplication tables from 1 to n
for i in range(1, n + 1):
    print(f"\nMultiplication table for {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
