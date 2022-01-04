# factory_design.py

from abc import ABCMeta, abstractmethod


# abstract class Person for Teacher, Student
class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def person_method(self):
        """ Interface Method """


class Student(IPerson):

    def __init__(self) -> None:
        self.name = "Basic Student Name"

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):

    def __init__(self) -> None:
        self.name = "Basic Teacher name"

    def person_method(self):
        print("I am a teacher")


s1 = Student()
s1.person_method()
t1 = Teacher()
t1.person_method()

print(isinstance(s1, IPerson))  # student 객체가 IPerson의 객체임을 확인할 수 있다.


class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return -1


if __name__ == '__main__':
    choice = input("What type of person do you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()

