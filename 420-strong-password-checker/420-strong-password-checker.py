# start 1700
# 문제정의 : 대문자,소문자, 숫자는 최소 한개이상을 포함하고, 같은 문자는 인접해서 3번 반복 안되는
#           비밀번호를 만들 수 있는 단계를 찾아라 비밀번호는 6~20
# input :  1 password 50
# output : 이미 strong 0 / 아니면 strong 만들 최소 단계
# from collections import Counter

# class Solution:
#     def strongPasswordChecker(self, password: str) -> int:
        
#         def checkone (password) :
#             count = 0
#             if 6<= len(password) <= 20 :
#                 print('checkone',[count,0,0])
#                 return checktwo(password ,[count,0,0] )
#             else :
#                 if len(password) > 20 :
#                     count = len(password)-20 
#                     print('checkone',[0,count,0])
#                     return checktwo(password, [0,count,0])
#                 if len(password) < 6 :
#                     count = 6-len(password)
#                     print('checkone',[count,0,0])
#                     return checktwo(password, [count,0,0])

#         def checktwo (password, change) :
#             pos = [0,0,0]
#             check = Counter(password)
#             for c in check :
#                 if c.isdecimal():
#                     pos[0] = 1
#                 if c.isupper() :
#                     pos[1] = 1
#                 if c.islower() :
#                     pos[2] = 1
#             print('pos',pos)
#             if pos[0] and pos[1] and pos[2] :
#                 print('checktwo', change)
#                 return checkthree(password,change) 
#             else :
#                 if change[0] < 3-sum(pos) :
#                     if len(password) < 6 :
#                         change[0] += 3-sum(pos)-change[0]
#                         print('checktwo', change)
#                     if len(password) > 20 :
#                         change[0] += 3-sum(pos)
#                         change[2] += 3-sum(pos)
#                         print('checktwo', change)
#                     if 6 <= len(password) <= 20 :
#                         change[0] += 3-sum(pos)
#                         change[2] += 3-sum(pos)
#                 return checkthree(password,change)

#         def checkthree(password, change) :
#             count = 0
#             check = Counter(password)
#             insert = change[0]
#             delete = change[1]
#             chword = change[2]
#             print(change)
#             return insert+delete+chword


#             # logic
#             # greedy 접근법
#             # 각 조건을 만족하는 것이 최적해, 즉 유일해이다
#             # 각 조건을 만족 시키기 위한 방법을 강구해야한다.
#             # 실제 값을 대입해서 구해야하는가??
#             # 그리디 접근을 위해 최상위 조건은 ? 1번
#             # 3개의 조건을 체크하는 함수를 만들고 재귀로 호출한다

#         count = checkone(password)         
#         return count

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        lower = any('a' <= c <= 'z' for c in password)
        upper = any('A' <= c <= 'Z' for c in password)
        digit = any(c.isdigit() for c in password)
        missing = 3 - int(lower) - int(upper) - int(digit)
        
        # case 1: len < 6
        if len(password) < 6:
            return max(missing, 6-len(password))
        
        # case 2: 6 <= len <= 20
        i = 2
        repeating = []
        while i < len(password):
            repeat = 2
            while i < len(password) and password[i] == password[i-1] == password[i-2]:
                repeat += 1
                i += 1
            if repeat > 2:
                repeating.append(repeat)
            i += 1
        
        if len(password) <= 20:
            replace = 0
            for repeat in repeating:
                replace += (repeat // 3)
            return max(missing, replace)
        
        # case 3: len > 20
        repeating = [(i%3, i) for i in repeating]
        heapq.heapify(repeating)
        for i in range(len(password)-20):
            if not repeating:
                break
            length_mod_3, length = heapq.heappop(repeating)
            if length-1 >= 3:
                heapq.heappush(repeating, ((length-1)%3, length-1))
        repeating = [i[1] for i in repeating]
        
        replace = 0
        for repeat in repeating:
            replace += (repeat // 3)
        return max(missing, replace)+(len(password)-20)