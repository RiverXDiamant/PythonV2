# Loop_Practice: Using the range() function

# ------------------
# range(stop)
# ------------------

for n in range(3):
    print(n)

for n in range(3+1):
    print(n)

# ------------------
# range(start, stop)
# ------------------

for n in range(2, 6):
    print(n)

for n in range(5, 10+1):
    print(n)

# ------------------
# range(start,stop,step)
# ------------------

for n in range(4, 15+1, 2):
    print(n)

for n in range(2*2, 25, 3+2):
    print(n)

for n in range(10, 0, -2):
    print(n)

# -----------------------------------------
# Key Takeaways
# -----------------------------------------

# The roles of the range(start, stop, step) function parameters are:

# Start - Beginning of range

#   value included in range

#   default = 0

# Stop - End of range

#   value excluded from range (to include, use stop+1)

#   no default

#    must provide the ending index number

# Step - Incremental value

#   default = 1
