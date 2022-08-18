class Stack:
    def __init__(self):
        self.data = []
        self.min = float('inf')
    def push(self, value):
        if value < self.min:
            self.min = value
        self.data.append(value)

    def pop(self):
        value = self.data.pop()
        if value == self.min:
            self.min = min(self.data)
        return value
    def get_min(self):
        return self.min
