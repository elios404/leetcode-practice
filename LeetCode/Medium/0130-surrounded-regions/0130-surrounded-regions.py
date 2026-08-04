# So only leave the region touches the edges of the grid and replace all "O" To "X"
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m, n = len(board), len(board[0]) #row, col
        di = [-1, 0, 1, 0]
        dj = [0, -1, 0, 1]

        def search(i, j):
            board[i][j] = 'V'

            for d in range(4):
                ni, nj = i + di[d], j + dj[d]

                if ni < 0 or m <= ni or nj < 0 or n <= nj:
                    continue
                if board[ni][nj] == 'O':
                    search(ni, nj)
        
        # 1. search border first
        for j in [0, n-1]:
            for i in range(m):
                if board[i][j] == 'O':
                    search(i,j)
        
        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == 'O':
                    search(i,j)

        # 2. replace left "O"
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        # 2. replace "V" to "O"
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'V':
                    board[i][j] = 'O'