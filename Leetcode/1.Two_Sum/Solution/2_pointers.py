class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        S = len(nums)
        for i in range(S):
            for j in range(i+1, S):
                if nums[i] + nums[j] == target:
                    return [i,j]