def rotate_left(arr, d):
    d %= len(arr)
    print(9%8)
    return arr[d:] + arr[:d]


arr1 = [1, 2, 3, 4, 5, 6]
d1 = 2
print(rotate_left(arr1, d1))  # Output: [3, 4, 5, 6, 1, 2]

arr2 = [1, 2, 3]
d2 = 4
print(rotate_left(arr2, d2))  # Output: [2, 3, 1]
