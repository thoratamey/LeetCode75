class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        larg=max(nums)
        for i in range(len(nums)):
            if larg==nums[i]:
                return i
