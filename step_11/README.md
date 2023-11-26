# try-except

* Pass by reference vs Pass by Value
* Mutable and Immutable Variables
* Runtime Error Classes
* Try-Except-Else-Finally Block

## Pass by Reference vs Pass by Value

### Pass by Reference

If you pass immutable arguments like integers, strings or tuples to a function, the passing acts like pass-by-value. The function gets a copy of the arguments and changes that the function makes to the arguments do not get reflected in the original variable.

```python
def updateNumber(num: int):
    print("Number before change: ", id(num))
    num += 10
    print("Number after change: ", id(num))

n = 15
print("Number before function call", id(n))
updateNumber(n)
print("Number after function call", id(n))
```

### Pass by Value

If you pass mutable arguments like lists, dictionaries or sets to a function, the function gets a reference to the argument. So, changes made to the argument change the original variable.

```python
def updateList(myList: list):
    print("List before change: ", id(myList))
    myList.append(20)
    print("List after change: ", id(myList))

lst = [10, 20, 30]
print("Number before function call", id(lst))
updateList(lst)
print("Number after function call", id(lst))
```

## Mutable and Immutable Variables

Variables in Python can be either mutable or immutable.

* **Mutable types** can be changed after they are created. Examples include lists, dictionaries and sets.
* **Immutable types** cannot be changed after they are created. Examples include integers, floats, strings, and tuples.

### Example: Mutable Type
```python
my_list = [1, 2, 3]
print("Before modification: ", my_list, "id: ", id(my_list))
my_list.append(4)
print("After modification: ", my_list, "id: ", id(my_list))
```

In this example, the list `my_list` is modified in place, and its `id` remains the same.

### Example: Immutable Type

```python
my_string: str = "hello"
print("Before modification: ", my_string, "id: ", id(my_string))
my_string = my_string + " world"
print("After modification: ", my_string, "id: ", id(my_string))
```

In this example, when we modify `my_string`, a new string object is created, and the `id` of `my_string` changes.

## Runtime Error Classes

Runtime errors in Python are also known as exceptions. 

They occur while the program is running if the interpreter encounters an error condition that it can't recover from. Python has several built-in exceptions, such as 
* `TypeError`, 
* `ValueError`, 
* `IndexError`, 
* `ZeroDivisionError`, 
* etc.

```python
# ZeroDivisionError
try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# TypeError
try:
    '2' + 2
except TypeError:
    print("You can't add a string to an integer!")

# ValueError
try:
    int('python')
except ValueError:
    print("You can't convert 'python' to an integer!")

# IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("That index is not in the list!")

# KeyError
try:
    my_dict = {'name': 'Python'}
    print(my_dict['age'])
except KeyError:
    print("That key is not in the dictionary!")
```

## Try-Except-Else-Finally Block

The `try-except-else-finally` block is a control flow structure in Python used for exception error handling. Here's a brief explanation:

* `try`: This block contains the code that might raise an exception. If an exception occurs, the rest of the try block is skipped and the `except` block is executed.
* `except`: This block contains the code that handles the exception. You can specify different handlers for different execeptions.
* `else`: This block contains the code that will be executed if the `try` block doesn't raise any exceptions. It is optional.
* `finally`: This block contains the code that will always be executed, whether an exception has occurred or not. It is optional.

**Example 1**:
```python
try:
    # Code that may raise an exception
    x = 1 / 0
except ZeroDivisionError:
    # Handle the exception
    print("You can't divide by zero!")
else:
    # Code to run if no exception was raised in the try block
    print("No exceptions were raised.")
finally:
    # Code to run no matter what happens
    print("This will always run.")
```

**Example 2**:
```python
try:
    # Code that may raise an exception
    numerator = 10
    denominator = 2
    result = numerator / denominator
except ZeroDivisionError as e:
    # Handle the exception
     print("Caught a ZeroDivisionError:", str(e))
else:
    # Code to run if no exception was raised in the try block
    print("Division successful:", result)
finally:
    # Code to run no matter what happens
    print("This block is always executed")
```