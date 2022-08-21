class Stack:
    '''Builing a min stack while keeping all push pop peek operations O(1). We can use a stack to keep the min values
    and pop them out when value is removed from the data stack. Alternatively, we can have nodes(objects) that keeps
    both the value and the previous min value. The method can potentially be space inefficient'''
    def __init__(self):
        self.data = []
        self.min_stack = []
    def push(self, value):
        if self.min_stack:
            if value < self.min_stack[-1]:
                self.min_stack.append(value)
        else:
            self.min_stack.append(value)
        self.data.append(value)

    def pop(self):
        value = self.data.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value
    def get_min(self):
        return self.min_stack[-1]


x = Stack()
x.push(5)
x.push(10)
print(x.get_min())
x.push(1)
print(x.get_min())
x.pop()
print(x.get_min())
print(x.data)
