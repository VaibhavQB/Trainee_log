class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def stacklen(self):
        return len(self.stack)

    def isFull(self):
        return self.stacklen == self.size

    def isEmpty(self):
        return self.stacklen == 0

    def stackpush(self, val):
        if self.isfull():
            return "Stack is FULL! Can not push another item"
        self.stack.append(val) 

    def stackpop(self):
        if self.isEmpty():
            return "Stack is Empty! Can not pop item"

    def top(self):
        if self.isEmpty :
            return "No Items in Stack"
        return self.stack[-1]


s = Stack(7)
print(s.stacklen())