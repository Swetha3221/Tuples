'''
'''
 Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4

'''
'''
Ans:
# Input: a string of space-separated numbers
input_values = input("Enter tuple values: ")

# Split the input string into individual numbers and convert them to integers
numbers_tuple = tuple(map(int, input_values.split()))

# Input: the value to count
x = int(input("Enter the value to count: "))

# Count the occurrences of x in the tuple
count_x = numbers_tuple.count(x)

# Print the result
print(count_x)
  
'''
'''
