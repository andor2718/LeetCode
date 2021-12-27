# https://leetcode.com/problems/flatten-nested-list-iterator/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#     def isInteger(self) -> bool:
#         """
#         @return True if this NestedInteger holds a single integer, rather than a nested list.
#         """
#
#     def getInteger(self) -> int:
#         """
#         @return the single integer that this NestedInteger holds,
#         if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         """
#
#     def getList(self) -> [NestedInteger]:
#         """
#         @return the nested list that this NestedInteger holds,
#         if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nums = self._flatten(nestedList)
        self.pos = 0

    def next(self) -> int:
        num = self.nums[self.pos]
        self.pos += 1
        return num

    def hasNext(self) -> bool:
        return self.pos < len(self.nums)

    def _flatten(self, nestedList: [NestedInteger]) -> list[int]:
        result = list()
        for item in nestedList:
            if item.isInteger():
                result.append(item.getInteger())
            else:
                result.extend(self._flatten(item.getList()))
        return result

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
