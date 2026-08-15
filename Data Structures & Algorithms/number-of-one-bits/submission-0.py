class Solution:
    def hammingWeight(self, n: int) -> int:
        a = bin(n)
        return a.count("1")