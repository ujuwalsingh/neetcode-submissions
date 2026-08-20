class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        a = []
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end,s.rfind(s[i]))

            if end == i:
                a.append(end - start + 1)

                start = i + 1
        return a