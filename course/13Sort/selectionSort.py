def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # 假设当前未排序部分的第一个元素是最小值
        min_idx = i
        # 在未排序部分中查找最小值的索引
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 将最小值与未排序部分的第一个元素交换
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 示例
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)  # 输出: [11, 12, 22, 25, 64]