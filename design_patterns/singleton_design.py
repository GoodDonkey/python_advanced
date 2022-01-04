# singleton_design.py

from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def print_data(self): pass


""" 하나의 클래스는 하나의 인스턴스를 가져야 하므로
    객체를 가리키는 표현은 PersonSingleton.__instance 를 사용한다.
    self를 사용하면 생성된 객체를 가리키게 되므로 사용하지 않는다. """


class PersonSingleton(IPerson):

    __instance = None  # 클래스 변수로 선언

    def __init__(self, name, age) -> None:
        if PersonSingleton.__instance is not None:  # 이미 객체가 있는 경우.
            raise Exception("Singleton cannot be instantiated more than one")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def get_instance():

        if PersonSingleton.__instance is None:
            PersonSingleton("Default Name", 0)  # __init__()

        return PersonSingleton.__instance

    def print_data(self):
        print(f"Name: {PersonSingleton.__instance.name}\n Age: {PersonSingleton.__instance.age}")


p = PersonSingleton("donkey", 30)
print(p)
p.print_data()

# 1개 이상 객체를 생성할 수 없다.
# p2 = PersonSingleton("Bob", 25)

p3 = PersonSingleton.get_instance()
print(p3)  # 같은 인스턴스인지 확인하기
