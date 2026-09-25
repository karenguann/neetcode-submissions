class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for j in range(len(nums)):
            seen[nums[j]] = j
        
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen:
                if i == seen[difference]:
                    continue
                elif i < seen[difference]:
                    return [i, seen[difference]]
                else:
                    return [seen[difference], i]


        