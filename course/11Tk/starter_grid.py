from tkinter import *

root = Tk()

root.title("我的窗口")

# 回调函数
def callback():
    print("你点了一下按钮")

b1 = Button(root, text="1", command=callback)
b2 = Button(root, text="2", command=callback)
b3 = Button(root, text="3", command=callback)
b4 = Button(root, text="4", command=callback)
b5 = Button(root, text="5", command=callback)
b6 = Button(root, text="6", command=callback)
b7 = Button(root, text="7", command=callback)
b8 = Button(root, text="8", command=callback)
b9 = Button(root, text="9", command=callback)

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

b10 = Button(root, text="calculator", command=callback)
b10.grid(row=3, column=0, columnspan=3)
#
mainloop()