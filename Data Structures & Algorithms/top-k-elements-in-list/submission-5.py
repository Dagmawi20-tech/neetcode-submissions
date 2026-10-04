class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        count = 0
        lyst = []
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        while count<k: 
            num = max(seen, key = seen.get)
            lyst.append(num)
            del(seen[num])
            count += 1
        return lyst