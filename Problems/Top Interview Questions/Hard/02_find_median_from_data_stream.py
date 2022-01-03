# https://leetcode.com/problems/find-median-from-data-stream/

import heapq


class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap and not self.max_heap:
            # Initialize min_heap with the first element of data stream
            self.min_heap.append(num)
        elif num >= self.findMedian():
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > len(self.max_heap) + 1:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        else:
            heapq.heappush(self.max_heap, -num)
            if len(self.max_heap) > len(self.min_heap):
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            # NOTE: Items in max_heap are negated, hence the subtraction
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return self.min_heap[0]
