# Python Looping and Input Techniques

* While Loop
* For Loop
* Control Statements
  * Break
  * Continue
  * Pass
* Input Function
* Command Line Arguments (sys.argv)
* Examples

## While Loop

A `while` loop in Python repeatedly executes a target statement as long as a given condition is true.

**Syntax:**
```python
while condition:
    statement
```

**Example**
```python
i: int = 0
while i < 5:
    print(i)
    i += 1
```

## For Loop

The `for` loop in Python is used to iterate over a sequence (`list`, `tuple`, `string`) or other iterable objects.

**Syntax:**
```python
for element in sequence:
    statement
```

**Example**
```python
for i in range(5):
    print(i)
```

## Control Statements

Control statements in Python are used to control the order of execution of the program based on the values and logic.

### Break

The `break` statement terminates the loop statement and transfers execution to the statement immediately following the loop.

**Syntax:**
```python
for element in sequence:
    if condition:
        break
```

**Example**
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

### Continue

The continue statement in Python returns the control to the beginning of the while loop or for loop.


**Syntax:**
```python
for element in sequence:
    if condition:
        continue
    statement
```

**Example**
```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

### Pass

The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.

**Syntax:**
```python
if condition:
    pass
```

**Example**
```python
for i in range(5):
    if i == 3:
        pass
    print(i)
```

## Input Function

The input() function allows user input.

**Syntax:**
```python
input(prompt)
```

**Example**
```python
name = input("Enter your name: ")
print("Hello, " + name)
```

## Command Line Arguments (sys.argv)

Command line arguments are parameters supplied to the program when it is invoked. `sys.argv` is a list in Python, which contains the command-line arguments passed to the script.

**Syntax:**
```python
import sys
print(sys.argv)
```

**Example**
```python
# Save this as test.py
import sys
for i in range(len(sys.argv)):
    if i == 0:
        print("Function name: %s" % sys.argv[0])
    else:
        print("%d. argument: %s" % (i,sys.argv[i]))
```