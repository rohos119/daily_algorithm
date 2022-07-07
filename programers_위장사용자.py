import re 
from itertools import *
def solution(user_id, banned_id):
    answer = 0
    pList = ((list(permutations(user_id, len(banned_id)))))
    temp = []
    for p in pList :
        count = 0
        for i in range(len(banned_id)):
            check = re.compile(f"^{banned_id[i].replace('*','.')}$")
            m = check.match(p[i])
            if m and len(banned_id[i]) == len(m.group()) :
                count += 1
        if count == len(banned_id) :
            temp2 = sorted(list(map(str,p)))
            temp.append(temp2)
    answer = set(map(tuple,temp))
    return len(answer)
