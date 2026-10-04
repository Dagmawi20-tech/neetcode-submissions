class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        return s
    def decode(self, s: str) -> List[str]:
        result = []

        while s:
            length, remaining = s.split("#", 1)
            length = int(length)

            result.append(remaining[:length])
            s = remaining[length:]

        return result
        



