class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num = sorted(nums)
        seen = []
        for i in num:
            if i not in seen:
                seen.append(i)
        count = 1
        maxcount = 1
        for i in range (len(seen)):
            counter = False
            for k in range (i + 1, len(seen)):
                if seen[i] + 1 == seen[k]:
                    count +=1
                    counter = True
                if counter == False:
                    count = 1
                maxcount = max(count, maxcount)
        return maxcount
        