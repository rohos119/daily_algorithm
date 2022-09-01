# start 2224
# 문제정의 : k를 지운 가장 작은 숫자를 반환하라
# input : 1 k num 1e5
# output : 가장작은 숫자 -> string
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        # logic
        # 가장 작은수를 만들 수 있는 경우
        # 가장 앞자리부터 확인하는데
        # 만약 가장 앞자리 보다 작을 경우만 현재꺼 삭제
        # 아닐경우에는 그냥 뒤에거 삭제
        if k == len(num) or len(num) < 2 :
            return "0"
        
        temp =[]
        i=0
        count = k
        while k > 0 and i < len(num) :
            #print(temp,k,num[i])
            # 가장 앞자리가 뒤보다 클경우
            if temp and num[i] < temp[-1] :
                temp.pop()
                k -=1
            # 앞보다 뒤가 더 클경우
            else :
                temp.append(num[i])
                i += 1
        if k == 0:
            #print(''.join(temp),num[i:])
            return str(int(''.join(temp)+num[i:]))    
        else:
            #print(''.join(temp[:len(num)-count]))
            return str(int(''.join(temp[:len(num)-count])))