# 1215 1255
# 문제정의 : 무손실 압축 (LZW)를 구현하라
# input : 영문대문자로만 된 msg / 1 msg 1000
# output : 색인번호를 출력
from collections import deque
def solution(msg):
    answer = []
    dic = {chr(ord('A')+i) : i+1 for i in range(0,26)}  
    addwords = []
    end = 26
    # logic
    # 시작점과 끝점을 잡고
    # 만약 dic 안에 시작점과 끝점+1 까지가 없다면
    # dic끝으로 넣고
    # 답은 시작점과 끝점까지만을 넣는다
    # 넣고 나서 시작점을 최신화 
    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1
            answer.append(dic[msg[w:c]])
            w = c

    return answer
