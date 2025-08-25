f = open('data.txt')  # read
l = []

for line in f:
    l.append(int(line))

print(l)

s = 0
for n in l:
    s += n
mean = s / len(l)
print(mean)

v = 0
for n in l:
    v += ((n - mean) ** 2) / len(l)

print(v)
f.close()

# f = open('data.txt', 'r')
# s = 0
# t = 0
# for line in f:
#     t += 1
#     s += int(line)   # s = s + int(line)
#
# mean = s / t
# print(mean)
# f.close()
#
# f = open('data.txt', 'r')
# for line in f:
#     s += int(line)

a = 2
print(a ** 3)