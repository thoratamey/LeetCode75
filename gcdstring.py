class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        def gcd(len1, len2):
            while len2:
                len1, len2 = len2, len1 % len2
            return len1
        return str1[:gcd(len(str1), len(str2))]
