class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=0
        res=0
        for i in range(len(gain)):
            ans=ans+gain[i]
            res=max(ans,res)
        return res
        
