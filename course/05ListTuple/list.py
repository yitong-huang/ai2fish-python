students = ["huang", "li", "wang"]

print(len(students))

print(students[0])
print(students[1])
print(students[2])
#print(students[3])

print(students[-1])
print(students[-2])
print(students[-3])
#print(students[-4])

students.append("xxx")
print("append xxx:", students)
students.append("huang")
print("append huang:", students)


students.insert(1, "yyy")
print("insert yyy:", students)

students.pop()
print("pop:", students)

students.pop(1)
print("pop:", students)

print(students * 2)