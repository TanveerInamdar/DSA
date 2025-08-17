#Stacks and Queues
#Stacks LIFO
stk = []
#append to it:

stk.append(5)
stk.append(4)
stk.append(3)


x= stk.pop()

print(x)

print(stk)

print(stk[-1])

if stk: #if empty
    print(True)

stk.pop()
# stk.pop()
#stk.pop() # error for empty stack
print(stk)
#Queue - FIFO

from collections import deque

q = deque()
print(q)

# enqueue

q.append(5)
q.append(6)
print(q)

#deque or pop left

q.popleft() # We dont write just pop because that would be a stack - specify right or left

print(q)
print(q[0])  #peek from left operation - O(1)
print(q[-1]) # peek from right operation - O(1)


