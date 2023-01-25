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
    
    def push_front(self, e):
        new_node = self._Node(e, self.header, self.header.next)
        self.header.next.prev = new_node
        self.header.next = new_node
        self.length += 1

    def push_back(self, e):
        new_node = self._Node(e, self.trailer.prev, self.trailer)
        self.trailer.prev.next = new_node
        self.trailer.prev = new_node
        self.length += 1

    def pop_front(self):
        if self.empty():
            return -1
        to_be_removed = self.header.next
        self.header.next, to_be_removed.next.prev = to_be_removed.next, self.header

        self.length -= 1
        return to_be_removed.element
    
    def pop_back(self):
        if self.empty():
            return -1
        to_be_removed = self.trailer.prev
        self.trailer.prev, to_be_removed.prev.next = to_be_removed.prev, self.trailer

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
deque = DoublyLinkedList()

command_map = {
    "push_front": deque.push_front,
    "push_back": deque.push_back,
    "pop_front": deque.pop_front,
    "pop_back": deque.pop_back,
    "size": deque.size,
    "empty": deque.empty,
    "front": deque.front,
    "back": deque.back
}

for _ in range(int(input())):
    cmds = input().split()
    if len(cmds) == 1:
        print(command_map[cmds[0]]())
    else:
        command_map[cmds[0]](cmds[1])

# --------------------

# from collections import deque
# import sys
# deq = deque([])
# input()
# for commands in sys.stdin.read().rstrip().split('\n'):
#     command = commands.split()
#     if command[0] == "push_front":
#         deq.appendleft(command[-1])
#     elif command[0] == "push_back":
#         deq.append(command[-1])
#     elif command[0] == "pop_front":
#         if deq:
#             print(deq.popleft())
#         else:
#             print(-1)
#     elif command[0] == "pop_back":
#         if deq:
#             print(deq.pop())
#         else:
#             print(-1)
#     elif command[0] == "size":
#         print(len(deq))
#     elif command[0] == "empty":
#         print(int(not bool(deq)))
#     elif command[0] == "front":
#         if deq:
#             print(deq[0])
#         else:
#             print(-1)
#     else:
#         if deq:
#             print(deq[-1])
#         else:
#             print(-1)