class MinStack:

    def __init__(self):
        # Stack stores tuples of (value, current_minimum)
        self.stack = []

    def push(self, val: int) -> None:
        # If the stack is empty, the current minimum is the value itself
        if not self.stack:
            self.stack.append((val, val))
        else:
            # The new minimum is the smaller of the new value and the previous minimum
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self) -> None:
        # Simply pop the top tuple
        self.stack.pop()

    def top(self) -> int:
        # The top value is the first element of the top tuple
        return self.stack[-1][0]

    def getMin(self) -> int:
        # The current minimum is the second element of the top tuple
        return self.stack[-1][1]