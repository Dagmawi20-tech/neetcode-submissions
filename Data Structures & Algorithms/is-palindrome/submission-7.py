class Solution:
    def isPalindrome(self, s: str) -> bool:
        se = []
        for i in s:
            if i not in ",:? '.":
                se.append(i.lower())
        es = se[::-1]
        return es == se
        