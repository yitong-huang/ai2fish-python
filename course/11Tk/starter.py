from tkinter import *

root = Tk()

root.title("我的窗口")
root.geometry("400x500")
root.resizable(True, True)

l1 = Label(root, text="Hello, Tkinter!")
l1.pack()
#
# 回调函数
def callback():
    print("你点了一下按钮")
#
b = Button(root, text="按钮", command=callback)
# b.pack(fill="x")
# # button.pack(side="bottom", anchor="w", expand=True)
b.pack(pady=50, padx=10)
#
button1 = Button(root, text="按钮", command=callback)
button1.pack()
#
mainloop()