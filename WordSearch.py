Word Search:
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Time = O(m*n)4^L - m*n is the no of the elements in the matrix , L is the length of the string(word) 4 is the direction
need to search.
Space = O(n) - length of the string(word)





class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board == None or len(board) == 0 or len(word) == 0:
            return False
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(word,board,i,j):
                    return True
        return False
    def dfs(self,word,board,i,j):
        #base case Check
        if (i < 0 or j < 0 or i >= self.m or j >= self.n or board[i][j] == "#"):
            return False
        #logic
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        if board[i][j] == word[0]:
            if len(word) == 1:
                return True
            prev = board[i][j] 
            board[i][j]  = "#"
            for d in dirs: #action
                row = d[0] + i
                col = d[1] + j
                if (self.dfs(word[1:],board,row,col)): #recursion
                    return True
            board[i][j] = prev #backtracking
        return False
