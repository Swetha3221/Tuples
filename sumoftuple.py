'''
'''
Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
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

# Calculate the sum of the tuple values using the predefined sum() method
total_sum = sum(values_tuple)

# Print the sum of the values
print(total_sum)
'''
'''
