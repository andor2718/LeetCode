# https://leetcode.com/problems/design-linked-list/

class MyLinkedList:
    class ListNode:
        def __init__(self, val: int = 0, next=None, prev=None):
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if not 0 <= index < self.size:
            return -1
        dist_from_head = index
        dist_from_tail = self.size - 1 - index
        if dist_from_head <= dist_from_tail:
            curr = self.head
            for _ in range(dist_from_head):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(dist_from_tail):
                curr = curr.prev
        return curr.val

    def addAtHead(self, val: int) -> None:
        if self.size == 0:
            self.head = self.tail = self.ListNode(val=val)
        else:
            new_node = self.ListNode(val=val, next=self.head)
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.head = self.tail = self.ListNode(val=val)
        else:
            new_node = self.ListNode(val=val, prev=self.tail)
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if not 0 <= index <= self.size:
            return
        if index == 0:
            return self.addAtHead(val)
        elif index == self.size:
            return self.addAtTail(val)
        else:
            dist_from_head = index
            # NOTE: No -1 here, because we always insert before index.
            dist_from_tail = self.size - index
            if dist_from_head <= dist_from_tail:
                curr = self.head
                for _ in range(dist_from_head - 1):
                    curr = curr.next
                new_node = self.ListNode(val=val, next=curr.next, prev=curr)
                curr.next.prev = new_node
                curr.next = new_node
            else:
                curr = self.tail
                for _ in range(dist_from_tail - 1):
                    curr = curr.prev
                new_node = self.ListNode(val=val, next=curr, prev=curr.prev)
                curr.prev.next = new_node
                curr.prev = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if not 0 <= index < self.size:
            return
        if self.size == 1:
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            dist_from_head = index
            dist_from_tail = self.size - 1 - index
            if dist_from_head <= dist_from_tail:
                curr = self.head
                for _ in range(dist_from_head - 1):
                    curr = curr.next
                curr.next = curr.next.next
                curr.next.prev = curr
            else:
                curr = self.tail
                for _ in range(dist_from_tail - 1):
                    curr = curr.prev
                curr.prev = curr.prev.prev
                curr.prev.next = curr
        self.size -= 1
