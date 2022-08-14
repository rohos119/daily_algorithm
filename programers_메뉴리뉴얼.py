# start 2250 , goal 40m , end 2328 -> take 40 
# 문제정의 : 가장 많이 주문한 단품메뉴들을 코스 메뉴로 변경, 단  코스 메뉴는 2가지 이상, 최소 2명이상 손님이 주문
# input : 2 order : 단품메뉴 20 / 알파벳 대문자, 같은 알파벳 x , 1 course: 코스의 단품메뉴 개수 10 / 오름차순 정렬, 중복 x
# output : 사전순으로 오름차순 정렬한 문자열 list

from itertools import combinations 
def solution(orders, course):
    answer = []
    menu_dic={}
    for o in orders :
        for c in course:
            temp = combinations(sorted(list(o)),c)
            for t in temp :
                if t in menu_dic.keys() :
                    menu_dic[t] += 1
                else:
                    menu_dic[t] = 1
    for c in course :
        max_v = 2
        temp = []
        for k,v in menu_dic.items() :
            if len(k) == c and v >= 2 :
                if v > max_v :
                    max_v = v
                    temp = []
                    temp.append(''.join(k))
                elif v==max_v :
                    temp.append(''.join(k))
        answer += temp
        answer.sort()

    return answer
