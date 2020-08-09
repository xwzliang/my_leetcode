from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            num_needed = target - nums[i]
            if num_needed in hashtable:
                return [hashtable[num_needed], i]
            else:
                hashtable[nums[i]] = i
