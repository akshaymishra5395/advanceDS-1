from Stack import Stack

class MyQueue:
    def __init__(self):
        self.s1=Stack()
        self.s2=Stack()
  
    def enqueue(self,x):    #O(1)
       self.s1.push(x)
       
    def dequeue(self):      #O(N)
        if not self.s2.isEmpty():
           return self.s2.pop()
        elif not self.s1.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
            return self.s2.pop()
        else:
            print("Queue is Empty")     
        
if __name__ == '__main__':
    sq = MyQueue()
    sq.enqueue(1)
    sq.enqueue(2)
    sq.enqueue(3)
    print(sq.dequeue())
    sq.enqueue(4)
    print(sq.dequeue())
    print(sq.dequeue())
    print(sq.dequeue())
    print(sq.dequeue())
    print()

