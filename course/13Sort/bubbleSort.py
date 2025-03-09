from wheel.macosx_libfile import swap32


def bubble_sort(arr):
    n = len(arr)

    # swapped = False
    for i in range(n):
        # 标记是否发生了交换
        swapped = False
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