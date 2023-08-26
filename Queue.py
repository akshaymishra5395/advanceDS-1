#2.1 Queue using list 
class Queue:
  def __init__(self):
    self.li=[]
  
  def enqueue(self, x):
    self.li.append(x)
    
    
  def dequeue(self):
    if self.isEmpty():
      print("Queue is Empty")
      return -1
    return self.li.pop(0)
  
  def isEmpty(self):
    return self.li==[]
  
  def printQueue(self):
    print(self.li)
     
     
if __name__ == '__main__':
  sq = Queue()
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
