# Regular Expressions

import re

# log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# index = log.index("[")
# print(log[index+1:index+6])

# A more efficient way is to use regex to extract the process ID by
# importing the re module which lets us use the search function to find regular expressions inside strings

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
# print(result[1])

# Extracting a PID Using regexes

result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])

def extract_pid(log_line):
  regex = r"\[(\d+)\]"
  result = re.search(regex, log_line)
  if result is None:
    return ""
  return result[1]

print(extract_pid(log))

def extract_pid(log_line):
    regex = r"\[(\d+)\]\: (\w+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)



#Basic Matching with grep: grep works by printing out any line that matches the query that we pass it

# Call the search function on the re module; stored the return value of that function in the result variable
# The r indicates that this is a Rawstring

# The span attribute indicates a range where the sub string can be found


result = re.search(r"aza", "plaza")
# print(result)

# output: <re.Match object; span=(2, 5), match='aza'>

result = re.search(r"aza", "bazaar")
# print(result)

# output: <re.Match object; span=(1, 4), match='aza'>

# print(re.search(r"p.ng", "penguin"))

#output: <re.Match object; span=(0, 4), match='peng'>

def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

# print(check_aei("academia")) # True
# print(check_aei("aerial")) # False
# print(check_aei("paramedic")) # True

def check_punctuation (text):
  result = re.search(r"[,-.-!-;-?]", text)
  return result != None

# print(check_punctuation("This is a sentence that ends with a period.")) # True
# print(check_punctuation("This is a sentence fragment without a period")) # False
# print(check_punctuation("Aren't regular expressions awesome?")) # True
# print(check_punctuation("Wow! We're really picking up some steam now!")) # True
# print(check_punctuation("End of the line")) # False

# Repetition Qualifiers

# print(re.search(r"Py.*n", "Pygmalion"))
# print(re.search(r"Py.*n", "Python programming"))
# print(re.search(r"Py[a-z]*n", "Python Programming"))

# print(re.search(r"o+l+", "goldfish"))

import re
def repeating_letter_a(text):
  result = re.search(r"[Aa].*a", text)
  return result != None

# print(repeating_letter_a("banana")) # True
# print(repeating_letter_a("pineapple")) # False
# print(repeating_letter_a("Animal Kingdom")) # True
# print(repeating_letter_a("A is for apple")) # True

#Escaping Characters
# print(re.search(r"\.com", "Gamestop.com"))

# Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.

def check_character_groups(text):
  result = re.search(r"\w\s", text)
  return result != None

# print(check_character_groups("One")) # False
# print(check_character_groups("123  Ready Set GO")) # True
# print(check_character_groups("username user_01")) # True
# print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
# print(re.search(pattern, "_this_is_a_valid_variable_name"))
# print(re.search(pattern, "this isn't a valid variable name"))

# output: <re.Match object; span=(0, 30), match='_this_is_a_valid_variable_name'>


#? ========== Capturing Groups ==========

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
# print(result)
# print(result.groups())

# Function to rearrange names

def rearrange_name(name):
  result = re.search(r"^(\w*), (\w*)$", name) 
  if result is None:
    return name
  return "{} {}".format(result[2], result[1])

rearrange_name("Lovelace, Ada")
rearrange_name("Ritchie, Dennis")



def rearrange_name(name):
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
# print(name)

# ==========
# print(re.search(r"[a-zA-Z]{5}", "a ghost"))

def long_words(text):
  pattern = "\w{7,}"
  result = re.findall(pattern, text)
  return result

# print(long_words("I like to drink coffee in the morning.")) # ['morning']
# print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
# print(long_words("I never drink tea late at night.")) # []