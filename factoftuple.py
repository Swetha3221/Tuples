'''
'''
 Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
'''
'''
Ans:
def custom_factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Input: a string of numbers followed by the number to count
input_numbers = input("Enter numbers: ")
x = int(input("Enter the number to count: "))

# Create a tuple from the input string of numbers
numbers_tuple = tuple(map(int, input_numbers.split()))

# Count the occurrences of x in the tuple
count_x = numbers_tuple.count(x)

# Calculate the factorial of the count
factorial_value = custom_factorial(count_x)

# Print the result
print(factorial_value)
'''
'''
