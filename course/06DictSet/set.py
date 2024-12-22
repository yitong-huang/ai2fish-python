s = {1, 2, 3}
print(s)

s2 = set([4, 5, 6])
print(s2)

s = {1, 2, 3, 1, 2, 3}
print(s)

s.add(10)
print("s.add(10):", s)
s.add(3)
print("s.add(3):", s)

s.remove(3)
print("s.remove(3):", s)
