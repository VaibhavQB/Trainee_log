# STACK Implementation Using Class

class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def stacklen(self):
        return len(self.stack)

    def isFull(self):
        return self.stacklen() == self.size

    def isEmpty(self):
        return self.stacklen() == 0

    def stackpush(self, val):
        if self.isFull():
            return "Stack is FULL! Can not push another item"
        self.stack.append(val) 

    def stackpop(self):
        if self.isEmpty():
            return "Stack is Empty! Can not pop item"
        return self.stack.pop()

    def top(self):
        if self.isEmpty :
            return "No Items in Stack"
        return self.stack[-1]
    
    def __str__(self):
        return str(self.stack) if not self.isEmpty() else "Stack is Empty"


s = Stack(7)
s.stackpush("Hi")
s.stackpush("All")
s.stackpush("Great")
print(s)
 
print(s.stacklen())
 
print("remove this element",s.stackpop())
s.stackpop()
s.stackpop()
s.stackpop()
 
print(s.top())
print(s.stacklen())
print(s)