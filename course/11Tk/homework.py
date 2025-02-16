from tkinter import *

root = Tk()

root.title("我的窗口")
root.geometry("400x500")

def callback():
    print("你点了一下按钮")
#
b1 = Button(root, text="1", command=callback, height=2, width=5)
b1.pack(side="top", anchor="w", pady=(150,0))
#
b4 = Button(root, text="4", command=callback, height=2, width=5)
b4.pack(side="top", anchor="w")
#
b7 = Button(root, text="7", command=callback, height=2, width=5)
b7.pack(side="top", anchor="w")
#
mainloop()