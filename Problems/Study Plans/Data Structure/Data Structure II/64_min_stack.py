# https://leetcode.com/problems/min-stack/

class MinStack:
    class StackElement:
        def __init__(self, val, curr_min):
            self.val = val
            self.curr_min = curr_min

    def __init__(self):
        self.elements = list()

    def push(self, val: int) -> None:
        if not self.elements:
            curr_element = self.StackElement(val, val)
        else:
            curr_element = self.StackElement(val, min(val, self.getMin()))
        self.elements.append(curr_element)

    def pop(self) -> None:
        self.elements.pop()

    def top(self) -> int:
        top_element = self.elements[-1]
        return top_element.val

    def getMin(self) -> int:
        top_element = self.elements[-1]
        return top_element.curr_min
