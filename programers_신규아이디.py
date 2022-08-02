# start : 1820  goal : 30m end : 1838
# 문제정의 : 7단계에 맞춰 new_id를 수정해라
# input : 1 n 100 / n은 - / _ . 만가능
# output : userid -> string
import re
def solution(new_id):
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id.lower())
    new_id = re.sub(r'[.]{2,}', '.', new_id) 
    new_id = new_id.strip('.')
    if len(new_id) == 0:
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]

    answer = new_id
    return answer
