print("name")  # printing a string


# ! Name "name" is not defined  [name-defined]

# print(name) # ? uncomment this line to see the error.


name: str = "Muhammad Ahmad Shoukat"

print(name)  # printing a string


# String Data type in Python


# boundaries of string

# 1. single quotes

# 2. double quotes

# 3. triple quotes


# 1. single quotes

name1: str = "Muhammad Ahmad Shoukat"

print(name)  # printing a string


# 2. double quotes

name2: str = "Muhammad Ahmad Shoukat"

print(name)  # printing a string


# 3. triple quotes

name3: str = """Muhammad Ahmad Shoukat"""

print(name)  # printing a string


# message: str = 'PIAIC Student Card \n father's Name' # ! SyntaxError: invalid syntax unterminated string

# print(message)  # printing a string


message: str = "PIAIC Student Card \n father's Name"

print(message)  # printing a string

# string concatenation


"a" + "b" + "c"  # "abc"

print("a" + "b" + "c")  # "abc"


print("a" + 7 * "b" + "c")


print("\n")


my_name: str = "Muhammad Ahmad Shoukat"

father_name: str = "Shoukat Ali"

education: str = "BSCS"

university: str = "Virtual University of Pakistan"

age: int = 24


card: str = (
    "PIAIC Student Card\n Student Name: "
    + my_name
    + "\n Father Name: "
    + father_name
    + "\n Education: "
    + education
    + "\n University: "
    + university
    + "\n Age: "
    # + age  # ! TypeError: can only concatenate str (not "int") to str | age is int | Unsupported operand types for +: 'str' and 'int'
    + str(age)
)


print(card)


print("\n")


# "\" Line Continuation Character


# print(7 + \

#       8 + \

#       9)


# card_with_line_continuation_character: str = "PIAIC Student Card\n Student Name: " + my_name\

#     + "\n Father Name: " + father_name\

#     + "\n Education: " + education


# Defining multi line string using triple quotes


multi_line_string: str = """PIAIC Student Card

Student Name: """

print(multi_line_string)


# f-string python 3.6


print(
    f"PIAIC Student Card\n Student Name: {my_name}\n Father Name: {father_name}\n Education: {education}"
)


multi_line_f_string: str = f"""PIAIC Student Card

Student Name: {my_name}

Father Name: {father_name}

Education: {education}
"""

print(multi_line_f_string)


# string_literal_card: str = f ` PIAIC Student Card

# Student Name: {my_name}

# Father Name: {father_name}

# Education: {education}

# ``


# f_string and jinja style formatting


# f_string

f"""

Student Name: {my_name}
"""


# jinja style formatting

"""

Student Name: {{my_name}}
"""


# String Formatting


# 1. % formatting

# 2. .format()

# 3. f-string


# String Methods and Attributes


# 1. len()

# 2. lower()

# 3. upper()

# 4. title()

# 5. count()

# 6. find()

# 7. replace()

# 8. strip()

# 9. split()


a: list[str] = [
    i for i in dir(str) if "__" not in i
]  # list of all methods and attributes of string data type

print(a)


# ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',

# 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',

# 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',

# 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',

# 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',

# 'title', 'translate', 'upper', 'zfill']


# Capitalize
galaxy: str = "andromeda galaxy"

print(galaxy.capitalize())  # Andromeda galaxy

# Casefold

print(galaxy.casefold())  # andromeda galaxy

# lower

print(galaxy.lower())  # andromeda galaxy

# lstrip and rstrip and strip - (left, right, both remove spaces)

import re  # regular expression

# remove prefix and suffix

url: str = "https://www.google.com"

print(url.removeprefix("https://"))  # www.google.com
