class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        compDict = {}
        
        for x in range(len(nums)):
            if nums[x] in compDict:
                return [compDict[nums[x]],x]
            compDict[target - nums[x]] = x