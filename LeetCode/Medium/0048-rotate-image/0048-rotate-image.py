class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        visited = [[False] * n for _ in range(n)]

        def move(i: int, j: int, val: int) -> None:
            visited[i][j] = True
            temp = matrix[j][n-1-i]
            matrix[j][n-1-i] = val

            if not visited[j][n-1-i]:
                move(j, n-1-i, temp)

        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    move(i, j, matrix[i][j])
        