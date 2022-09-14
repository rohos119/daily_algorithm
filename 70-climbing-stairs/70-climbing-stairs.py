# start : 2332
# 문제정의 : n개의 개단을 오르는 방법 최대 2개의 계단을 오를수 있음
# input : 1 n 45 
# output : 방법의 수 -> int
class Solution:
    def climbStairs(self, n: int) -> int:
        
        # logic
        # top-down 접근법
        # 점화식으로 쪼개기
        def dp(index, memo = {}):
            if index in memo:
                return memo[index]
            if index == n:
                return 1
            if index > n:
                return 0
            
            memo[index + 1] = dp(index + 1)
            memo[index + 2] = dp(index + 2)
            
            return memo[index + 1] + memo[index + 2]
        
        return dp(0)