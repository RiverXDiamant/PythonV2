# ========== Raising Errors ==========

import random

# participants = ['Jack','Jill','Larry','Tom']

# def Guess(participants):
#     try:
#         f = (participants)
#     except OSError:
#         return None
#     my_participant_dict = {}
#     for participant in participants:
#         my_participant_dict[participant] = random.randint(1, 9)
#     if my_participant_dict['Larry'] == 9:
#         return True
#     else:
#         return False
    
# print(Guess(participants))

# ==========================================================

def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        if not username.isalnum():
            return False
        return True
    
# validate_user([3], 1)

my_list = [27, 5, 9, 6, 8]

def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("Value must be given in this list")
    else:
        my_list.remove(myVal)
    return my_list

print(RemoveValue(27))

my_word_list = ['east', 'after', 'up', 'over', 'inside']

def OrganizeList(myList):
    for item in myList:
        assert type(myList) == str, "Word list must be a list of strings"
    myList.sort()
    return myList

my_new_list = [6, 3, 8, "12", 42]

print(OrganizeList(my_new_list))