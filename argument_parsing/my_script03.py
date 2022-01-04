# my_script03.py

import sys
import getopt

# optional arguments

# Usage: my_script02.py FILENAME

# f 는 명시할 옵션, : 는 옵션 이후에 필수적으로 argument 를 받아야함을 의미
opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])

print(opts)
print(args)

filename = None
message = None

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

print("filename is ", filename)
print("message is ", message)

if filename and message:
    with open(filename, "w+") as f:
        f.write(message)
    print("file written!")


