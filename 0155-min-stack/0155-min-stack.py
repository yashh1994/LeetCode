class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
            self.stack.append(val)
        else:
            if val < self.min:
                self.stack.append(2 * val - self.min)
                self.min = val
            else:
                self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        top = self.stack.pop()
        if top < self.min:
            self.min = 2 * self.min - top
        if not self.stack:
            self.min = float('inf')

    def top(self) -> int:
        if not self.stack:
            return -1
        top = self.stack[-1]
        if top < self.min:
            return self.min
        return top

    def getMin(self) -> int:
        return self.min
