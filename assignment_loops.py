"""
Count Occurrences: Given a list and a target element,
count the occurrences of the target in the list.
"""
numbers = [1, 2, 3, 4, 5, 2, 2, 6, 7,2,5]
target = int(input("Enter the number to find the number of occurrence "))

# List of numbers
numbers = [1, 2, 3, 4, 5, 2, 2, 6, 7, 2, 5]

# Input: Target element
target = int(input("Enter the number to find the number of occurrences: "))

# Count the occurrences of the target in the list
count = numbers.count(target)

# Output the result
print(f"The number {target} occurs {count} times in the list.")



# Count and display vowels in a string
s1 = input("Enter the string to find the vowels in a string ")

# Input: A string from the user
s1 = input("Enter the string to find the vowels in the string: ").lower()

# Initialize a counter and a set of vowels
vowels = "aeiou"
vowel_count = 0

# Find and count the vowels in the string
for char in s1:
    if char in vowels:
        vowel_count += 1

# Output the result
print(f"There are {vowel_count} vowels in the string.")


# Calculate the factorial of a number
n = int(input("Enter the number to calculate the factorial "))

# Input: A number from the user
n = int(input("Enter the number to calculate the factorial: "))

# Function to calculate factorial
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Output the result
print(f"The factorial of {n} is {factorial(n)}.")


"""
A palindrome number is a number that remains the same when its digits are reversed.
For example, 121, 1331, 16461 are palindrome numbers, while 123 and 321 are not.
"""

# Input: A number from the user
n = int(input("Enter a number to check if it's a palindrome: "))

# Convert the number to a string and check if it's the same when reversed
if str(n) == str(n)[::-1]:
    print(f"{n} is a palindrome number.")
else:
    print(f"{n} is not a palindrome number.")


# WAP to unlock the mobile device using a pattern
"""
User enters a correct password in 5 attempts, phone will be unlocked.
If a user enters an incorrect password for 5 attempts,
You have to wait for 30 seconds to try again.
This process repeats
"""
import time

# Set the correct password
correct_password = "1234"

# Allow 5 attempts for the user to enter the correct password
attempts = 5

while True:
    for i in range(attempts):
        password = input("Enter the password to unlock the phone: ")
        
        if password == correct_password:
            print("Phone unlocked successfully!")
            break
        else:
            print(f"Incorrect password. You have {attempts - (i + 1)} attempts left.")
    
    # If user fails all 5 attempts, wait for 30 seconds
    if password != correct_password:
        print("Too many incorrect attempts! Please wait 30 seconds to try again.")
        time.sleep(30)
    else:
        break
