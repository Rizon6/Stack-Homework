class Stack:
    def __init__(self, space):
        self.space = space
        self.stack = []
    
    def push(self, item):
        if not self.is_full():
            self.stack.append(item)
        else:
            print("Too many items in stack")
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.space
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None
        
stack = Stack(5)

print(stack.is_empty())
stack.push(1)
print(stack.is_empty())
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.peek())
print(stack.is_full())
stack.pop()
print(stack.peek())
print(stack.is_full())