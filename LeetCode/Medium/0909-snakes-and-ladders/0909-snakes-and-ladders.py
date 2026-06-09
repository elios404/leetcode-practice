"""
1. Approach : 
    - Firstly, we need to find which position (i, j) we can go in next step
    - If we need to check whether next move is heading right or left. By, gap between board_row and current row % 2 is even or odd.
    - If it's odd then need to go left, if it's even then go to right.
    - While heading right, if we reach the end of the row then go up, if heading left and reach the start of the row, then go up.
    => totally different apporach -> Why we need to think this in grid, we only need to know which number is in which position of the board (I solved in this way)
2. Time Complexity : O(N^2) - In worst case, visit every number in board
3. Space Complexity : O(N^2) - Visited Boolean Array is O(N) and queue for the next location.. Don't know well but at least smaller than put all the number in queue
"""
from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)

        # Helper: Keep it 1-indexed to match the game exactly
        def get_coordinates(square: int) -> tuple[int, int]:
            # Subtract 1 just for the math, to get 0-based row/col offsets
            r, c = divmod(square - 1, n)
            # If it's an odd row from the bottom, the column goes right-to-left
            if r % 2 == 1:
                c = n - 1 - c
            # Return actual matrix row (inverted from top) and col
            return n - 1 - r, c

        # Queue stores: (current_square, moves_taken)
        q = deque([(1, 0)])
        visited = set([1])

        while q:
            curr_square, moves = q.popleft()
            
            for dice_roll in range(1, 7):
                next_square = curr_square + dice_roll
                
                # Optimization: if we exceed the board, stop checking larger dice rolls
                if next_square > n * n:
                    break
                
                # Check for snakes/ladders
                r, c = get_coordinates(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                
                # Check winning condition immediately
                if next_square == n * n:
                    return moves + 1
                
                # Only add to queue if this final destination hasn't been visited
                if next_square not in visited:
                    visited.add(next_square)
                    q.append((next_square, moves + 1))
                    
        return -1