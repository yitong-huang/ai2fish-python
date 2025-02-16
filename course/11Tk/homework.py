from tkinter import *

root = Tk()

root.title("我的窗口")
root.geometry("400x500")

def callback():
    print("你点了一下按钮")
#
b1 = Button(root, text="1", command=callback)
b1.pack(side="left")
#
b4 = Button(root, text="4", command=callback)
b4.pack(side="left")
#
b7 = Button(root, text="7", command=callback)
b7.pack(side="left")
#
mainloop()