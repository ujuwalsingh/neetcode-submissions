class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxval = nums[0]
        currsum = nums[0]
        for i in range(1,len(nums)):
            currsum = max(nums[i], nums[i] + currsum)

            maxval = max(maxval,currsum)
        return maxval
