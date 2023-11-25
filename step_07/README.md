# Python Static Typing for Dictionaries

Creation of dictionaries (Obj's in Javascript) in python using static typing.

* Setting up Static Typing
* Creating Dictionaries
  * Using Any Type
  * Using Optional Type
  * Using Union Type
* Dictionary Comprehensions
* Swapping Keys and Values

## Setting up Static Typing

import the required types from the `typing` module to use static typing in Python.

```python
from typing import Any, Optional, Union
```

## Creating Dictionaries

### Using `Any` Type

`Any` is the most flexible type. It can represent any type at all. 

Example:

```python
from typing import Dict

my_dict: Dict[Any, Any] = {
    1: "one",
    "two": 2,
    (3, 4): [3, 4]
}
```

### Using `Optional` Type

`Optional` is an alternate to type that can either specified type of `None`

Example:
```python
from typing import Dict

my_optional_dict: Dict[Any, Optional[int]] = {
    1: 10,
    "two": None,
    (3, 4): 34
}
```

### Using `Union` Type

`Union` type allows us to specify that a value can be one of several types.

Example:
```python
from typing import Dict

my_union_dict: Dict[Any, Union[int, str]] = {
    1: "one",
    "two": 2,
    (3, 4): "three-four"
}
```

## Dictionary Comprehension

Dictionary comprehensions provide a concise way to create dictionaries.

```python
squared_numbers = {
    i: i**2 for i in range(5)
}
```

## Swapping Keys and Values

To swap the keys and values of dictionary:

```python
swapped_dict = {
    v: k for k, v in my_dict.items()
}
```