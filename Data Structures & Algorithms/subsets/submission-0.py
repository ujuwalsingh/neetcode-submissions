import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        for r in range(len(nums) + 1):
            combinations = itertools.combinations(nums, r)
            subset.extend(map(list, combinations))
        return subset