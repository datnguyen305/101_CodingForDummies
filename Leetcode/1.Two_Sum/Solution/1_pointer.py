class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        memory = {}
        for i in range(len(nums)):
           remainder = target - nums[i]
           if remainder in memory:
            return [i, memory[remainder]]
           memory[nums[i]] = i