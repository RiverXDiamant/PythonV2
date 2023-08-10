# ========== Managing Data and Processes

import os
import sys
import subprocess

# filename = sys.argv[1]

# if not os.path.exists(filename):
#     with open(filename, 'w') as f:
#         f.write("New file created\n")
# else:
#     print("Error, the file {} already exists!".format(filename))
#     sys.exit(1)

# Running System Commands in Python

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)

# ====================== Log Files =======================

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+))$" 
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
print(usernames)

import re
def show_time_of_pid(line):
  pattern = r'^(\w+ [0-9] [0-9]+:[0-9]+:[0-9]+) [\w\.]+ [\w=]+\[([0-9]+)\]'
  result = re.search(pattern, line)
  return '{} pid:{}'.format(result[1],result[2])

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187


