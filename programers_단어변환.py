# start 2126
# 문제정의 : begin에서 집합 words로 바꿔가며 target으로 변환하는 가장 짧은 변환과정을 찾아라
# input : 3 begin,words[i],target 10 / 세개의 모든 input은 길이가 같음 / 알파벳 소문자로만 되어있음
# output : 변환 횟수/ 반환이 안되면 0을 return 
        
def solution(begin, target, words):
    
    # logic
    # word의 단어로 바꾸면서 가는 것이다
    # 한번의 한개의 알파벳만 바꿀수 있다
    # words에 있는 단어로만 바꿀수 있다
    # words 각 글자를 visitied로 하자
    # 탐색은 어떻게 할것인가?
    # 종료조건: words를 다돌았을때 종료
    # target이랑 같으면 return count
    
    # 바꿀수 있는 경우의 수는 ? 바꿀 것과 지금것의 글자차이가 1개만 나야함
    #
    answer = 0
    visited = [False]*len(words)
    count = 0
    stack = [(begin, 0)]
    while stack:
        cur, depth = stack.pop()
        if cur == target:
            answer = depth
        
        for i in range(len(words)):
            if visited[i] == True:
                continue
            cnt = 0
            for a,b in zip(cur, words[i]):
                if a!=b:
                    cnt += 1
            if cnt == 1:
                visited[i] = True
                stack.append((words[i], depth+1))
    
 
    
    return answer
