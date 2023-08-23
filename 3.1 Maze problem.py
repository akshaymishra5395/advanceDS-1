class GFG:
    def __init__(self):
        self.R = None
        self.C = None
        self.dir = [[-1, 1], [0, 1], [1, 1],
                    [1, 0],[1,-1],[0,-1 ], [-1, -1],
                    [-1, 0]]
    
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

    def printPosition(self, matrix, word):
        # Rows and columns in given grid
        self.R = len(matrix)
        self.C = len(matrix[0])
        
        for row in range(self.R):
            for col in range(self.C):
                
                # print("origin",row,col)
                if self.search(matrix, row, col, word):
                    print("pattern found at " +
                           str(row) + ', ' + str(col))


if __name__=='__main__':

    matrix = [
                [1, 0, 0, 0],
                [1, 1, 0, 1],
                [0, 1, 0, 0],
                [1, 1, 1, 1]    ]
    
    gfg = GFG()
    gfg.printPosition(matrix, 'ASH')
    print('')
