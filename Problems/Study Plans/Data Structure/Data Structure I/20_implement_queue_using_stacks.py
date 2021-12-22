# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    def __init__(self):
        self.in_stack = list()
        self.out_stack = list()

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._populate_outs()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._populate_outs()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _populate_outs(self) -> None:
        if self.out_stack:
            return  # It's populated already
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
