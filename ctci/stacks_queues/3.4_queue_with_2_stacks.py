class MyQueue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, value):
        self.enqueue_stack.append(value)

    def dequeue(self):
        if self.dequeue_stack:
            return self.dequeue_stack.Zpop()
        for i in range(len(self.enqueue_stack)):
            self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def top(self):
        if self.enqueue_stack:
            return self.enqueue_stack[0]
        else:
            return self.dequeue_stack[-1]
    def is_empty(self):
        return not self.dequeue_stack and not self.enqueue_stack

x = MyQueue()
x.is_empty()
x.enqueue(4)
print(x.top())
x.enqueue(2)
print(x.top())
print(x.dequeue())
print(x.top())
x.enqueue(3)
print(x.top())
print(x.dequeue())
