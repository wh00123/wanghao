'''
# Nested loop to print the multiplication table
for i in range(1, 10):
    for j in range(1, 10):
        # Multiply i and j and print with appropriate spacing
        print(f"{i} x {j} = {i*j:2d}", end="  ")
    # Move to the next line for the next row
    print()
'''

# Nested loop to print the multiplication table in an equilateral triangle shape
for i in range(1, 10):
    # Print spaces to center the triangle
    print(" "*(10-i), end="")
    for j in range(1, i+1):
        # Multiply i and j and print with appropriate spacing
        print(f"{i} x {j} = {i*j:2d}", end="  ")
    # Move to the next line for the next row
    print()
