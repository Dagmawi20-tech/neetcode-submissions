class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        count = 0
        buckets = []
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for number, frequency in seen.items():
            buckets[frequency].append(number)
            result = []

        for frequency in range(len(buckets) - 1, 0, -1):
            for number in buckets[frequency]:
                result.append(number)
                if len(result) == k:
                    return result
        