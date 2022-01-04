class Person:
    # constructor
    def __init__(self, name, age) -> None:
        print("__Init__")
        self.name = name
        self.age = age
    #
    def __del__(self):
        print("Object is being deconstructed")


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # 객체를 print 할때 사용됨.
    def __str__(self):
        return f"X: {self.x}, y: {self.y}"

    def __repr__(self):
        return

    def __len__(self):
        return 123

    # call 하면 자동 으로 실행되는 구문
    def __call__(self, *args, **kwargs):
        print("Hello I was called!")


v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2
print(v3)
print(len(v3))
v3()



# p = Person("Mike", 25)
