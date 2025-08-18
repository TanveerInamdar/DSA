A = [-3, -1, 0, 1, 4,7]

#Traditional Binary Search Algorithm:
def BinarySearch(arr, target):
    N = len(arr)

    L = 0
    R = N-1

    while L <= R:
        mid = (L + R) // 2

        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            R = mid -1
        else:
            L = mid + 1


    return False

print(BinarySearch(A, 7))