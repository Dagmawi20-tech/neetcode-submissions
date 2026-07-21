class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = s.replace(" ", "")
        x = p.replace("?", "")
        d = x.replace(",", "")
        f = d.replace("'", "")
        z = f.replace(".", "")
        y = z.replace(":", "")
        r = y[::-1]
        return r.lower() == y.lower()
        