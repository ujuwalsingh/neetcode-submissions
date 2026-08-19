import itertools
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        for r in range(len(nums) + 1):
            combinations = itertools.combinations(nums, r)
            subset.extend(map(list, combinations))
        seen = set()
        x = []
        for i in subset:
            a = tuple(sorted(i))
            if a not in seen:
                seen.add(a)
                x.append(i)
        return x