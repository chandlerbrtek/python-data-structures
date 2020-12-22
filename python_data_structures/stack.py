"""Main module."""
class Stack:
    stack = []

    def isEmpty(self) -> bool:
        return len(self.stack) == 0

    def push(self, value: any) -> None:
       self.stack.append(value)
    
    def peek(self) -> any:
        return self.stack[-1]
    
    def pop(self) -> any:
        return self.stack.pop()