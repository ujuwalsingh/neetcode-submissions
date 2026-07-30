class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i-1] +1 :
        #         return nums[i] -1 
        
        # return 0