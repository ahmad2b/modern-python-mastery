# Defining a variable
name = "Pakistan"

# Printing the variable
print(name)

# Printing the type of variable
print(type(name))

# Printing the id of variable
print(id(name))

# Printing the dir of variable (methods and attributes)
print([i for i in dir(name) if "__" not in i])


# names: str = 700
# Incompatible types in assignment (expression has type "int", variable has type "str")

# print(name)
# print(type(name))
# print(id(name))


# Type `int`

print("--" * 20)  # Separator
print("Type `int`")
print("--" * 20)  # Separator
number: int = 700  # variable declaration
print(number)  # print variable
print(type(number))  # type of variable
print(id(number))  # memory address
print(
    [i for i in dir(number) if "__" not in i]
)  # to check all the methods & attributes of a class
print("--" * 20)  # Separator
print("\n")

# Type `float`

print("--" * 20)  # Separator
print("Type `float`")
print("--" * 20)  # Separator
decimal: float = 70.73  # variable declaration
print(decimal)  # print variable
print(type(decimal))  # type of variable
print(id(decimal))  # memory address
print(
    [i for i in dir(decimal) if "__" not in i]
)  # to check all the methods & attributes of a class
print("--" * 20)  # Separator
print("\n")

# Type `bool`

print("--" * 20)  # Separator
print("Type `bool`")
print("--" * 20)  # Separator
boolean: bool = True  # variable declaration
print(boolean)  # print variable
print(type(boolean))  # type of variable
print(id(boolean))  # memory address
print(
    [i for i in dir(boolean) if "__" not in i]
)  # to check all the methods & attributes of a class
print("--" * 20)  # Separator
print("\n")

# Type `list`

print("--" * 20)  # Separator
print("Type `list`")
print("--" * 20)  # Separator
long: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # variable declaration
print(long)  # print variable
print(type(long))  # type of variable
print(id(long))  # memory address
print(
    [i for i in dir(long) if "__" not in i]
)  # to check all the methods & attributes of a class
print("--" * 20)  # Separator
print("\n")


# Type `tuple`

print("--" * 20)  # Separator
print("Type `tuple`")
print("--" * 20)  # Separator

short: tuple[int, str, float, bool] = (1, "2", 3.0, True)  # variable declaration
print(short)  # print variable
print(type(short))  # type of variable
print(id(short))  # memory address
print(
    [i for i in dir(short) if "__" not in i]
)  # to check all the methods & attributes of a class
print("--" * 20)  # Separator
print("\n")


# Type `any`

print("--" * 20)  # Separator
print("Type `any`")
print("--" * 20)  # Separator

from typing import Any

any_type: Any = 1  # variable declaration
print(any_type)  # print variable
print(type(any_type))  # type of variable
print(id(any_type))  # memory address

any_type = "2"  # variable declaration
print(any_type)  # print variable
print(type(any_type))  # type of variable
print(id(any_type))  # memory address
