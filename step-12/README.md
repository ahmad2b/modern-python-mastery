# Python Error Handling and File Handling

* Error Handling
  * Try-Except-Else
  * Multiple Except Blocks
  * Creating Custom Errors
  * Dynamic Error Handling
* File Handling with Access Modifiers
  * Read More (r)
  * Read and Write Mode (r+)
  * Write Mode (w)
  * Write and Read Mode (w+)
  * Append Mode (a)
  * Append and Read Mode (a+)
  * Binary Read Mode (rb)
* Reading Files
  * Reading CSV Files
  * Reading PDF Files
  * Reading Excel Files
  * Reading Audio Files

## Error Handling

### Try-Except-Else

A mechanism to catch and handle exceptions gracefully.

**Syntax**: 
```python
try:
    # code that may raise an exception
except ExceptionType:
    # code to handle the exception
else:
    # code to run if no exception was raised
```

### Multiple Except Blocks

Allows handling different types of exceptions differently.

**Syntax**:
```python
try:
    # code that may raise an exception
except ExceptionType1:
    # handle ExceptionType1
except ExceptionType2:
    # handle ExceptionType2
```

### Creating Custom Errors

You can define your own exception types or custom classes for specific error conditions by inheriting from the base `Exception` class.

**Syntax**:
```python
class MyException(Exception):
    pass
```

**Example**:
```python
class NegativeValueError(Exception):
    def __str__(self) -> str:
        return "Value cannot be negative"

def sqrt(value: float) -> float:
    if value < 0:
        raise NegativeValueError()
    return value **0.5

```

### Dyanmic Error Handling

You can handle errors dynamically by capturing the exception and analyzing it.

**Syntax**:
```python
try:
    # code that may raise an exception
except Exception as e:
    # handle the exception with the instance 'e'
```

## File Handling with Access Modifiers

### Read Mode (r)

Opens a file for reading.

```python
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)
```

### Read and Write Mode (r+)

Opens a file for reading and writing.

```python
with open('file.txt', 'r+') as f:
    content = f.read()
    print(content)
    f.write("New line")
```

### Write Mode (w)

Opens a file for writing, creates the file if it does not exist, and truncates the file if it exists.

```python
with open('file.txt', 'w') as f:
    f.write("Hello, World!")
```

### Write and Read Mode (w+)

Opens a file for writing and reading.

```python
with open('file.txt', 'w+') as f:
    f.write("Hello, World!")
    f.seek(0)
    content = f.read()
    print(content)
```

### Append Mode (a)

Opens a file for appending, creates the file if it does not exist.

```python
with open('file.txt', 'a') as f:
    f.write("Appending line")
```

### Append and Read Mode (a+)

Opens a file for appending and reading.

```python
with open('file.txt', 'a+') as f:
    f.write("Appending line")
    f.seek(0)
    content = f.read()
    print(content)
```

### Binary Read Mode (rb)

Opens a file in binary read mode.

```python
with open('file.txt', 'rb') as f:
    content = f.read()
    print(content)
```

## Reading Files

### Reading CSV Files

You can use the csv module to read CSV files.

```python
import csv

with open('file.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### Reading PDF Files

You can use the `PyPDF2` library to read PDF files.

```python
import PyPDF2

with open('file.pdf', 'rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    text = reader.getPage(0).extractText()
    print(text)
```

### Reading Excel Files

You can use the `openpyxl` library to read Excel files.

```python
import openpyxl

wb = openpyxl.load_workbook('file.xlsx')
sheet = wb.active
cell = sheet['A1']
print(cell.value)
```

### Reading Audio Files

You can use the pydub library to read audio files.

```python
from pydub import AudioSegment

audio = AudioSegment.from_file("file.mp3")
print("Channels:", audio.channels)
print("Sample Width:", audio.sample_width)
print("Frame Rate:", audio.frame_rate)
print("Frame Width:", audio.frame_width)
print("Length (ms):", len(audio))
print("Frame Count:", audio.frame_count())
```