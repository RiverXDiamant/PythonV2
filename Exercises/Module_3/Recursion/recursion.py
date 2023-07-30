# Recursion: The repeated application of the same procedure to a smaller problem
#   - lets us tackle complex problems by reducing the problem to a simpler one
#   - a way of doing a repetitive task by having a function call itself
#   -  Base Case ( specific condition): A recursive function calls itself usually with a modified parameter until it reaches a specific condition.

# ? A recursive function will usually have this structure:

def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)

# Example 1: Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. Note: base is assumed to be a positive number.


def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return number == 1

    # Recursive case: keep dividing number by base.
    return is_power_of(number//base, base)


print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False

# Example #2: The count_users function recursively counts the amount of users that belong to a group in the company system, by going through each of the members of a group and if one of them is a group, recursively calling the function and counting the members


def count_users(group):
    count = 0
    for member in get_members(group):
        if is_group(member):
            count += count_users(member)
        else:
            count += 1
    return count


print(count_users("sales"))  # Should be 3
print(count_users("engineering"))  # Should be 8
print(count_users("everyone"))  # Should be 18

# Example #3: Implement the sum_positive_numbers function, as a recursive function that returns the sum of all positive numbers between the number n received and 1


def sum_positive_numbers(n):
    if n == 0:
        return n
    return n + sum_positive_numbers(n-1)


print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15

# ? Week 3 Quiz

number = 15  # Initialize the variable
while number >= 5:  # Complete the while loop condition
    print(number, end=" ")
    number -= 5  # Increment the variable


# Should print 15 10 5

for number in range(5, -1, -1):
    print(number)

# Should print:
# 5
# 4
# 3
# 2
# 1
# 0


def factorial(n):
    result = n
    start = n
    n -= 1
    while n > 0:  # The while loop should execute as long as n is greater than 0
        result *= n  # Multiply the current result by the current value of n
        n -= 1  # Decrement the appropriate variable by -1
    return result


print(factorial(3))  # Should print 6
print(factorial(9))  # Should print 362880
print(factorial(1))  # Should print 1


def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    rows = 5
    for x in range(1, 1, 1):
        # Complete the inner loop range to control the number of

        # asterisks per row
        for y in range(rows):
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the
        # end of the row
        print()


rows_asterisks(5)
# Should print the asterisk rows shown above


def countdown(start):
    x = start
    if x > 0:
        return_string = "Counting down to 0: "
        while x >= 0:  # Complete the while loop
            return_string += str(x)  # Add the numbers to the "return_string"
            if x > 0:
                return_string += ","
            x -= 1  # Decrement the appropriate variable
    else:
        return_string = "Cannot count down to 0"
    return return_string


print(countdown(10))  # Should be "Counting down to 0: 10,9,8,7,6,5,4,3,2,1,0"
print(countdown(2))  # Should be "Counting down to 0: 2,1,0"
print(countdown(0))  # Should be "Cannot count down to 0"


def all_numbers(minimum, maximum):

    return_string = ""  # Initializes variable as a string

    # Complete the for loop with a range that includes all
    # numbers up to and including the "maximum" value.
    for number in range(minimum, maximum + 1):

        # Complete the body of the loop by appending the number
        # followed by a space to the "return_string" variable.
        return_string += str(number) + ""

    # This .strip command will remove the final " " space
    # at the end of the "return_string".
    return return_string.strip()


print(all_numbers(2, 6))  # Should be 2 3 4 5 6
print(all_numbers(3, 10))  # Should be 3 4 5 6 7 8 9 10
print(all_numbers(-1, 1))  # Should be -1 0 1
print(all_numbers(0, 5))  # Should be 0 1 2 3 4 5
print(all_numbers(0, 0))  # Should be 0

# Multiplication Table


def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(start, stop + 1):
        # Complete the inner loop range
        for y in range(start, stop + 1):
            # Prints the value of "x" multiplied by "y"
            # and inserts a space after each value
            print(str(x*y), end=" ")
        # An empty print() function inserts a line break at the
        # end of the row
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above
