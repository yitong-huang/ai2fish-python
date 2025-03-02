from tkinter import *
from functools import partial

root = Tk()


# 回调函数
def callback(key):
    print("你点了一下按钮" + key)


for c in range(3):  # 0, 1, 2
    for r in range(4):  # 0, 1, 2, 3 row:2
        # 0, 1, 2 column:2
        b = Button(root, command=partial(callback, "({},{})".format(r, c)), text="({},{})".format(r, c))
        b.grid(column=c, row=r)

# 100
# 1  2  3  ... 10
# 11 12 13 ... 20
# ...
# 91 92 93 ... 100

# 3 4 5
# 3 // 3  1
# 3 % 3   0
# 4 // 3  1
# 4 % 3   1
# 5 // 3  1
# 5       2
mainloop()
