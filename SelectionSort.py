A = [-5,3,2,1,5,-3,2,-6, -7]

def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i+1,n):
            if arr[j] < arr[mini]:
                mini = j

        arr[i], arr[mini] = arr[mini], arr[i]
SelectionSort(A)
print(A)

