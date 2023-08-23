class MultiCircularQueue:
    def __init__(self , n , m=100):
        self.total_size = m
        self.n_queue = n
        self.arr = [None] * m
        self.bot = [self.B(i) for i in range(self.n_queue+1)]
        self.front = [ x for x in self.i_bottom]
        self.rear =  [ x for x in self.i_bottom]    
    
    def B(self,i):
        return (self.total_size//self.n_queue)*i - 1

    def enqueue(self,i,x):
        if self.front[i]==self.Bottom[i-1] and self.rear[i]==self.Bottom[i] or self.front[i]==self.rear[i]:
            print("stack overflow")
            return
        if self.front[i] == self.Bottom[i-1]:
            self.front[i]+=1  
        self.rear[i]+=1
        self.arr[self.rear[i]]=x

    def pop(self,i):
        if self.front[i]==self.Bottom[i-1] and self.rear[i]==self.Bottom[i-1]:  ##queue is empty
            return -1
        elif self.front[i]==self.Bottom[i]:
            temp = self.arr[self.front[i]]
            self.front[i]=self.Bottom[i-1]+1
        elif self.front[i]==self.rear[i]:
            temp = self.arr[self.front[i]]
            self.front[i],self.rear[i]=self.Bottom[i-1],self.Bottom[i-1]
        else:
            temp = self.arr[self.front[i]]
            self.fron[i]+=1
        return temp
     
if __name__ == '__main__':
  size=10
  number = 3
  sq = MultiCircularQueue(number,size)
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
