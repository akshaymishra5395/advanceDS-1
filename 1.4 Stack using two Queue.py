from Queue import Queue

class Stack:
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()

    def push(self,x):
        pass

    def pop(self):
        pass
        
if __name__ == '__main__':
    sq = Stack()
    sq.push(1)
    sq.push(2)
    sq.push(3)
    print(sq.pop())
    sq.push(4)
    print(sq.pop())
    print(sq.pop())
    print(sq.pop())
    print(sq.pop())
    print()