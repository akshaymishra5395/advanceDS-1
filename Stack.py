class Stack:
    def __init__(self):
        self.li=[]

    def push(self,x):
        self.li.append(x)
        # print(self.li,x)

    def pop(self):
        return self.li.pop()
    
    def isEmpty(self):
        return self.li==[]
    
