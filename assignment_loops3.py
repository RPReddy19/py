"""
Floyd's triangle pattern
The Floyd's triangle is a right-angled triangle that contains
consecutive natural numbers, starting with a 1 in the top left corner.
"""
"""
1
2 3
4 5 6
7 8 9 10
"""

# Input: Number of rows for Floyd's triangle
rows = int(input("Enter the number of rows for Floyd's triangle: "))

# Initialize a number to start the sequence
num = 1

# Generate Floyd's triangle
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()  # Move to the next line after each row


# Checkerboard Pattern
"""
The pattern typically contains two colours where a single checker
(that is a single square within the check pattern) is surrounded
on all four sides by a checker of a different colour.
"""
"""
B W B W
W B W B
B W B W
W B W B
"""
# Input: Size of the checkerboard
n = int(input("Enter the size of the checkerboard: "))

# Generate checkerboard pattern
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("B", end=" ")  # "B" for black
        else:
            print("W", end=" ")  # "W" for white
    print()  # Move to the next line after each row



# Hollow Square star pattern
"""
* * * *
*     *
*     *
* * * *
"""


# Input: Size of the square (number of rows and columns)
n = int(input("Enter the size of the hollow square pattern: "))

# Generate hollow square star pattern
for i in range(n):
    for j in range(n):
        # Print stars at the borders
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Hollow space in the middle
    print()  # Move to the next line after each row

# Diamond Pattern
"""
    *
   ***
  *****
 *******
  *****
   ***
    *
"""

# Input: Number of rows for the diamond (half the height)
n = int(input("Enter the number of rows for the diamond pattern: "))

# Generate the top half of the diamond
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Generate the bottom half of the diamond
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
