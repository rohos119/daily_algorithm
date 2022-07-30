#2023
# 문제정의 : \ -> 1 / -> -1 이 있는 곳에서 바닥까지 내려오는 공을 찾아라
# input : 1 m n 100
# output : 떨어진 column 위치 if 바닥까지 떨어지면 else -1

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # logic
        # 통과조건 : if x == m return n
        # 종료조건 : y가 이전보다 증가할때 -> 통과를 못하는 상황 -> 방향이 U가 될때
        # 떨어지는것을 어떻게 확인할까?
        # hint -> V 모양을 한 곳은 통과가 불가 하다 -> 연속적으로 1, -1인 모양
        # 방향을 정할까?
        # L R U D
        # 첫 시작일 때는 무조건 D로 시작
        # 1(\)일때 : D->R, L->U , R->D
        # -1(/)일때 : D->L, L->D, R->U
        direction = {'D' : (1,0),'L' : (0,-1),'R' : (0,1),'U' : (-1,0)}
        direct_ch = { '1':{'D' :'R','L':'U','R':'D'},
                      '-1' :{'D':'L','L':'D','R':'U'}
                    }
        rows,cols = len(grid), len(grid[0])
        answer = [-1]*cols
        ball = [[i,'D'] for i in range(cols)]
        print(rows,cols)
        for i,b in enumerate(ball) :
            x,y = 0,b[0]
            while b[1] != 'U' :
                b[1] = direct_ch[str(grid[x][y])][b[1]]
                x = x+direction[b[1]][0]
                y = y+direction[b[1]][1]
                if x<0 or y>=cols or y<0 :
                    break
                if x == rows :
                    answer[i] = y
                    break
        return answer     