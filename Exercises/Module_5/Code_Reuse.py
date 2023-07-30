# ======================= Composition ==================

# imports
import datetime
import random

# Object Composition ============


class Repository:
    def __inti__(self):
        self.packages = {}

    def add_package(self, package):
        self.packages[package.name] = package

    def total_size(self):
        result = 0
        for package in self.package.values():
            result += package.size
        return result


# Example 1 ===============================
class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class shirt(Clothing):
    material = "Cotton"


class pants(Clothing):
    material = "Cotton"


polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)


# ========== Python Modules ==========
# Modules can be used to organize functions, classes, and other data together in a structured way
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

now = datetime.datetime.now()
print(type(now))
print(now)

print(now.year)
print(now + datetime.timedelta(days=28))
