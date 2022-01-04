class Person:

    # __var 는 private 변수이다.
    def __init__(self, name, age, gender) -> None:
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        # 다양한 조건을 추가하여 setter 정의 하면 된다.
        if len(value) > 10:
            print("that's too long name.")
        else:
            self.__name = value

    @staticmethod
    def my_method():
        print("Hello World!")

    def my_method02(self):
        print("Non-static", self.__name)


Person.my_method()

p1 = Person("donkey", 20, "m")
print(p1.Name)
p1.Name = "donkkkey"
print(p1.Name)

p1.my_method()  # static 인데 객체로도 사용가능

Person.my_method02(p1)  # instance method 라도 객체를 넣어주기만 하면 됨...


