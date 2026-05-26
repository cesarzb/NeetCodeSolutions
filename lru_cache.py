"""
Problem: LRU Cache
Link: https://neetcode.io/problems/lru-cache/question

Implement Least Recently Used Cache Class that supports 
put and get operations while having capacity limit.
"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.dummyL = Node(0, 0)
        self.dummyR = Node(0, 0)
        self.dummyL.next = self.dummyR
        self.dummyR.prev = self.dummyL

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]

        self.remove(node)
        self.insert_right(node)

        return node.val

    def insert_right(self, node: Node) -> None:
        node.prev = self.dummyR.prev
        node.next = self.dummyR
        node.prev.next = node
        self.dummyR.prev = node

    def remove(self, node: Node) -> None:
        node.next.prev = node.prev
        node.prev.next = node.next

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.cache[key].val = value
            return
        
        if len(self.cache) >= self.cap:
            old_node = self.dummyL.next
            self.remove(old_node)
            del self.cache[old_node.key]

        self.cache[key] = Node(key, value)
        self.insert_right(self.cache[key])

