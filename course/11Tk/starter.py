from tkinter import *

# def main():
root = Tk()

root.title("计算器")
root.geometry("400x500")
root.resizable(True, False)

l1 = Label(root, text="xxx!")
l1.pack(side="top", anchor="w")

# 回调函数
def callback():
    print("你点了一下按钮")

b = Button(root, text="yyy", command=callback)
b.pack(side="top", pady=100)
# # # button.pack(side="bottom", anchor="w", expand=True)
# b.pack(pady=50, padx=10)
# #
# button1 = Button(root, text="按钮", command=callback)
# button1.pack()
#
mainloop()


# main()