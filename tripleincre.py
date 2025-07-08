class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        h, m = float('-inf'), float('-inf')
        for num in reversed(nums):
            if num >= h:
                h = num
            elif num >= m:
                m = num
            else:
                return True
        return False
