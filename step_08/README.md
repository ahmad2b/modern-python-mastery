# Python Dictionary Guide

How to create dictionaries?
How to work with dictionaries?
How to access values, add key-value pairs?
Dictionary Methods

* Introduction
* Creating a Dictionary
* Accessing Values
* Adding Key-Value Pairs
* Dictionary Methods
  * clear
  * copy
  * fromkeys
  * get
  * items
  * keys
  * pop
  * popitem
  * setdefault
  * update
  * values

## Introduction

A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key.

## Creating a Dictionary

In python, a dictionary is defined within braces `{}` with each item being a pair in the form `key:value`. Key and value can be of any type.

Example:
```python
my_dict = {
    "name" : "John",
    "age" : 30
}
```

## Accessing Values

You can access the items of a dictionary by referring to its key name, inside square brackets.

```python
print(my_dict["name"])
```

## Adding Key-Value Pairs

You can add a new item to a dictionary by using a new key and assigning a value to it.

Example:
```python
my_dict["job"] = "Engineer"
print(my_dict)
```

## Dictionary Methods

Python has a set of built-in methods that you can use on dictionaries.

1. `clear()`: removes all the elements from a dictionary.
2. `copy()`: returns a copy of the dictionary.
3. `fromkeys()`: returns a dictionary with the specified keys and the specified value.
4. `get()`: returns the value of the specified key.
5. `items()`: returns a view object that displays a list of a dictionary's key-value tuple pairs.
6. `keys()`: returns a view object that displays a list of all the keys in the dictionary.
7. `pop()`: removes the specified item from the dictionary.
8. `popitem()`: removes the item that was last inserted into the dictionary.
9. `setdefault()`: returns the value of the specified key. If the key does not exist: insert the key, with the specified value.
10. `update()`: updates the dictionary with the specified key-value pairs.
11. `values()`: returns a view object that displays a list of all the values in the dictionary.