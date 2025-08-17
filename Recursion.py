def F(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return F(n-1) + F(n-2)

# print( F(6))


class SinglyNode:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)

Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(6)

Head.next = A
A.next = B


def reverse(node):
    if not node:
        return

    reverse(node.next)
    print(node)

reverse(Head)

