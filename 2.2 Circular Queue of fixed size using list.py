class CircularQueue:
  def __init__(self,n=100):
    self.size=n
    self.arr=[None]*n
    self.front= -1
    self.rear=-1
    
  #Function to push an element x in a queue.
  def push(self, x):
    if self.front==0 and self.rear == self.size-1 or self.front == self.rear+1 : ##queue is full
      return -1
    else:
      if self.front == -1:
        self.front+=1  
      self.rear+=1
      self.arr[self.rear]=x
    
  #Function to pop an element from queue and return that element.
  def pop(self):
    if self.front==-1 and self.rear==-1:  ##queue is empty
      return -1
    elif self.front==self.size-1:
      temp = self.arr[self.front]
      self.front=0
    elif self.front==self.rear:
      temp = self.arr[self.front]
      self.front,self.rear=-1,-1
    else:
      temp = self.arr[self.front]
      self.fron+=1
    return temp

     
if __name__ == '__main__':
  sq = CircularQueue()
  Q = int(input())
  while Q > 0:
    query = list(map(int, input().split()))
    if query[1] == 1:
      sq.push(query[0],query[2])
    else:
      print(sq.pop(query[0]), end=' ')
    Q -= 1
  print()


# 4
# 1 2 2 2 2
