def solution(clothes):
    temp = {}
    for c in clothes :
        temp[c[1]] = 1
    
    for c in clothes :
        temp[c[1]] += 1
    
    answer = 1
    for key,value in temp.items() :
        answer *= value
        
    
    return answer -1
