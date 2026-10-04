class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for number in nums:
            seen[number] = seen.get(number, 0) + 1

        highest = max(seen.values())
        buckets = [[] for _ in range(highest + 1)]

        for number, frequency in seen.items():
            buckets[frequency].append(number)

        result = []

        for frequency in range(highest, 0, -1):
            for number in buckets[frequency]:
                result.append(number)
                if len(result) == k:
                    return result