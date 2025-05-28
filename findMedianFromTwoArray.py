
def findMedianFromTwoArray(arr1,arr2):
    if len(arr1) == 0 and len(arr2) == 0:
        return 0
    lengthOfArray = len(arr1)+len(arr2)
    medianCursor = lengthOfArray//2
    isEven = (lengthOfArray % 2 == 0)
    prevVal = currVal = 0
    cursor = 0
    ipointer = jpointer = 0
    
    while cursor <= medianCursor:
        prevVal = currVal
        if ipointer < len(arr1) and (jpointer >= len(arr2) or arr1[ipointer] < arr2[jpointer]):
            currVal = arr1[ipointer]
            ipointer += 1
        else:
            currVal = arr2[jpointer]
            jpointer += 1
        
        cursor += 1
    if isEven:
        return (prevVal + currVal)/2
    else:
        return currVal
            
        


# Sorted Array 1
arr1 = [1, 3, 5, 7, 9]

# Sorted Array 2
arr2 = [2, 4, 6, 8, 10,11]

print(findMedianFromTwoArray(arr1,arr2))

