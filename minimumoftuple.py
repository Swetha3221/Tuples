'''
'''
Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
'''
'''
Ans:
# Input: number of values to be entered
n = int(input())

# Initialize an empty list to store the values
values = []

# Loop to get n values from the user
for _ in range(n):
    value = int(input())  # Get each value
    values.append(value)  # Add the value to the list

# Create a tuple from the list of values
values_tuple = tuple(values)

# Initialize min_value with the first element of the tuple
min_value = values_tuple[0]

# Loop through the tuple to find the actual minimum value
for number in values_tuple:
    if number < min_value:
        min_value = number  # Update min_value if a smaller number is found

# Print the minimum value
print(min_value)

'''
'''
