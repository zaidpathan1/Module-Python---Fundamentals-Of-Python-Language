from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squared = list(map(lambda x: x**2, numbers))
product = reduce(lambda x, y: x * y, numbers)
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Print the result
print("Original list:", numbers)
print("Squared list:", squared)
print("Product of all numbers:", product)
print("Odd numbers:", odd_numbers)
