# Object-Oriented Programming in Python

Object-Oriented Programming (OOP) is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.

or

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data and code that manipulates that data. Objects are instances of classes, which can hold both data (attributes) and code (methods).


## Classes and Objects

In Python, everything is an object. You can create your own objects by defining a class, which is a blueprint for creating objects.

```python
class MyClass:
    pass
```

## Methods

Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.

```python
class MyClass:
    def my_method(self):
        pass
```

```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute
    
    def bark(self):       # Method
        print("Woof!")
```

## Attributes and Class Variables

Attributes are variables stored in an instance or class. Class variables are shared by all instances of a class.

```python
class MyClass:
    class_var = 'I am a class variable'

    def __init__(self, attr):
        self.attr = attr
```

```python
class Dog:
    species = "Canis familiaris"  # Class variable
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("Woof!")
```

## Inheritence

Inheritance is a way of creating a new class using details of an existing class without modifying it.

```python
class MyParentClass:
    pass

class MyChildClass(MyParentClass):
    pass
```

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def bark(self):
        print("Woof!")
```

### Examples

```python
class MyClass:
    class_var = 'I am a class variable'

    def __init__(self, attr):
        self.attr = attr

    def my_method(self):
        print(self.attr)

my_instance = MyClass('I am an instance attribute')
my_instance.my_method()  # prints: I am an instance attribute
```