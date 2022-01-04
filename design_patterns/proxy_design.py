# proxy_design.py

from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def person_method(self):
        """ Interface Method """


class Person(IPerson):

    def person_method(self):
        print("I'm a Person!")


# Person 객체를 직접 만들지 않고 아래의 프록시 클래스를 통해 만든다.
class ProxyPerson(IPerson):

    def __init__(self) -> None:
        self.person = Person()

    def person_method(self):
        print("I'm the proxy functionality!")
        self.person.person_method()

    @property
    def Person(self):
        print("from proxy...")
        return self.person

p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()

p3 = p2.Person
p3.person_method()


