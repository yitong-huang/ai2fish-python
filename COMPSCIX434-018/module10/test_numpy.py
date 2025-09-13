import numpy as np

l1 = [1, 2, 3, 20, 40]
l2 = [1, 2, 3, 20, 40]
l3 = l1 + l2
print(l3)



a = np.array([1, 2, 3, 20, 40])
b = np.array([2, 5, 9, 20, 30])
print(a + b)
print(a * 2 + 10)
print(a == 20)
print(a > 20)
print(a * b)
#
print(np.sum(a))
print(np.prod(a))
print(np.max(a))
print(np.min(a))
print(np.std(a))
print(np.median(a))
print(np.average(a))
print(np.mean(a))

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(a * b)
print(a.dot(b))
print(np.dot(a, b))

# l = [1, 2 ,5, 60]   # [2, 4, 10, 120]
# result = []
# for item in l:
#     result.append(item * 2)
# l = l * 2
# print(result)
# l2d = [[1, 2, 3], [3, 6, 20]]
# l3d = [[[1,2, 3], [4, 5, 6]], [[1, 2, 4], [9, 10 ,10]]]