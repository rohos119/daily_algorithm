# start : 1700
# 문제정의 : tops 과 bottom의 주사위 리스트를 top이 같은 숫자가 되던, bottom이 같은 숫자가 되게끔 최소한의 스왑을 활용해서 만들어라
# input : 2 tops,bottom 2*1e4 / 1 top[i],bottom[i] 6
# output : 만들수 없을땐 -1 / 최소 회전 수
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        # logic
        # bottom을 바꿀 건지 top을 바꿀건지 먼저 선택을 한다?
        # counter로 세서 확인가능 ??
        # 바꿀 리스트 결정 -> 가장 많은 수를 갖는 곳에서 부터는 안된다.
        # 같은 값을 갖는 곳을 탑기준으로 찾고,
        # 바꿀 리스트를 결정했다면, 어떻게 뽑을지를 결정하자 
        
#         topcount = collections.Counter(tops)
#         bottomcount = collections.Counter(bottoms)
#         # print(topcount,bottomcount)
#         topcount = sorted(topcount, key=lambda x : topcount[x])
#         bottomcount = sorted(bottomcount, key=lambda x : bottomcount[x])
#         # print(topcount,bottomcount)
        
#         if topcount[0] > bottomcount[0] :
#             for t
            
        sames = [tops[i] for i in range(len(tops)) if tops[i] == bottoms[i]]
        print(sames)
        samecount = collections.Counter(sames)
        bottomcount = collections.Counter(bottoms)
        topcount = collections.Counter(tops)
        
        for n in range(1,7):
            if bottomcount[n] + topcount[n] - samecount[n] == len(tops):
                return min(bottomcount[n], topcount[n]) - samecount[n]
            
        return -1