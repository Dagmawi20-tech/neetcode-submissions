class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 = sorted(list(s))
        w2 = sorted(list(t))
        return w1 == w2


