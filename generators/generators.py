# Seq 1 to 9,000,000
import sys


def my_generator(n):
    for x in range(n):
        yield x ** 3


values = my_generator(1000)
print("size of values: ", sys.getsizeof(values), " bytes")

# next 로 iterate
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print("--------------")

# for 문으로 iterate
li = []
for x in values:
    li.append(x)

print("size of li: ", sys.getsizeof(li), " bytes")




