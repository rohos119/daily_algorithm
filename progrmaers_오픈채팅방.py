def solution(record):
    # user_id의 고유값
    temp = {}
    flag = {'Enter' : '들어왔습니다.', 'Leave' : '나갔습니다.' }
    answer = []
    
    for r in record :
        line = r.split(' ')
        if line[0] in ['Enter','Change'] :
            temp[line[1]] = line[2]
            
    for r in record :
        line = r.split(' ')
        if line[0] != 'Change' :
            answer.append(temp[line[1]] +"님이 "+ flag[line[0]]) 
        
    return answer
