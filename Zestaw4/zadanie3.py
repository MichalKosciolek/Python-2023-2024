# podpunkt A) 
# zdefiniować w ramach klasy A funkcję foo(self, x), metodę klasy class_foo, metodę statyczną static_foo, 
# tak, żeby kod poniżej drukował treści jak w komentarzach

class A(object):
    def foo(self, x):
        print(f'wykonanie foo({self}, {x})')

    @classmethod
    def class_foo(cls, x):
        print(f'class_foo({cls}, {x})')

    @staticmethod
    def static_foo(x):
        print(f'wykonanie static_foo({x})')

a = A()
a.foo(123) # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
A.foo(a,123) # ditto
a.class_foo(123) # class_foo(<class '__main__.A'>, 123)
A.class_foo(123) # ditto
a.static_foo(123) # wykonanie static_foo(123)
A.static_foo(123) # ditto

print("-----------------")

# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class BaseChild1(Base):
    def abstract_method(self):
        print("Hello from BaseChild1")

class BaseChild2(Base):
    def abstract_method(self):
        print("Hello from BaseChild2")

c1 = BaseChild1()
c1.abstract_method()

c2 = BaseChild2()
c2.abstract_method()

print("-----------------")

# podpunkt C)
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez 
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu

class MyClass:
    def __init__(self):
        self._nazwa = None

    @property
    def nazwa(self):
        return self._nazwa

    @nazwa.setter
    def nazwa(self, value):
        self._nazwa = value

a = MyClass()
a.nazwa = "Nazwa"
print(a.nazwa)