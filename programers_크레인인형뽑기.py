from collections import deque
def solution(board, moves):
    answer = 0
    temp = []
    for m in moves :
        for i in range(len(board[0])):
            if board[i][m-1] !=0 :                
                if len(temp)>0 :
                    if temp[-1] == board[i][m-1]:
                        temp.pop()
                        answer += 1
                    else :
                        temp.append(board[i][m-1])  
                else :     
                    temp.append(board[i][m-1])
                board[i][m-1]=0
                break
                
    return answer*2
