class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = 0
        dic = {}
        n_l = []
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        sortedKey = sorted(dic, key=lambda x: dic[x], reverse=True)
        return sortedKey[:k]

                

