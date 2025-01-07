grade = [["huang", 90], ["li", 80], ["wang", 95], ["zhao", 55]]

# grade这个数组，每个元素是另一个数组
# 内部数组第一个元素是名字，第二个元素是分数
# 要求按分数计算等级，>=90:A，>=80 <90:B, >=60 <80:C，<60:D
# 并且把等级作为内部元素的第一个元素放进数组里

# 预期的结果
# grade = [["A", "huang", 90], ["B", "li", 80],
# ["A", "wang", 95], ["D", "zhao", 55]]

for g in grade:
    # print(g[0], g[1])
    if g[1] >= 90:
        g.insert(0, "A")
    elif g[1] >= 80:
        g.insert(0, "B")
    elif g[1] >= 60:
        g.insert(0, "C")
    else:
        g.insert(0, "D")

print(grade)