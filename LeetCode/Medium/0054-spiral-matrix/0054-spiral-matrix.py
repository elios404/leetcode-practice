class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0]) # Row, Col
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        visited = [[False] * n for _ in range(m)]

        output = []
        cnt = 0
        y,x,d = 0,0,0
        while True:
            output.append(matrix[y][x])
            visited[y][x] = True
            cnt += 1

            if cnt == m * n:
                break

            ny, nx = y + dy[d], x + dx[d]
            if ny < 0 or m <= ny or nx < 0 or n <= nx or visited[ny][nx]: #True
                d = (d+1)%4
                y, x = y + dy[d], x + dx[d]
            else:
                y,x = ny,nx

        #print(output)
        return output