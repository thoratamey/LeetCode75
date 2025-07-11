class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_length = 0
        k = 1
        for right in range(len(nums)):
            if nums[right] == 0:
                k-=1
            while(k<0):
                if nums[left] == 0:
                    k+=1
                left += 1
            max_length = max(max_length, right - left)
        return max_length
