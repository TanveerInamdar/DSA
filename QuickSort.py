A = [-5,3,2,1,5,-3,2,-6,-7]
# Time = O(n logn)

def quicksort(arr):
    if len(arr)<= 1:
        return arr
    p = arr[-1]

    L = [x for x in arr[:-1] if x <= p]
    R = [x for x in arr[:-1] if x > p]


    L = quicksort(L)
    R = quicksort(R)

    return L + [p] + R

P = quicksort(A)

print(P)
