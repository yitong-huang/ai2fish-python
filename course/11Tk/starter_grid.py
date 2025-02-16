from tkinter import *

root = Tk()

# 回调函数
def callback():
    print("你点了一下按钮")

for i in range(12):  # (0, 1, 2 ... 11)
    # 创建一个按钮
    b = Button(root, text=(i+1), command=callback)
    # 按钮.grid(row= ?, column= ?)
    b.grid(row= i // 3, column= i % 3)

#
mainloop()