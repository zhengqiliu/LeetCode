class Node:
    def __init__(self, val, min, next = None):
        self.val = val
        self.min = min
        self.next = next

class MinStack:
           

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = Node('*', float('inf'))

    def push(self, x: int) -> None:
        new_node = Node(x, min(self.head.min, x), self.head)
        self.head = new_node

    def pop(self) -> None:
        if self.head.val == '*':
            return
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
