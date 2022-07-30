# 문제정의 happy number는 양수인트로 시작해서
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n > 1 and n not in s:
            s.add(n)
            st = str(n)
            sum1 = 0
            for i in st:
                sum1 += (int(i)*int(i))
            n = sum1 
            
        if n == 1:
            return 1
        return 0
        