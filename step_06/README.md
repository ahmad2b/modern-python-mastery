# Control Flow and Typing Guide

* if statement
* if-else statement
* if-elif-else statement
* nested if-else-elif
* static type and variables
* union type
* optional type
* zip function with lists
* sorting a list of tuples

## if Statement

```python
x : int = 10
if x < 5:
    print("x is greater than 5")
```

## if-else statement

```python
x : int = 4

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

## if-elif-else statement

```python
x : int = 4
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

## nested if-else-elif

```python
x : int = 10
y : int = 5

if x > 5:
    if y > 5:
        print("x and y are both greater than 5")
    else:
        print("x is greater than 5 but y is not")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

## static type variables

In python 3.6 and later, you cna use static type annotations to indicate the expected type of a variable.

```python
x : int = 10
y : int = "Hello"
z : float = 3.14
```

## Union and Optional Types

`union` allows a variable to be a one of several types, `Optional` is a shorthand for `Union[T, None]`

```python
from typing import Union, Optional

def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, Guest!"
    else:
        return f"Hello, {name}!"

age: Union[int, str] = "Twenty"

print(greet())
print(greet("John"))
```

## Zip Function with lists

The `zip` function is used to combine two or more iterables.

```python
names: list[str] = ["Alice", "Bob", "Charlie"]
ages: list[int] = [25, 30, 35]

zipped = zip(names, ages)
for name, age in zipped:
    print(f"{name} is {age} years old")
```

## Sorting a list of tuples

You can sort a list of tuples based on the second tuple index using the `sorted` function.

```python
tuples: list[tuple[str, int]] = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
sorted_tuples = sorted(tuples, key = lambda x:x[1])
print(sorted_tuples) # Output: [('Charlie', 20), ('Alice', 25), ('Bob', 30)]
```