class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel=set("aeiou")
        count=0
        max_vo=0
        for right in range(len(s)):
            if s[right] in vowel:
                count+=1
            if right>=k:
                if s[right-k] in vowel:
                    count-=1
            max_vo=max(max_vo,count)
        return max_vo
