# 2236
# 문제정의 : 오름차순의 회전된 배열에서 target의 index를 찾아라
# input : 1 nums 5000 , -1e4 num[i] 1e4 nums[i]는 고유한 값
# output : target의 index 없으면 -1
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		left, right = 0, len(nums)-1
		while left <= right:
			mid = left + (right-left)//2
			if nums[mid] == target:
				return mid

			if nums[left] <= nums[mid]:
				if nums[mid] > target >= nums[left]:
					right = mid - 1
				else:
					left = mid + 1
			else:
				if nums[mid] < target <= nums[right]:
					left = mid + 1
				else:
					right = mid - 1

		return -1