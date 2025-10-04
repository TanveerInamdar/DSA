# Parent is smaller than children.
# Left child - 2i + 1 right child - 2i + 2
# Extract min - O(log n)
# Insert = O(log n)
# heap peek - Gets the minimum of the heap - O(1) as its the first element.
# Heap Sort -  Repeatedly pop off the minimum - O (N log n)


# Build Min Heap
A = [-4,-3,1,2,5,8,10,9,12]

import heapq
heapq.heapify(A)
print(A)