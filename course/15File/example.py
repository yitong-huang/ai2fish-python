# 文件操作
# 对象object
f = open('test', 'r')

# l = f.readline()
# print(l)

print("======")

# a = f.read()
# print(a)

print("======")

s = 0
for line in f:
    s += int(line)   # s = s + int(line)
print(s)

print("======")

# f.write("111")

f.close()

# w -> write
f = open('test', "w")
f.write("222\n")
f.write("11")
f.write("333")
f.close()

# a -> append
f = open('test2', "a")
f.write("\n33334444")
f.write("\n1111")
f.close()


# operation system
import os
os.remove('test2')