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


result = re.search(r"aza", "plaza")
print(result)

result = re.search(r"aza", "bazaar")
print(result)
