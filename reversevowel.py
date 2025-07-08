class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        l=0
        r=len(s)-1
        lst=set("aeiouAEIOU")
        while l<=r:
            if not s[l] in lst:
                l+=1
            elif not s[r] in lst:
                r-=1
            else:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
        return "".join(s)
