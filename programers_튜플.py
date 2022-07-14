def solution(s):
    answer = []
    temp = [ si.replace("{","").replace("}","").split(',') for si in s[1:-1].split("},")]
    temp2 = [ len(t) for t in temp ]
    
    check = 1
    for i in range(1,len(temp)+1) :
        for t in temp[temp2.index(i)] :
            if int(t) not in answer :
                answer.append(int(t))
        check += 1        
    return answer
