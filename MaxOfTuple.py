'''
'''
Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
'''
'''
Ans:
# Input: number of values to be entered
n = int(input("Enter the number of values: "))

# Initialize an empty list to store the values
values = []

# Loop to get n values from the user
for _ in range(n):
    value = int(input())  # Get each value
    values.append(value)  # Add the value to the list

# Create a tuple from the list of values
values_tuple = tuple(values)

# Initialize max_value with the first element of the tuple
max_value = values_tuple[0]

# Loop through the tuple to find the actual maximum value
for number in values_tuple:
    if number > max_value:
        max_value = number  # Update max_value if a larger number is found

# Print the maximum value
print(max_value)
'''
'''
