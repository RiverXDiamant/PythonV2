# Lists Examples

def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return (words[n-1])
    return ("")


# print(get_word("This is a lesson about lists", 4))  # Should print: lesson
# print(get_word("This is a lesson about lists", -4))  # Nothing
# print(get_word("Now we are cooking!", 1))  # Should print: Now
# print(get_word("Now we are cooking!", 5))  # Nothing


# ? We use tuples to store information that refers to a specific thing and does not change; i.e. - someones Full Name

# Tuples
# As we mentioned earlier, strings and lists are both examples of sequences. Strings are sequences of characters, and are immutable. Lists are sequences of elements of any data type, and are mutable. The third sequence type is the tuple. Tuples are like lists, since they can contain elements of any data type. But unlike lists, tuples are immutable. They’re specified using parentheses instead of square brackets.

# You might be wondering why tuples are a thing, given how similar they are to lists. Tuples can be useful when we need to ensure that an element is in a certain position and will not change. Since lists are mutable, the order of the elements can be changed on us. Since the order of the elements in a tuple can't be changed, the position of the element in a tuple can have meaning. A good example of this is when a function returns multiple values. In this case, what gets returned is a tuple, with the return values as elements in the tuple. The order of the returned values is important, and a tuple ensures that the order isn’t going to change. Storing the elements of a tuple in separate variables is called unpacking. This allows you to take multiple returned values from a function and store each value in its own variable.

# Tuple Example

def file_size(file_info):
    name, type, size = file_info
    return ("{:.2f}".format(size / 1024))


# print(file_size(('Class Assignment', 'docx', 17875)))  # Should print 17.46
# print(file_size(('Notes', 'txt', 496)))  # Should print 0.48
# print(file_size(('Program', 'py', 1239)))  # Should print 1.21

# Iterating over Lists and Tuples

# Using enumerate function; Get the index of an element while going through a list

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))

# Output - the enumerate function returns a tuple for every element in a list

# 1 - Ashley
# 2 - Dylan
# 3 - Reese


# Example # 2 - define a function that receives a list of people

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result


print(full_emails([("alex@example.com", "Alex Diego"),
      ("shay@example.com", "Shay Brandt")]))

#! word of caution about some common errors when dealing with lists in Python. Because we use the range function so much with for loops, you might be tempted to use it for iterating over indexes of a list and then to access the elements through indexing. You could be particularly inclined to do this if you're used to other programming languages before. Because in some languages, the only way to access an element of a list is by using indexes. Real talk, this works but looks ugly.
#
#! It's more idiomatic in Python to iterate through the elements of the list directly or using enumerate when you need the indexes like we've done so far. There are some specific cases that do require us to iterate over the indexes, for example, when we're trying to modify the elements of the list we're iterating. By the way, if you're iterating through a list and you want to modify it at the same time, you need to be very careful. If you remove elements from the list while iterating, you're likely to end up with an unexpected result. In this case, it might be better to use a copy of the list instead.


def skip_elements(elements):
    # code goes here
    new_list = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            new_list.append(element)
    return new_list


# # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# # Should be ['Orange', 'Strawberry', 'Peach']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))

# List Comprehensions -
# Lets us create new lists based on sequences or ranges
# Can also use conditional clauses

# multiples = []
# for x in range(1, 11):
#     multiples.append(x*7)
# print(multiples)

# More efficient way  using List comprehension

multiples = [x*7 for x in range(1, 11)]
# print(multiples)

# List Comprehension #2
# generate a list of the lengths if the strings

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
# print(lengths)

# All numbers divisible by 3 from 0 to 100
z = [x for x in range(0, 101) if x % 3 == 0]
print(z)


def odd_numbers(n):
    return [x for x in range(0, n+1) if x % 2 != 0]


print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10))  # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11))  # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1))  # Should print []

# ==================== Simple and Long Form List Comprehension ===========================

# Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines
# of code into one line:
print([x*2 for x in range(1, 11)])


# Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1, 11):
    my_list.append(x*2)
print(my_list)

# ================ List Comprehension with Conditional Statement ====================

# List Comprehension with Conditional Statement
print("List comprehension result:")

# The following list comprehension compacts multiple lines
# of code into one line:
print([x for x in range(1, 101) if x % 10 == 0])

# Long form for loop with nested if-statement
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1, 101):
    if x % 10 == 0:
        my_list.append(x)
print(my_list)


def squares(start, end):
    return [n*n for n in range(start, end + 1)]


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# ? Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

filenames = ["program.c", "stdio.hpp",
             "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [l.replace('.hpp', '.h') for l in filenames]


print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# ? Question 2
# Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.


def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    piggy_text = []
    for word in words:
        # Create the pig latin word and add it to the list
        word = word[1:] + word[0] + 'ay'
        piggy_text.append(word)
        # Turn the list back into a phrase
    return ' '.join(piggy_text)


print(pig_latin("hello how are you"))

print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# Should be "rogrammingpay niay ythonpay siay unfay"
print(pig_latin("programming in python is fun"))


# ? Question 3
# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
#  For example:
#  640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
#  755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
#  Fill in the blanks to make the code convert a permission in octal format into a string format.

def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += "-"
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------

# ? The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that.


def guest_list(guests):
    for name, age, position in guests:

        print("{} is {} years old and works as {}".format(name, age, position))


guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'),
           ('Amanda', 25, "Engineer")])
