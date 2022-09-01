# start 2115
# 문제정의 : 특정인덱스에서 시작해서 다시 특정 인덱스까지 올 수 있는 인덱스로 구하라
# input : 1 n 1e5 / 0 gas,cost 1e4 / 
# output : 순회 가능한 index -> int / 없으면 -1
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # logic
        # 왜 greedy 접근법일까?
        # 최적해를 보장한다? 어떻게 -> 시작점에서 더하고, cost를 빼고 이 과정이 최적해인가?
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
        if tank < 0:
            return -1

        start = 0
        extra = 0
        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            if extra + gain < 0:
                start = i + 1
                extra = 0
            else:
                extra += gain
        return start