# 높이 h, 넓이 W 인 직사각형 케익
# 수평으로 자른 곳 horizontalcut, 수직으로 자른 곳 verticalcuts
# 이때, 가장 큰 넓이를 갖는 케익을 찾아라

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        # 문제 : 가장 큰 넓이를 갖는 케익을 찾자 주어진 범위에서
        # 가장 큰 넓이를 갖는곳은 가장 먼 거리 h* 가장 먼거리 w
        # worstCase : h 가 없을때, w 가 없을때, 둘다 없을때
       
        if horizontalCuts and verticalCuts :
            horizontalCuts.sort()
            verticalCuts.sort()
            
            w_dist =[verticalCuts[0]]
            for i in range(1,len(verticalCuts)) :
                w_dist.append(verticalCuts[i]-verticalCuts[i-1])
            w_dist.append(w-verticalCuts[-1])
            
            h_dist =[horizontalCuts[0]]
            for i in range(1,len(horizontalCuts)) :
                h_dist.append(horizontalCuts[i]-horizontalCuts[i-1])
            h_dist.append(h-horizontalCuts[-1])
            
            return (max(w_dist)*max(h_dist))%(10**9+7)
        else :
            if horizontalCuts :
                horizontalCuts.sort()
                h_dist =[horizontalCuts[0]]
                for i in range(1,len(horizontalCuts)) :
                    h_dist.append(horizontalCuts[i]-horizontalCuts[i-1])
                h_dist.append(h-horizontalCuts[-1])
                return (w*max(h_dist))%(10**9+7)
            if verticalCuts:
                verticalCuts.sort()
                w_dist =[verticalCuts[0]]
                for i in range(1,len(verticalCuts)) :
                    w_dist.append(verticalCuts[i]-verticalCuts[i-1])
                w_dist.append(w-verticalCuts[-1])
                return (h*max(w_dist))%(10**9+7)
            
            return (w*h)%(10**9+7)
                        
        
        
            