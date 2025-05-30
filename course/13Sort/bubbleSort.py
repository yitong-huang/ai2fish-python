def bubble_sort(arr):
    n = len(arr)

    # swapped = False
    for i in range(n):
        # 标记是否发生了交换
        swapped = False
        # i表示已经有多少个值排好序（排到了最后面），对应gif图的橘黄色
        # n-i就是不再需要去处理这些排好序的数字
        # -1是因为后面if的比较是arr[j]和arr[j+1]，
        # 也就是说处理倒数第二个数字的时候就把最后一个数字比较了，所以-1，不需要处理最后一个数
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                # 交换位置
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # 如果没有发生交换，说明列表已经有序，提前退出
        if not swapped:
            print("break", i)
            break
    return arr

# 示例
arr = [5, 3, 8, 4, 6]  # list
sorted_arr = bubble_sort(arr)
print(sorted_arr)