# Simple Caclulator
from typing import Union


def add(a: Union[int, float], b: Union[int, float]):
    return f"{a} + {b} = {a + b}"


def subtract(a: Union[int, float], b: Union[int, float]):
    return f"{a} - {b} = {a - b}"


def multiply(a: Union[int, float], b: Union[int, float]):
    return f"{a} * {b} = {a * b}"


def divide(a: Union[int, float], b: Union[int, float]):
    return f"{a} / {b} = {a / b}"


def calculator():
    print("Welcome to the calculator")
    print("Please enter the first number\t\n")
    a = float(input())
    print("Please enter the second number\t\n")
    b = float(input())
    print("Please enter the operation\n")
    operation = input("\t+, -, *, /\n")
    if operation == "+":
        print(add(a, b))
    elif operation == "-":
        print(subtract(a, b))
    elif operation == "*":
        print(multiply(a, b))
    elif operation == "/":
        print(divide(a, b))
    else:
        print("Invalid operation")


calculator()
