class Solution:
    def reverse(self, x: int) -> int:
        z = x
        if x < 0:
            x = x * -1
        s = str(x)
        a = ""
        for i in range(len(s)-1, -1, -1):
            a += s[i]
        if z < 0:
            a = (-1 *(int(a)))
        else:
            a = int(a)
        if a in range(-2**31, (2**31) -1):
            return a
        else:
            return 0
        