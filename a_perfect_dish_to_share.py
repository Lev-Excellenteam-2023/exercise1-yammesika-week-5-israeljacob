# Import the math module, which provides various mathematical functions and constants
import math


# Define a function that takes an integer num and returns a list of its proper divisors
def divide_nums(num):
    # Initialize an empty list to store the divisors
    my_list = []
    # Iterate over all integers from 1 to num//2 and check whether each one is a divisor
    for i in range(1, int(num/2)+1):
        if num % i == 0:
            # If i is a divisor, add it to the list of divisors
            my_list.append(i)
    # Return the list of divisors
    return my_list


# Define a generator function that yields perfect numbers one at a time
def a_ֹperfect_dish_to_share():
    # Start with num = 1
    num = 1
    # Enter an infinite loop
    while True:
        # Increment num by 1 on each iteration
        num += 1
        # Calculate the list of proper divisors of num using the divide_nums function
        my_list = divide_nums(num)
        # Calculate the sum of the proper divisors
        my_sum = 0
        for i in my_list:
            my_sum += i
        # Check whether the sum of the proper divisors equals num
        if my_sum == num:
            # If so, yield num
            yield num


# Create a generator object by calling the a_ֹperfect_dish_to_share function
result = a_ֹperfect_dish_to_share()

# Enter an infinite loop to print each perfect number one at a time
while True:
    # Use the next function to get the next perfect number from the generator and print it
    print(next(result))
