complete = True # False
grade = 95


# 完成 而且按分数去分级
if complete:
    if grade > 90:
        print("A")
    elif grade > 80:
        print("B")
    else:
        print("C")
else:
    print("fail..")