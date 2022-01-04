# infinite sequence

# 1에서 계속 5를 곱해서 값을 주는 generator
def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5


values = infinite_sequence()

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

for x in range(100):
    print(values.__next__())
