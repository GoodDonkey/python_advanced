# my_script02.py

import sys

# Usage: my_script02.py FILENAME

filename = sys.argv[1]
message = sys.argv[2]

with open(filename, "w+") as f:
    f.write(message)

