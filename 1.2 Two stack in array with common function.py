
class TwoStacks:
  def __init__(self, n=100):
    self.size = n
    self.arr = [None] * n
    self.top1 = -1
    self.top2 = n

  def push(self,i,x):
    if self.top1 ==self.top2 - 1:
      print("Stack "+str(i)+" is Full")
      return 
    else:
      if i==1:
        self.top1+=1
        self.arr[self.top1]=x
      else:
        self.top2-=1
        self.arr[self.top2]=x
      print(self.arr)

  
  def pop(self,i):
    if i==1:
      if self.top1==-1:
        print("Stack "+str(i)+" is Empty")
        return -1
      else:
        temp = self.arr[self.top1]
        self.arr[self.top1]=None
        self.top1-=1
        print(self.arr)
        return temp
    else:
      if self.top2==self.size:
        print("Stack "+str(i)+" is Empty")
        return -1
      else:
        temp = self.arr[self.top2]
        self.arr[self.top1]=None
        self.top2+=1
        print(self.arr)
        return temp
        
if __name__ == '__main__':
  sq = TwoStacks(5)
  sq.push(1,2)
  sq.push(1,3)
  sq.push(1,5)
  sq.push(2,14)
  sq.push(2,12)
  sq.push(2,11)
  print(sq.pop(1))
  print(sq.pop(1))
  print(sq.pop(1))
  print(sq.pop(1))
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
