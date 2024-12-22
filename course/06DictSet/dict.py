grade = {"huang": 90, "li": 80, "wang": 90}
print('grade["huang"]:', grade["huang"])

grade["xxx"] = 100
print("grade:", grade)

grade["huang"] = 95
print("grade:", grade)

# print(grade["yyy"])

print('grade.get("huang"):', grade.get("huang"))
print('grade.get("yyy"):', grade.get("yyy"))
print('grade.get("yyy", 0):', grade.get("yyy", 0))

print('"huang" in grade:', "huang" in grade)
print('"yyy" in grade:', "yyy" in grade)