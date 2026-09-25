class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(nums)
        count = {}

        for i in sorted_nums:
            if i not in count:
                count[i] = 0
            count[i] += 1
        
        sorted_nums = sorted(count.items(), key=lambda x: x[1], reverse=True)

        output = []

        for i in range(k):
            output.append(sorted_nums[i][0])
        
        return output

        