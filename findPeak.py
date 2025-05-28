def findPeak(arr):
    low = 0
    high = len(arr) - 1
    offset = 1

    while low < high:
        mid = (low + high) // 2
        offset = 1
        while mid+offset < len(arr) and arr[mid] == arr[mid+offset]:
            offset += 1
        if arr[mid] > arr[mid + offset]:
            high = mid
        else:
            low = mid + 1

    return arr[low]


arr = [1,4,4,4,5,7,7,7,9,7,4,4,4,3,1]
print(findPeak(arr))

# arr = [1, 2, 3, 4, 5, 6,7,5, 4, 3, 2, 1]
# print(findPeak(arr))