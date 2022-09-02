# start 1700
# 문제정의 : 대문자,소문자, 숫자는 최소 한개이상을 포함하고, 같은 문자는 인접해서 3번 반복 안되는
#           비밀번호를 만들 수 있는 단계를 찾아라 비밀번호는 6~20
# input :  1 password 50
# output : 이미 strong 0 / 아니면 strong 만들 최소 단계
# from collections import Counter

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        
        def checkone (password) :
            count = 0
            if 6<= len(password) <= 20 :
                print('checkone',[count,0,0])
                return checktwo(password ,[count,0,0] )
            else :
                if len(password) > 20 :
                    count = len(password)-20 
                    print('checkone',[0,count,0])
                    return checktwo(password, [0,count,0])
                if len(password) < 6 :
                    count = 6-len(password)
                    print('checkone',[count,0,0])
                    return checktwo(password, [count,0,0])

        def checktwo (password, change) :
            pos = [0,0,0]
            check = Counter(password)
            for c in check :
                if c.isdecimal():
                    pos[0] = 1
                if c.isupper() :
                    pos[1] = 1
                if c.islower() :
                    pos[2] = 1
            print('pos',pos)
            if pos[0] and pos[1] and pos[2] :
                print('checktwo', change)
                return checkthree(password,change) 
            else :
                if change[0] < 3-sum(pos) :
                    if len(password) < 6 :
                        change[0] += 3-sum(pos)-change[0]
                        print('checktwo', change)
                    if len(password) > 20 :
                        change[0] += 3-sum(pos)
                        change[2] += 3-sum(pos)
                        print('checktwo', change)
                    if 6 <= len(password) <= 20 :
                        change[0] += 3-sum(pos)
                        change[2] += 3-sum(pos)
                return checkthree(password,change)

        def checkthree(password, change) :
            count = 0
            if len(password) < 6 :
                return change[0]
            
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
            print(repeating)
            
            if len(password) <= 20 :
                for repeat in repeating:
                    change[2] += (repeat // 3)
                print(change)
                return max(change[0],change[2])-min(change[0],change[2])
            
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
                change[2] += (repeat // 3)
            print(change)
            if change[0] > change[2] :
                return change[0]-change[2]+change[1]
            elif change[0] == change[2] :
                return change[0]+change[1]
            else :
                return change[2]-change[0]+change[1]
