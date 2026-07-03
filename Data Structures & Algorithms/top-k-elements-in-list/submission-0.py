class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = []
        for i in set(nums):
            count = 0
            for j in nums:
                if i == j:
                    count += 1
            a.append([count,i])
            a.sort(reverse = True)
        b = []
        for i in range(k):
            b.append(a[i][1])
        return b