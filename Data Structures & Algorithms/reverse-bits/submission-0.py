class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(format(n, "032b"))
        n = "".join(reversed(n))
        return int(n, 2)