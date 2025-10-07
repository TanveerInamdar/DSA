A = [5,3,2,1,5,3,2,6,7]

#Time - O(K+N) where K is the max val. Good algo for arrays where highest val is low.

def countingsort(arr):
    n = len(arr)
    maxx = max(arr)
    counts = [0] * (maxx+1)

    for x in arr:
        counts[x] += 1

    i = 0
    for c in range(maxx+1):
        while counts[c] > 0:

            arr[i] = c
            i += 1
            counts[c] -= 1
countingsort(A)
print(A)
