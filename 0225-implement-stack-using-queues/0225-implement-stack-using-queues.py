from collections import deque

class MyStack:
    def __init__(self):
        # We use a single deque to simulate both the queue and the stack
        self.q = deque()

    def push(self, x: int) -> None:
        # Add the new element to the back of the queue
        self.q.append(x)
        # Rotate the queue: move all elements except the newly added one to the back
        # This brings the new element to the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # The front of the queue is the top of the stack
        return self.q.popleft()

    def top(self) -> int:
        # The front of the queue is the top of the stack
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0