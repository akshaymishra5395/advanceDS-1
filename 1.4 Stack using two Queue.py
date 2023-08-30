# from Queue import Queue
class Queue:
  def __init__(self):
    self.li=[]
  
  def enqueue(self, x):
    self.li.append(x)
    
    
  def dequeue(self):
    if self.isEmpty():
      return -1
    return self.li.pop(0)
  
  def isEmpty(self):
    return self.li==[]
  
  def printQueue(self):
    print(self.li)

class Stack:
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()

    def push(self,x):
        self.q2.enqueue(x)
        # self.q2.printQueue()
        while(not self.q1.isEmpty() ):
            self.q2.enqueue(self.q1.dequeue())
        self.q1,self.q2=self.q2,self.q1
        

    def pop(self):
        if self.q1.isEmpty():
           print("Stack is Empty")
           return -1
        else:
            return self.q1.dequeue()
        
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