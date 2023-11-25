# Python Data structures and loops

* Lists
* For loop
* else with for loop
* list comprehension
* tuples
* methods

## List

A list is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Lists are defined by having values between square brackets `[]`.

Example:
```python
fruits = ['apple', 'banana', 'cherry']
print(fruits)
```

## For Loop

The for loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.

Example:
```python
for fruit in fruits:
    print(fruit)
```

## Else with For Loop

The `else` statement can be used with a for loop for code that is to be executed when the loop has finished executing, but only if the loop completed normally (i.e., it did not encounter a break statement).

Example:
```python
for fruit in fruits:
    print(fruit)
else:
    print("No fruits left.")
```

## List Comprehension

List Comprehension is an elegant way to define and create lists based on existing lists. It is a more succinct way to create lists in Python.

Example:
```python
squares = [x**2 for x in range(10)]
print(squares)
```

## Tuples

A tuple is similar to list. The difference between the two is that tuples are immutable, which means we cannot change the elements of a tuple once it is assigned, whereas in a list, elements can be changed.

Example:
```python
dimensions = (1920, 1080)
print(dimensions)
```

## Methods

Here are some commonly used methods for lists and tuples:

### List Methods:
* `append()`: Adds an element at the end of the list
* `extend()`: Add the elements of a list (or any iterable), to the end of the current list
* `remove()`: Removes the first item with the specified value

### Tuple Methods:
* `count()`: Returns the number of times a specified value occurs in a tuple
* Searches the tuple for a specified value and returns the position of where it was found
