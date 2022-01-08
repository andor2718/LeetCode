# https://leetcode.com/problems/lru-cache/

from __future__ import annotations

from typing import Optional


class Node:
    def __init__(self, key: int = 0, val: int = 0,
                 next: Optional[Node] = None, prev: Optional[Node] = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._lut = dict()
        self._dll_head = None
        self._dll_tail = None

    def _dll_pop(self, node: Node) -> None:
        if node.prev and node.next:  # Node is between head and tail
            node.prev.next, node.next.prev = node.next, node.prev
        elif not node.prev and not node.next:  # Only node
            self._dll_head = self._dll_tail = None
        elif node.prev:  # Tail node, prev exists
            self._dll_tail = node.prev
            self._dll_tail.next = None
        else:  # Head node, next exists
            self._dll_head = node.next
            self._dll_head.prev = None

    def _dll_tail_insert(self, node: Node) -> None:
        node.next = None
        if self._dll_tail:  # Tail exists
            node.prev = self._dll_tail
            self._dll_tail.next = node
            self._dll_tail = node
        else:  # Doubly linked list is empty
            node.prev = None
            self._dll_head = self._dll_tail = node

    def get(self, key: int) -> int:
        if key not in self._lut:
            return -1
        node = self._lut[key]
        self._dll_pop(node)
        self._dll_tail_insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self._lut:
            node = self._lut[key]
            self._dll_pop(node)
            node.val = value
            self._dll_tail_insert(node)
        else:
            if len(self._lut) == self._capacity:
                node_to_evict = self._dll_head
                del self._lut[node_to_evict.key]
                self._dll_pop(node_to_evict)
            new_node = Node(key=key, val=value)
            self._lut[key] = new_node
            self._dll_tail_insert(new_node)
