class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            set_in_row = set()
            for col in range(9):
                if board[row][col] in set_in_row:
                    return False
                elif board[row][col] != ".": #if it's number
                    set_in_row.add(board[row][col])
                else:
                    continue
        
        for col in range(9):
            set_in_col = set()
            for row in range(9):
                if board[row][col] in set_in_col:
                    return False
                elif board[row][col] != ".": #if it's number
                    set_in_col.add(board[row][col])
                else:
                    continue
        
        # i, j is most left upper part of 3*3 grid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                set_in_grid = set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] in set_in_grid:
                            return False
                        elif board[i+k][j+l] != ".":
                            set_in_grid.add(board[i+k][j+l])
                        else:
                            continue

        return True