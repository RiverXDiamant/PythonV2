# ========== OOP ==========

# Models concepts using classes and objects
# - A flexible, powerful paradigm where classes represent and define concepts, while objects are an instance of classes.

# In object-oriented programming, concepts are modeled as classes and objects. An idea is defined using a class, and an instance of this class is called an object. Almost everything in Python is an object, including strings, lists, dictionaries, and numbers. When we create a list in Python, we’re creating an object which is an instance of the list class, which represents the concept of a list. Classes also have attributes and methods associated with them. Attributes are the characteristics of the class, while methods are functions that are part of the class.

# Type function examples
#   Tells us which class the value or variable belongs to
print(type({}))
print(type([]))
print(type(""))
print(type(9))

# dir()
# List of all the attributes and methods in a class
#! Special Methods begin and End with double underscores;  they're called by some of the internal Python functions
# print(dir(""))
# print("================================")
# print(dir(9))
# print("================================")
# print(dir({}))
# print("================================")
# print(dir([]))

# When we use the help function on any variable or value, we're showing all the documentation for the corresponding class.
# help("")


class Birds:
    color = ""
    number = []


# bluejay = Birds()
# bluejay.count()
# print(bluejay.number)


# ========== Classes and Methods ==========

# Constructor

class Peach:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


georgia = Peach("Peachy", "succulent")
print(georgia.color)
print(georgia.flavor)


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)


help(Apple)

# Docstrings - have to be indented at the same level on block its documenting


def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes, and seconds."""
    return hours*3600+minutes*60+seconds


help(to_seconds)


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        """Outputs a message with the name of the person."""
        print("Hello! My name is {name}.".format(name=self.name))


help(Person)

# Inheritance


class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


class Pear(Fruit):
    pass


class Grape(Fruit):
    pass


toms = Pear("green", "sweet")
carnelian = Grape("purple", "sweet")
print(toms.flavor)
print(carnelian.color)


class Clothing:
    material = ""

    def __init__(self, name):
        self.name = name

    def check_material(self):
        print("This {} is made of {}".format(self.name, self.material))


class Shirt(Clothing):
    material = "Cotton"


polo = Shirt("Polo")
polo.check_material()
