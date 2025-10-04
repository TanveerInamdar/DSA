# Parent is smaller than children.
# Left child - 2i + 1 right child - 2i + 2
# Extract min - O(log n)
# Insert = O(log n)
# heap peek - Gets the minimum of the heap - O(1) as its the first element.
# Heap Sort -  Repeatedly pop off the minimum - O (N log n)


# Build Min Heap
A = [-4,3,1,0,2,5,10,8,12,9]

import heapq
heapq.heapify(A)
#print(A)

# Heap Push - Insert element into heap
#Time - O(log n)

heapq.heappush(A, 4)


minn = heapq.heappop(A) # heapq only supports a min Heap not a Max Heap

# print(A, minn)
# print(A)

#Heap sort
#Time: O(n logn) - Space - O(n)
#NOTE - O(1) is possible via swapping but is complex so I am not doing it rn.

def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n

    for i in range(n):
        mini = heapq.heappop(arr)
        new_list[i] = mini

    return new_list

#print(heapsort([1,3,5,7,9,2,4,6,8,0]))

#Max heap


