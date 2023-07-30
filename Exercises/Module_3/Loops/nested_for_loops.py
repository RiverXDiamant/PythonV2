# Nested For Loops

# ? For loops are best when you want to iterate over a known sequence of elements
# ? When you want to operate while a certain condition is true, while loops are the best choice

# Nested loop within a function
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end="")
    print()


# Combining a nested loop with conditionals

teams = ['Dragons', 'Wolves', 'Pandas', "Unicorns"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

# ------------------------------------------------

# Iterates over the list and greets each friend


def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)


greet_friends(['Taylor', 'Luis', 'Jamaal', 'Eli'])

# ------------------------------------------------

# greet_friends("Barry") <-- will iterate through each letter of a string
#! If you want it to iterate over the whole string, have that string be a part of a list

# ------------------------------------------------

# * Question 2

# Fill in the blanks to make the factorial function return the factorial of n. Then, print the first 10 factorials (from 0 to 9) with the corresponding number. Remember that the factorial of a number is defined as the product of an integer and all integers before it. For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.


def factorial(n):
    result = 1
    for x in range(1, n):
        result = result * x
    return result


for n in range(0, 10):
    print(n, factorial(n+1))

# ------------------------------------------------

# * Question 3

# Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.

for x in range(1, 11):
    print(x**3)

# ------------------------------------------------

# * Question 4

# Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.

for multiples_of_7 in range(0, 100, 7):
    print(multiples_of_7)

# ------------------------------------------------

# * Question 5

# The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts.  Currently the code will keep executing the function even if it succeeds. Fill in the blank so the code stops trying after the operation succeeded.


def retry(operation, attempts):
    for n in range(attempts):
        if operation():
            print("Attempt " + str(n) + " succeeded")
        if n == 1:
            break
        else:
            print("Attempt " + str(n) + " failed")


retry(create_user, 3)
retry(stop_service, 5)

# While Loops


def is_power_of_two(number):
    # This while loop checks if the "number" can be divided by two
    # without leaving a remainder. How can you change the while loop to
    # avoid a Python ZeroDivisionError?
    while number % 2 == 0:
        if (number == 0):
            break
        number = number / 2
    # If after dividing by 2 "number" equals 1, then "number" is a power
    # of 2.
    if number == 1:
        return True
    return False


# Calls to the function
print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False


# Fill in the blanks so that the while loop continues to run while the
# "divisor" variable is less than the "number" parameter.

def sum_divisors(number):
    # Initialize the appropriate variables
    divisor = 1
    total = 0

    # Avoid dividing by 0 and negative numbers
    # in the while loop by exiting the function
    # if "number" is less than one
    if number < 1:
        return 0

    # Complete the while loop
    while divisor < number:
        if number % divisor == 0:
            total += divisor
        # Increment the correct variable
        divisor += 1

    # Return the correct variable
    return total


print(sum_divisors(0))  # Should print 0
print(sum_divisors(3))  # Should print 1
# 1
print(sum_divisors(36))  # Should print 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should print 1+2+3+6+17+34+51
# 114


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

multiplication_table(5)
# Should print:
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25

multiplication_table(8)
# Should print:
# 8x1=8
# 8x2=16
# 8x3=24
