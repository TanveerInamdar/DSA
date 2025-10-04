A = [-5,3,2,1,5,-3,2,-6, -7]


def mergesort(arr):
    n = len(arr)

    if n == 1:
        return arr

    m = n // 2
    l = arr[:m]
    r = arr[m:]

    l = mergesort(l)
    r = mergesort(r)
    L,R = 0,0
    L_len = len(l)
    R_len = len(r)

    sortarr = [0] *n
    i = 0

    while L < L_len and R < R_len:
        if l[L] < r[R]:
            sortarr[i] = l[L]
            L +=1
        else:
            sortarr[i] = r[R]
            R += 1
        i += 1
    while L < L_len:
        sortarr[i] = l[L]
        L += 1
        i += 1
    while R < R_len:
        sortarr[i] = r[R]
        R +=1
        i +=1

    return sortarr

A = mergesort(A)
print(A)


