class Stack:
    def __init__(self):
        self.li=[]

    def push(self,x):
        self.li.append(x)

    def pop(self):
        return self.li.pop()
    
    def top(self):
        return self.li[-1]
    
    def isEmpty(self):
        return self.li==[]
    
    def printStack(self):
        print(self.li)
        
    def peekStack(self):
        return self.li
    
