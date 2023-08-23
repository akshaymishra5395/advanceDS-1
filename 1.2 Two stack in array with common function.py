
class TwoStacks:
  def __init__(self, n=100):
    self.size = n
    self.arr = [0] * n
    self.top1 = -1
    self.top2 = n

  def push(self,i,x):
    if self.top1 !=self.top2 - 1:
      if i==1:
        self.top1+=1
        self.arr[self.top1]=x
      else:
        self.top2-=1
        self.arr[self.top1]=x
  
  def pop(self,i):
    if i==1:
      if self.top1==-1:
        return -1
      else:
        temp = self.arr[self.top1]
        self.top1-=1
        return temp
    else:
      if self.top2==self.size:
        return -1
      else:
        temp = self.arr[self.top2]
        self.top2+=1
        return temp
        
if __name__ == '__main__':
  sq = TwoStacks()
  Q = int(input())
  while Q > 0:
    query = list(map(int, input().split()))
    if query[1] == 1:
      sq.push(query[0],query[2])
    else:
      print(sq.pop(query[0]), end=' ')
    Q -= 1
  print()

#number of operations
#stack push(1) element 
#stack pop(2)  
# 6   
# 1 1 2 
# 1 1 3 
# 2 1 4 
# 1 2 
# 2 2 
# 2 2
