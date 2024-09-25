# Let’s write a loop that processes numbers from 1 to 10, skips multiples of 3, and stops processing if a number is greater than 7

# Loop from 1 to 10
for i in range(1, 11):
    # Stop processing if the number is greater than 7
    if i > 7:
        break
    
    # Skip multiples of 3
    if i % 3 == 0:
        continue
    
    # Process the number (print it in this case)
    print(i)
