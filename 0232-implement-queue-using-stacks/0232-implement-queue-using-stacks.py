class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        # Always push new elements to the input stack
        self.input.append(x)

    def pop(self) -> int:
        # Ensure the output stack has the elements in FIFO order
        self._transfer()
        return self.output.pop()

    def peek(self) -> int:
        # Ensure the output stack has the elements in FIFO order
        self._transfer()
        return self.output[-1]

    def empty(self) -> bool:
        # Queue is empty if both stacks are empty
        return not self.input and not self.output

    def _transfer(self) -> None:
        # If the output stack is empty, move all elements from input to output
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())