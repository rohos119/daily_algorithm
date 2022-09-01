# start 2115
# 문제정의 : 특정인덱스에서 시작해서 다시 특정 인덱스까지 올 수 있는 인덱스로 구하라
# input : 1 n 1e5 / 0 gas,cost 1e4 / 
# output : 순회 가능한 index -> int / 없으면 -1
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # logic
        # 왜 greedy 접근법일까?
        # 최적해를 보장한다? 어떻게 -> 시작점에서 더하고, cost를 빼고 이 과정이 최적해인가?
        
        first_station = 0
        available_gas = 0
        gas_cost_diff = 0
        for i in range(len(gas)):
            gas_cost_diff = gas_cost_diff + gas[i] - cost[i]
            available_gas = available_gas + gas[i] - cost[i]
            if available_gas < 0:
                available_gas = 0
                first_station = i + 1
        if gas_cost_diff >= 0:
            return first_station
        else:
            return -1