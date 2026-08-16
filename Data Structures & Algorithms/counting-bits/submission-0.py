class Solution:
    def countBits(self, n: int) -> List[int]:
        a = []
        for i in range(n + 1):
            b = bin(i)
            c = b.count('1')
            a.append(c)
        return a