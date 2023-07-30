# =========================== Dictionaries ==========================

# dictionaries are used to organize elements into collections. Unlike lists, you don't access elements inside dictionaries using their position. Instead, the data inside dictionaries take the form of pairs of keys and values. To get a dictionary value we use its corresponding key. Another way these two vary is while in a list the index must be a number, in a dictionary you can use a bunch of different data types as keys, like strings, integers, floats, tuples, and more. The name dictionaries comes from how they work in a similar way to human language dictionaries. In an English language dictionary the word comes with a definition.
# Keys inside of a dictionary are unique; updating the value just replaces the key
# Delete keywords with del
x = {}

print(type(x))

# Using a dictionary to store to store the number of files corresponding to each extension
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
# print(file_counts)

# # ? How many txt files
# print(file_counts["txt"])
# print("txt" in file_counts)
# # 14
# print("html" in file_counts)
# False

# add new file

# file_counts["cfg"] = 8
# print(file_counts)

# del file_counts["cfg"]
# print(file_counts)


def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


# print(count_letters("aaaaa"))
# print(count_letters("tenant"))
# print(count_letters("a long string with a lot of letters"))

# ========== Iterating Over Dictionaries ==========

# You can iterate over dictionaries using a for loop, just like with strings, lists, and tuples. This will iterate over the sequence of keys in the dictionary. If you want to access the corresponding values associated with the keys, you could use the keys as indexes. Or you can use the items method on the dictionary, like dictionary.items(). This method returns a tuple for each element in the dictionary, where the first element in the tuple is the key and the second is the value.

# If you only wanted to access the keys in a dictionary, you could use the keys() method on the dictionary: dictionary.keys(). If you only wanted the values, you could use the values() method: dictionary.values().

# If you've got a list of information you'd like to collect and use in your script then the list is probably the right approach. For example, if you want to store a series of IP addresses to ping, you could put them all into a list and iterate over them. Or if you had a list of host names and their corresponding IP addresses, you might want to pair them as key values in a dictionary.

#  you want to use dictionaries when you plan on searching for a specific element
# - can use any immutable data type as keys

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': [
    'yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

speed_limits = {"street": 35, "highway": 65, "school": 15}
speed_limits["highway"]
print(speed_limits["highway"])

car_makes = ["Ford", "Volkswagen", "Toyota"]
car_makes.remove("Ford")
print(car_makes)

animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])


def highlight_word(sentence, word):
    # Complete the return statement using a string method.
    return sentence.replace(word, word.upper())


print(highlight_word("Have a nice day", "nice"))
# Should print: "Have a NICE day"
print(highlight_word("Shhh, don't be so loud!", "loud"))
# Should print: "Shhh, don't be so LOUD!"
print(highlight_word("Automating with Python is fun", "fun"))
# Should print: "Automating with Python is FUN"

# ==================


def first_character(string):
    # Complete the return statement using a string operation.
    return string[0]


print(first_character("Hello, World"))  # Should print H
print(first_character("Python is awesome"))  # Should print P
print(first_character("Keep going"))  # Should print K


# ==================
def alphabetize_lists(list1, list2):

    new_list = []  # Initialize a new list.
    new_list = list1 + list2  # Combine the lists.
    new_list.sort()  # Sort the combined lists.
    new_list = new_list  # Assign the combined lists to the "new_list".
    return new_list


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]


print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']


# ==================

def increments(start, end):
    # Create the required list comprehension.
    return [n for n in range(start + 2, end+3)]


print(increments(2, 3))  # Should print [4, 5]
print(increments(1, 5))  # Should print [3, 4, 5, 6, 7]
print(increments(0, 10))  # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def count_numbers(text):
    # Initialize a new dictionary.
    dictionary = {}
    # Complete the for loop to iterate through each "text" character.
    for char in text:
        # Complete the if-statement using a string method to check if the
        # character is a number.
        if char.isdigit():
            # Complete the if-statement using a logical operator to check if
            # the number is not already in the dictionary.
            if char not in dictionary:
                # Use a dictionary operation to add the number as a key
                # and set the initial count value to zero.
                dictionary[char] = 0
            # Use a dictionary operation to increment the number count value
            # for the existing key.
            dictionary[char] += 1
    return dictionary


print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}

print(count_numbers("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}

print(count_numbers("This is a sentence."))
# Should be {}

print(count_numbers("55 North Center Drive"))
# Should be {'5': 2}
