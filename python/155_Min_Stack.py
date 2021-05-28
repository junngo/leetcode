class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return  min([i for i in self.stack])

if __name__ == "__main__":
    minStack = MinStack();
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())   # return -3
    minStack.pop()
    print(minStack.top())      # return 0
    print(minStack.getMin())   # return -2
