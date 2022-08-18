# start 0011 0138
# 문제정의 : 겹쳐진 도형의 외각을 따라서 가는 가장짧은 경로를 구하라
# input : 1 rectangle 4, 1 charcterx,y 캐릭터초기위치 50, 1 itemx,y 아이템위치 50 
# output : 가장짧은경로 -> int 
from collections import *

def solution(rectangle, characterX, characterY, itemX, itemY):
    # logic
    # 가장짧은 경로를 구하라 -> bfs로 풀자
    # queue에 갈 수 있는 경로를 넣고
    # 종료조건은 itemx,itemy에 도착했을 경우

    # rectangle을 좌표로 표현하자
    # rectangle의 최대는 51*51
    matrix = [[0] * 1000 for _ in range(1000)]
    answer = 0
    for c1, r1, c2, r2 in rectangle:
        for i in range(2 * r1, 2 * r2 + 1):
            for j in range(2 * c1, 2 * c2 + 1):
                matrix[i][j] = 1

        # 사각형 테두리 0으로 채우기
    for c1, r1, c2, r2 in rectangle:
        for i in range(2 * r1 + 1, 2 * r2):
            for j in range(2 * c1 + 1, 2 * c2):
                matrix[i][j] = 0


    chR, chC, itR, itC = 2*characterY, 2*characterX, 2*itemY, 2*itemX
    stack = [(0, chR, chC)]
    while stack : 
        w, chR, chC = stack.pop(0) # 너비 우선 탐색
        matrix[chR][chC] = -1 # passed
        
        if matrix[itR][itC]<0 : return w//2
        
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)] : 
            if matrix[chR+dr][chC+dc]>0 : 
                stack.append((w+1, chR+dr, chC+dc))

 
