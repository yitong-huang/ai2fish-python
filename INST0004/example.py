def binarySearch(arr, target, first, last):
    if first > last:
        return -1
    mid = (first + last) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binarySearch(arr, target, mid + 1, last)
    else:
        return binarySearch(arr, target, first, mid - 1)


array = [-1, 1, 3, 5, 6, 9, 12]
print(binarySearch(array, 5, 0, len(array)-1))
print(binarySearch(array, 8, 0, len(array)-1))