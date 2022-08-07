# 2236
# 문제정의 : 오름차순의 회전된 배열에서 target의 index를 찾아라
# input : 1 nums 5000 , -1e4 num[i] 1e4 nums[i]는 고유한 값
# output : target의 index 없으면 -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print(nums)
        
        return nums.index(target) if target in nums else -1  