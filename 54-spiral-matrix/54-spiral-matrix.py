class Solution:
    def spiralOrder(self, matrix):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows = len(matrix)
        cols = len(matrix[0])

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        answer = []
        visitied = [[0] * cols for _ in range(rows)]

        def dfs(r, c, d):
            dx, dy = directions[d][0], directions[d][1]

            if len(answer) >= rows*cols:
                return

            if (r < 0 or r >= rows or c < 0 or c >= cols) or visitied[r][c] ==1:
                d += 1
                d = (d + 4) % 4
                d_dx, d_dy = directions[d][0], directions[d][1]
                return dfs(r-dx+d_dx,c-dy+d_dy,d)


            visitied[r][c] = 1
            # print(visitied, matrix, matrix[r][c], d)
            answer.append(matrix[r][c])
            dfs(r + dx, c + dy, (d + 4) % 4)
            return
        
        dfs(0,0,0)
        return answer

