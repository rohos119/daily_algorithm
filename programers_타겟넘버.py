#문제정의 : 주어진 숫자로 +,-를 활용하여 target 값으로 만들 수 있는 수를 찾아라
# input : 2 < number < 20 
# BigO(N^2) 까지는 가능할듯 싶다

from collections import deque
def solution(numbers, target):
    answer = 0
    depth = 0
    dq = deque([[numbers[0],-numbers[0]]])
    while dq and depth < len(numbers)-1:
        temp = dq.pop()
        n = []
        depth += 1
        for t in temp:
            n += [t + numbers[depth], t - numbers[depth]]
        dq.append(n)
    answer = dq.pop().count(target)
    return answer
