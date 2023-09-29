class MultiCircularQueue:
    def __init__(self , n , m=100):
        self.total_size = m
        self.n_queue = n
        self.arr = [None] * m
        self.bottom = [self.B(i) for i in range(self.n_queue)]
        self.front = [ x for x in self.bottom]
        self.rear =  [ x for x in self.bottom]
        self.bottom.append(self.total_size-1)
        

    def B(self,i):
        return (self.total_size//self.n_queue)*i - 1

    def enqueue(self,i,x):
        i=i-1
        if  self.front[i]==self.bottom[i]+1 and self.rear[i]==self.bottom[i+1] or self.front[i]==self.rear[i]+1:
            print("Queue "+str(i+1)+" is Full")
            return
        if self.front[i] == self.bottom[i]:
            self.front[i]+=1 
        if self.rear[i] == self.bottom[i+1]:
            self.rear[i]=self.bottom[i]+1
        else:    
            self.rear[i]+=1
        self.arr[self.rear[i]]=x
        print(f"Front={self.front[i]},Rear={self.rear[i]},Bottom={self.bottom[i]}")
        
    def dequeue(self,i):
        i=i-1
        # print(self.front[i],self.rear[i])
        if self.front[i]==self.bottom[i] and self.rear[i]==self.bottom[i]:  ##queue is empty
            print("Queue "+str(i+1)+" is Empty")
            return -1
        elif self.front[i]==self.rear[i]:
            temp = self.arr[self.front[i]]
            self.arr[self.front[i]]=None
            self.front[i],self.rear[i]=self.bottom[i],self.bottom[i]

        elif self.front[i]==self.bottom[i+1]:
            temp = self.arr[self.front[i]]
            self.arr[self.front[i]]=None
            self.front[i]=self.bottom[i]+1
        
        else:
            temp = self.arr[self.front[i]]
            self.arr[self.front[i]]=None
            self.front[i]+=1
        print(f"Front={self.front[i]},Rear={self.rear[i]},Bottom={self.bottom[i]}")
        return temp
     
if __name__ == '__main__':
   size=10
   num_of_queue = 3
   q = MultiCircularQueue(num_of_queue,size)
   q.enqueue(1,1)
   q.enqueue(1,2)
   q.enqueue(1,3)
   print(q.dequeue(1))
   q.enqueue(2,66)
   q.enqueue(2,77)
   
   
   print(q.dequeue(1))
   print(q.dequeue(1))
   print(q.dequeue(2))
   print(q.dequeue(1))
   print()


#   Q = int(input())
#   while Q > 0:
#     query = list(map(int, input().split()))
#     if query[1] == 1:
#       sq.push(query[0],query[2])
#     else:
#       print(sq.pop(query[0]), end=' ')
#     Q -= 1
#   print()


# 4
# 1 2 2 2 2
