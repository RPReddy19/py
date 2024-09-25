# Assignment-1: if condition
# Check if a person is eligible to vote based on their age

# Input: Age of the person
age = int(input("Enter your age: "))

# Check if the person is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")




# Assignment-2: if else condition
# WAP that checks whether a number is positive or negative

# Input: A number
number = int(input("Enter a number: "))

# Check whether the number is positive or negative
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"The number is zero.")


# Assignment-3: if else condition
# WAP that Checks if a given number is even or odd

# Input: A number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


# Assignment-4: nested if condition
# WAP to find the greatest of 3 numbers

# Input: Three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Find the greatest of the three numbers
if num1 >= num2:
    if num1 >= num3:
        print(f"The greatest number is {num1}.")
    else:
        print(f"The greatest number is {num3}.")
else:
    if num2 >= num3:
        print(f"The greatest number is {num2}.")
    else:
        print(f"The greatest number is {num3}.")


# Assignment-5: nested if else condition
"""

Movie Ticket Pricing
Imagine a movie theater that offers different ticket prices based on the age of the customer and the time of the day. The rules might be as follows:

Regular price: $10
Children under 12 and seniors over 65 get a 50% discount.
Matinee show (before 5 PM) offers a 25% discount to all.

# Input: Age and time of the show
age = int(input("Enter your age: "))
show_time = int(input("Enter the show time (in 24-hour format): "))

# Regular price
ticket_price = 10.00

# Apply discounts based on conditions
if age < 12 or age > 65:
    ticket_price *= 0.5  # 50% discount for children and seniors

if show_time < 17:
    ticket_price *= 0.75  # 25% discount for matinee show

# Output the final ticket price
print(f"Your ticket price is: ${ticket_price:.2f}")

"""

# Assignment-6: nested if else condition
# WAP to find the biggest country among 3 based on the population

# Input: Populations of three countries
country1 = int(input("Enter the population of Country 1: "))
country2 = int(input("Enter the population of Country 2: "))
country3 = int(input("Enter the population of Country 3: "))

# Find the biggest country by population
if country1 >= country2:
    if country1 >= country3:
        print("Country 1 has the largest population.")
    else:
        print("Country 3 has the largest population.")
else:
    if country2 >= country3:
        print("Country 2 has the largest population.")
    else:
        print("Country 3 has the largest population.")
