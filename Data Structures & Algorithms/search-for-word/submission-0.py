class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        sol = set()

        def backtrack(i, j, index):
            if index == len(word):
                return True

            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[index] or (i, j) in sol:
                return False

            sol.add((i, j))
            res = (backtrack(i+1, j, index+1) or 
                backtrack(i-1, j, index+1) or 
                backtrack(i, j+1, index+1) or 
                backtrack(i, j-1, index+1))
            sol.remove((i, j))
            return res

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0): return True

        return False
            
                    
        
