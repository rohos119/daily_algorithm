# start 2115
# 문제정의 : 특정인덱스에서 시작해서 다시 특정 인덱스까지 올 수 있는 인덱스로 구하라
# input : 1 n 1e5 / 0 gas,cost 1e4 / 
# output : 순회 가능한 index -> int / 없으면 -1
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # logic
        # 왜 greedy 접근법일까?
        # 최적해를 보장한다? 어떻게 -> 시작점에서 더하고, cost를 빼고 이 과정이 최적해인가?
        
        
        startIndex = 0
        current = 0
        
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        
        for i in range(n):
            current += gas[i] - cost[i]
            if current < 0:
                startIndex = i + 1
                current = 0
                
        return startIndex