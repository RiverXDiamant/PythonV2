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
print(result[1])


#Basic Matching with grep: grep works by printing out any line that matches the query that we pass it

# Call the search function on the re module; stored the return value of that function in the result variable
# The r indicates that this is a Rawstring

# The span attribute indicates a range where the sub string can be found


result = re.search(r"aza", "plaza")
print(result)

# output: <re.Match object; span=(2, 5), match='aza'>

result = re.search(r"aza", "bazaar")
print(result)

# output: <re.Match object; span=(1, 4), match='aza'>

print(re.search(r"p.ng", "penguin"))

#output: <re.Match object; span=(0, 4), match='peng'>

def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True