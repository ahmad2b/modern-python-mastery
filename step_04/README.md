# Python Lists and Their Methods

## List

A list in python is an ordered collection of items. Lists can contain a mix of different data types, including numbers, strings and other lists. Lists are created by placing the items inside square brackets `[]`, separated by commas.

Example
```python
bikes: list[str] = ['Harley', 'BMW', 'Suzuki', 'Yamaha', 'Ducati']
```

* Indexes
* Slicing
* Positive Indexing
* Negative Indexing
* List Methods in python

### Indexing

Indexes are used to access individual items from a list. They start at 0 for the first item.

```python
print(bikes[0]) # Output: Harley
```

### Slicing

It let you obtain a subset of items from a list. the syntax for slicing is `list[start:stop:step]`

Example
```python
print(bikes[1:4]) # Output: ['BMW', 'Suzuki', 'Yamaha']
```

### Positive Indexing

It start from the beginning of the list.

Example
```python
print(bikes[2]) # Output: Suzuki
```

### Negative Indexing

It starts from the end of the list with `-` sign.

Example
```python
print(bikes[-1]) # Output: Ducati
```

### List Methods in Python

### List Methods in Python

Python lists have several useful methods for manipulating lists:

1. `append(item)`: Adds an item to the end of the list.
    ```python
    bikes.append('Kawasaki')
    print(bikes)  # Output: ['Harley', 'BMW', 'Suzuki', 'Yamaha', 'Ducati', 'Kawasaki']
    ```

2. `extend(iterable)`: Adds all items from an iterable (like list, set, tuple) to the end of the list.
    ```python
    bikes.extend(['Triumph', 'KTM'])
    print(bikes)  # Output: ['Harley', 'BMW', 'Suzuki', 'Yamaha', 'Ducati', 'Kawasaki', 'Triumph', 'KTM']
    ```

3. `insert(index, item)`: Inserts an item at a specific position in the list.
    ```python
    bikes.insert(1, 'Aprilia')
    print(bikes)  # Output: ['Harley', 'Aprilia', 'BMW', 'Suzuki', 'Yamaha', 'Ducati', 'Kawasaki', 'Triumph', 'KTM']
    ```

4. `remove(item)`: Removes the first occurrence of an item from the list.
    ```python
    bikes.remove('BMW')
    print(bikes)  # Output: ['Harley', 'Aprilia', 'Suzuki', 'Yamaha', 'Ducati', 'Kawasaki', 'Triumph', 'KTM']
    ```

5. `pop(index)`: Removes and returns the item at a specific position in the list.
    ```python
    popped_bike = bikes.pop(0)
    print(popped_bike)  # Output: 'Harley'
    print(bikes)  # Output: ['Aprilia', 'Suzuki', 'Yamaha', 'Ducati', 'Kawasaki', 'Triumph', 'KTM']
    ```

6. `index(item)`: Returns the index of the first occurrence of an item in the list.
    ```python
    print(bikes.index('Ducati'))  # Output: 3
    ```

7. `count(item)`: Returns the number of times an item appears in the list.
    ```python
    print(bikes.count('Suzuki'))  # Output: 1
    ```

8. `sort()`: Sorts the items in the list in ascending order.
    ```python
    bikes.sort()
    print(bikes)  # Output: ['Aprilia', 'Ducati', 'KTM', 'Kawasaki', 'Suzuki', 'Triumph', 'Yamaha']
    ```

9. `reverse()`: Reverses the order of items in the list.
    ```python
    bikes.reverse()
    print(bikes)  # Output: ['Yamaha', 'Triumph', 'Suzuki', 'Kawasaki', 'KTM', 'Ducati', 'Aprilia']
    ```

10. `clear()`: Removes all items from the list.
    ```python
    bikes.clear()
    print(bikes)  # Output: []
    ```

11. `copy()`: Returns a copy of the list.
    ```python
    bikes_copy = bikes.copy()
    print(bikes_copy)  # Output: ['Yamaha', 'Triumph', 'Suzuki', 'Kawasaki', 'KTM', 'Ducati', 'Aprilia']
    ```