from typing import Union

PerType = Union[float, int]

percentages: list[PerType] = [88, 99.9, 50, 51, 65, 70, 66.7]

print(type(percentages))

grades: list[str] = []

for per in percentages:
    grade: str = ""

    if (per >= 0) and (per < 33):
        grade = "F"
    elif (per >= 33) and (per < 45):
        grade = "D"
    elif (per >= 45) and (per < 60):
        grade = "C"
    elif (per >= 60) and (per < 75):
        grade = "B"
    elif (per >= 75) and (per <= 85):
        grade = "A"
    elif (per >= 85) and (per < 100):
        grade = "A+"

    grades.append(grade)

print(percentages)
print(grades)
