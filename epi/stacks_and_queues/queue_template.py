import collections

class Queue:
    def __init__(self):
        self._data = collections.deque()
    
    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.popleft()

    def max(self):
        return max(self._data)
