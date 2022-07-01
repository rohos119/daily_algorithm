class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        answer = 0
        boxTypes.sort(key=lambda x: x[1])
        while truckSize > 0 :
            if boxTypes :
                t = boxTypes.pop() 
                if truckSize > t[0] :
                    answer += t[0]*t[1]
                    truckSize -= t[0]
                else :
                    answer += truckSize*t[1]
                    truckSize -= t[0]
            else :
                break
        return answer
        