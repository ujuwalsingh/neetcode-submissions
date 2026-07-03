class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftprod = [1] * (len(nums) + 1)
        rightprod = [1] * (len(nums) + 1)

        for i in range (len(nums)):
            leftprod[i+1] = nums[i] * leftprod[i]

        for i in range (len(nums)-1, -1, -1):
            rightprod[i] = nums[i] * rightprod[i+1]
        
        for i in range(len(nums)):
            nums[i] = leftprod[i] * rightprod[i+1]
        
        return nums
        
        # a = []
        # for i in range(len(nums)):
        #     b = 1
        #     for j in range(len(nums)):
        #         if i != j :
        #             b = b * nums[j]
        #     a.append(b)
        # return a