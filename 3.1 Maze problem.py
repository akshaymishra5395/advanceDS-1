class PathFinder:
    def __init__(self):
        self.R = None
        self.C = None
        self.dir = [[-1, 1], [0, 1], [1, 1],
                    [1, 0],[1,-1],[0,-1 ], [-1, -1],
                    [-1, 0]]
        self.visited =None
    
    def search(self,matrix,row,col,word):
        if matrix[row][col] != word[0]:
            return False
        
        for x, y in self.dir:

            rd, cd = row + x, col + y
            word_len = len(word)
            k=1
            while k< word_len:
                if (rd <0 or rd >= self.R or cd<0 or cd >=self.C):
                    break
                if (word[k] != matrix[rd][cd]):
                    break
                # print((rd,cd),matrix[rd][cd])
                rd += x
                cd += y
                k+=1
                # print("updated:",(rd,cd,k))
                

            if k == word_len:
                return True
            
        return False

    def findAllPath(self, matrix):
        # Rows and columns in given grid
        self.R = len(matrix)
        self.C = len(matrix[0])
        self.visited=[[0 for _ in range(self.C)] for _ in range(self.R) ]
        from Stack import Stack
        stack = Stack()
        cordinates=(0,0)
        direction=0
        self.visited[0][0]=1 
        
        stack.push((*cordinates,direction))
        while(not stack.isEmpty()):
            (i,j,direction) = stack.pop()
            while(direction<len(self.dir)):
                
                x,y=self.dir[direction]
                g, h = i + x, j + y
                print((i,j),direction)
                if (g <0 or g >= self.R or h<0 or h >=self.C):
                    direction+=1
                    continue
                if g==self.R - 1 and h == self.C -1 :
                    stacklist=[(x[0],x[1])for x in stack.peekStack()]
                    print(stacklist)
                    self.visited[g][h]=1
                    direction+=1
                
                elif matrix[g][h] and not self.visited[g][h]:
                    self.visited[g][h]=1
                    stack.push((i,j,direction))
                    i=g;j=h;direction=0
                else:
                    direction+=1
            print("--")
        print("No path found")


if __name__=='__main__':

    matrix = [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 1]    ]
    
    pf = PathFinder()
    pf.findAllPath(matrix)
    print('')
