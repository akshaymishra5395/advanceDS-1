class MultiStack:
  def __init__(self,n,m=100):
    self.total_size=m
    self.n_stack=n
    self.arr=[None]*m
    self.i_top=[self.B(i) for i in range(1,n)]
    
  def T(self,i):
    return self.i_top[i-1]
    
  def B(self,i):
    return (self.total_size//self.n_stack)*i - 1
    
  def push(self,i,x):
    if self.T(i)==self.B(i):
      print("stack overflow")
      return
    self.i_top[i-1]+=1    
    self.arr[self.i_top[i-1]]=x

  def pop(self,i):
    if self.T(i)==self.B(i-1):
      print("stack empty")
      return 
    temp = self.arr[self.i_top[i-1]]
    self.i_top[i-1]-=1
    return temp

if __name__ == '__main__':
  size=10
  number = 3
  sq = MultiStack(number,size)
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
  

