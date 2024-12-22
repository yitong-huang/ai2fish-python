students = ["huang", "li", "wang"]
for student in students:
    print(student)

levels = ("a", "b", "c", "d")
for level in levels:
    print(level)

for i, student in enumerate(students):
    print(i, student)

grades = {"huang": 80, "li": 70, "wang": 90}
for name in grades:
    print(name, grades[name])

for name, grade in grades.items():
    print(name, grade)

for c in "hello world":
    print(c)