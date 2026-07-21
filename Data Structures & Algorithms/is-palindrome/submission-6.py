class Solution:
    def isPalindrome(self, s: str) -> bool:
        se = []
        for i in range(len(s)):
            if s[i] not in ",:? '.":
                se.append(s[i].lower())
        es = se[::-1]
        return es == se
        