class DNode(): 
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:
    def _addNode(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _removeNode(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _bringToFront(self, node):
        self._removeNode(node)
        self._addNode(node)

    def _pop_tail(self):
        res = self.tail.prev
        self._removeNode(res)
        return res

    def __init__(self, capacity: int):
        self.lruMap = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DNode(), DNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.lruMap.get(key, None)
        if not node:
            return -1

        self._bringToFront(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.lruMap.get(key)

        if not node: 
            self.size += 1
            if self.size > self.capacity:
                lastNode = self.tail.prev
                self._removeNode(lastNode);
                del self.lruMap[lastNode.key]
                self.size -= 1                        
            node = DNode(key, value)
            self.lruMap[key] = node
            self._addNode(node)
        else:
            node.value = value
            self._bringToFront(node)