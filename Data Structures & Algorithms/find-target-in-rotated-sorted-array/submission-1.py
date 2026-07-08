class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # try:
        #     idx = nums.index(target)
        # except ValueError:
        #     idx = -1
        # return idx

        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1