class MultiStack:
  def __init__(self,n,m=100):
    self.n_stack=n
    self.total_size=m
    self.arr=[None]*m
    self.bottom=[self.B(i) for i in range(self.n_stack)]
    self.top=[ x for x in self.bottom]
    print(self.top)
    self.bottom.append(self.total_size-1)    

  def B(self,i):
    return (self.total_size//self.n_stack)*i - 1
    
  def push(self,i,x):
    i=i-1
    if self.top[i]==self.bottom[i+1]:
      print("Stack "+str(i+1)+" is Full")
      return -1
    self.top[i]+=1    
    self.arr[self.top[i]]=x
    print(self.arr)

  def pop(self,i):
    i=i-1
    if self.top[i]==self.bottom[i]:
      print("Stack "+str(i+1)+" is Empty")
      return -1
    temp = self.arr[self.top[i]]
    self.arr[self.top[i]]=None
    self.top[i]-=1
    print(self.arr)
    return temp

if __name__ == '__main__':
  size=10
  number = 3
  sq = MultiStack(number,size)
  sq.push(1,1)
  sq.push(1,2)
  sq.push(1,3)
  sq.push(1,4)
  print(sq.pop(1))
  sq.push(3,1)
  sq.push(3,2)
  sq.push(3,3)
  sq.push(3,4)
  sq.push(3,5)
  
  print(sq.pop(3))
  print(sq.pop(3))
  print(sq.pop(1))
  print(sq.pop(1))
  print(sq.pop(1))
  
  # Q = int(input())
  # while Q > 0:
  #   query = list(map(int, input().split()))
  #   if query[1] == 1:
  #     sq.push(query[0],query[2])
  #   else:
  #     print(sq.pop(query[0]), end=' ')
  #   Q -= 1
  print()

#number of operations
#stack push(1) element 
#stack pop(2)  
# 10   
# 1 1 1 
# 1 1 2 
# 1 1 3
# 1 1 4
# 1 1 5
# 1 1 6
# 2 1 6 
# 1 2 
# 2 2 
# 3 1 10
  

