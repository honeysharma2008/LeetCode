
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                new = nums[i] + nums[j]

                if new == target:
                    return [i, j]
