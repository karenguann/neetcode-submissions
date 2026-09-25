class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            if i not in count:
                count[i] = 0

            count[i] += 1

        buckets = [[] for i in range(len(nums) + 1)]

        for i in count:
            frequency = count[i]
            buckets[frequency].append(i)
        
        output = []

        for frequency in range(len(nums), 0, -1):
            for num in buckets[frequency]:
                output.append(num)

                if len(output) == k:
                    return output

        