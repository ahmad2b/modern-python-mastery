# Functions in Python

* `Pre-defined Functions`: 
* `User-defined Functions`
* `Arguments and Parameters` 
* `Default Functions` 
* `Optional, Positional, and Keyword Arguments`
* `Lambda Functions`
* `Recursive Functions`
* `Decorators`
* `Functions with Unlimited Arguments`

### Pre-defined Functions

These are built-in functions provided by Python, such as `print()`, `len()`, etc. For example, `print("Hello, World!")` will output the string "Hello, World!".

### User-defined Functions

These are functions defined by the users themselves using the `def` keyword.

**Example**
 ```python
def greet(name):
    return "Hello, " + name
```

### Arguments and Parameters

Parameters are the names used when defining a function, while arguments are the values passed into the function. For example, in `def greet(name: str):, name` is a parameter. In `greet("Alice")`, "Alice" is an argument.

### Default Functions

These are user-defined functions that have default values for parameters.

**Example**
 ```python
def greet(name: str = "World"):
    return "Hello, " + name
```

### Optional, Positional, and Keyword Arguments

#### Optional Arguments

Optional arguments are arguments that are optional as they have a default value.

**Example**
 ```python
def greet(name: str = "World"):
    return "Hello, " + name
```

#### Positional Arguments

Positional arguments are arguments that need to be in the correct positional order.

**Example**
 ```python
def subtract(a: int, b: int) -> int:
    return a - b

result: int = subtract(10, 5)
print(result)
```

#### Keyword Arguments

Keyword arguments are arguments passed to a function by explicitly specifying the name of the parameter.

**Example**
 ```python
def divide(dividend: int, divisor: int) -> float:
    return dividend / divisor

result: float = divide(divisor=5, dividend=25)
print(result)
```

### Lambda Functions

 These are small anonymous functions defined using the `lambda` keyword. 

**Example**
 ```python
 square: callable = lambda x: x ** 2
```

### Recursive Functions

These are functions that call themselves during their execution.

**Example**
 ```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
```

### Decorators

These are functions that modify the functionality of another function.

**Example 1**
 ```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")
```

**Example 2**
 ```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")
```

### Functions with Unlimited Arguments

These are functions that can take any number of arguments. These arguments are usually stored in a tuple or a dictionary.

#### Unlimited Positional Arguments

**Example**
 ```python
def add(*numbers: int) -> int:
    return sum(numbers)

result: int = add(1, 2, 3, 4, 5)
print(result)
```

#### Unlimited Keyword Arguments

**Example**
 ```python
def print_key_values(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_key_values(name="John", age="30", country="USA")
```