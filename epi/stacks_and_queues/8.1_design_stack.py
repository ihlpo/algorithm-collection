class Stack:
    def __init__(self):
        self.stack = []
        self.max = float('-inf')
    
    def push(self, value):
        self.stack.append(value)
        self.max = max(value, self.max)
        return
    
    def pop(self):
        return self.stack.pop()