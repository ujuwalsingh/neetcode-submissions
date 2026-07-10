class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = len(s1)
        for i in range(len(s2)):
            b = ""
            if s2[i] in s1:
                b = s2[i:i+a]
            if sorted(s1) == sorted(b):
                return True
        return False