class Queue:
    def __init__(self): 
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, value):
        self.enqueue_stack.append(value)

    def dequeue(self):
        if self.dequeue_stack:
            return self.dequeue_stack.pop()
        
        for i in range(len(self.enqueue_stack)):
            self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()
        
x = Queue()
x.enqueue(3)
x.enqueue(5)
x.enqueue(1)
print(x.enqueue_stack, x.dequeue_stack)
print(x.dequeue())
print(x.dequeue())
print(x.dequeue())
