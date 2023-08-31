class TwoDQueue:
    def __init__(self , n , m=100):
        self.R = n
        self.C = m
        self.n_queue = n
        self.arr = [[None for x in  range(self.C)] for x in range(self.R)]
        self.front = [-1]*self.R
        self.rear =  [-1]*self.R

    def enqueue(self,i,x):
        if  self.front[i]== 0 and self.rear[i]==self.C -1 or self.front[i]==self.rear[i]+1:
            print(f"Queue {str(i)} is Full")
            return
        if self.front[i] == -1:
            self.front[i]=0 
            self.rear[i]=0
        elif self.rear[i] == self.C -1:
            self.rear[i]= 0
        else:
            self.rear[i]+=1    
        self.arr[self.front[i]][self.rear[i]]=x
        print(f"Q={i},Front={self.front[i]},Rear={self.rear[i]}")
       
    def dequeue(self,i):
        
        if self.front[i]== -1 and self.rear[i]== -1:  ##queue is empty
            print(f"Queue {str(i)} is Empty")
            return -1
        elif self.front[i]==self.rear[i]:
            temp = self.arr[self.front[i]][self.rear[i]]
            self.arr[self.front[i]][self.rear[i]]=None
            self.front[i],self.rear[i]= -1,-1

        elif self.front[i] == self.C -1:
            temp = self.arr[self.front[i]][self.rear[i]]
            self.arr[self.front[i]][self.rear[i]]=None
            self.front[i]=0
        
        else:
            temp = self.arr[self.front[i]][self.rear[i]]
            self.arr[self.front[i]][self.rear[i]]=None
            self.front[i]+=1
        print(f"Q={i},Front ={self.front[i]}, Rear ={self.rear[i]}")
        return temp
     
if __name__ == '__main__':
   size=5
   num_of_queue = 4
   q = TwoDQueue(num_of_queue,size)
   q.enqueue(0,1)
   q.enqueue(1,1)
   q.enqueue(1,2)
   q.enqueue(1,3)
   print(q.dequeue(0))
   q.enqueue(2,66)
   q.enqueue(2,77)

   print()

