### 1 ###

# s = " Programming Python"
#
# # a.
# print(s[1])
# print(s[13])
# print(s[-6])
#
# # b.
# print(s[13:])
# print(s[13:19])
# print(s[-6:])


# ### 2 ###

# s = "   I am    Programming    Python!       "
# s = s.replace("       ", "")
# s = s.replace("   ", "")
# print(s)


### 3 ###
#
# length = 5
# width = 2.5
# height = 2.73
#
# volume = length * width * height
#
# s = f"The box has a length: {length}, width: {width} and height: {height}. The volume is: {volume:.7f}."
# print(s)


# ### 4 ###

# a.
# mylist = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in range(len(mylist)):
#     print(i)
#     mylist[i] = mylist[i] + mylist[i]
# del mylist[7]
# print(mylist)
#
# # b.
# mylist = [1, 2, 3, 4, 5, 6, 7, 8]
# newList = []
# newList.append(mylist[0] * 2)
# newList.append(mylist[1] * 2)
# newList.append(mylist[2] * 2)
# newList.append(mylist[3] * 2)
# newList.append(mylist[4] * 2)
# newList.append(mylist[5] * 2)
# newList.append(mylist[6] * 2)
# newList.append(mylist[7] * 2)
# newList.remove(newList[7])
# print(newList)


# # ### 5 ###
t = ('anita', 0, 'brandon', 'chitra', 5, 7)

# a.
l = list(t)
for i in range(len(l)):
    if isinstance(l[i], str):
        l[i] = l[i].capitalize()

# b.
for i in range(len(l)-1, -1, -1):
    if isinstance(l[i], int):
        l.remove(l[i])

# c.
t = tuple(l)
print(t)
