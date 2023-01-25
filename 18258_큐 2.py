class DoublyLinkedList:
    class _Node:
        __slots__ = "element", "prev", "next"
        def __init__(self, e, p, n):
            self.element = e
            self.prev = p
            self.next = n

    def __init__(self):
        self.header = self._Node(None, None, None)
        self.trailer = self._Node(None, None, None)
        self.header.next, self.trailer.prev = self.trailer, self.header
        self.length = 0

    def push(self, e):
        new_node = self._Node(e, self.trailer.prev, self.trailer)
        self.trailer.prev.next = new_node
        self.trailer.prev = new_node

        self.length += 1
    
    def remove_first(self):
        if self.empty():
            return -1
        to_be_removed = self.header.next
        self.header.next, to_be_removed.next.prev = to_be_removed.next, self.header

        self.length -= 1

        return to_be_removed.element
        
    def size(self):
        return self.length
    
    def empty(self):
        return int(not bool(self.length))
    
    def front(self):
        if self.empty():
            return -1
        
        return self.header.next.element

    def back(self):
        if self.empty():
            return -1
        
        return self.trailer.prev.element

input = __import__("sys").stdin.readline
queue = DoublyLinkedList()
command_map = {
    "push": queue.push,
    "pop": queue.remove_first,
    "size": queue.size,
    "empty": queue.empty,
    "front": queue.front,
    "back": queue.back
}
for _ in range(int(input())):
    cmds = input().split()
    if len(cmds) == 1:
        print(command_map[cmds[0]]())
    else:
        command_map[cmds[0]](cmds[1])

# -----------------------

class PseudoQueue:
    def __init__(self):
        self._list = []
        self.first_idx = 0
        self.length = 0
    
    def push(self, e):
        self._list.append(e)
        self.length += 1

    def size(self):
        return self.length

    def empty(self):
        return int(not bool(self.length))

    def front(self):
        if self.empty():
            return -1
        return self._list[self.first_idx]

    def back(self):
        if self.empty():
            return -1
        return self._list[-1]

    def remove_first(self):
        if self.empty():
            return -1
        element = self._list[self.first_idx]
        self.first_idx += 1
        self.length -= 1
        return element

input = __import__("sys").stdin.readline
queue = PseudoQueue()
command_map = {
    "push": queue.push,
    "pop": queue.remove_first,
    "size": queue.size,
    "empty": queue.empty,
    "front": queue.front,
    "back": queue.back
}
for _ in range(int(input())):
    cmds = input().split()
    if len(cmds) == 1:
        print(command_map[cmds[0]]())
    else:
        command_map[cmds[0]](cmds[1])