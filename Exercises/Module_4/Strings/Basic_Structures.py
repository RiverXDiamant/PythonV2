# Strings, Lists and Dictionaries

# Manipulate strings using indexing, slicing, and formatting
# Use lists and tuples to store, reference, and manipulate data
# Leverage dictionaries to store more complex data, reference data by keys, and manipulate data stored
# Combine the String, List, and Dictionary data types to construct complex data structures

# String Indexing and Slicing

#! Strings in Python are immutable; Must create a new str based on the old one

# String indexing allows you to access individual characters in a string. You can do this by using square brackets and the location, or index, of the character you want to access. It's important to remember that Python starts indexes at 0. So to access the first character in a string, you would use the index [0]. If you try to access an index that’s larger than the length of your string, you’ll get an IndexError. This is because you’re trying to access something that doesn't exist! You can also access indexes from the end of the string going towards the start of the string by using negative values. The index [-1] would access the last character of the string, and the index [-2] would access the second-to-last character.


# Example

word = "supercalifragilisticexpialadocious"
print(word.index("x"))

# Output: 21

# pets = "Cats & Dogs"

# "Dragons" in pets

# Formatting Strings


def student_grade(name, grade):
    return "{name} received {grade}% on the exam".format(name=name, grade=grade)


# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))

price = 7.5
with_tax = price * 1.09
# print(price, with_tax)

print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

#  ${:.2f} <-- formatting expression

# You can use the format method on strings to concatenate and format strings in all kinds of powerful ways. To do this, create a string containing curly brackets, {}, as a placeholder, to be replaced. Then call the format method on the string using .format() and pass variables as parameters. The variables passed to the method will then be used to replace the curly bracket placeholders. This method automatically handles any conversion between data types for us.

# If the curly brackets are empty, they’ll be populated with the variables passed in the order in which they're passed. However, you can put certain expressions inside the curly brackets to do even more powerful string formatting operations. You can put the name of a variable into the curly brackets, then use the names in the parameters. This allows for more easily readable code, and for more flexibility with the order of variables.

# You can also put a formatting expression inside the curly brackets, which lets you alter the way the string is formatted. For example, the formatting expression {:.2f} means that you’d format this as a float number, with two digits after the decimal dot. The colon acts as a separator from the field name, if you had specified one. You can also specify text alignment using the greater than operator: >. For example, the expression {:>3.2f} would align the text three spaces to the right, as well as specify a float number with two decimal places. String formatting can be very handy for outputting easy-to-read textual output.
