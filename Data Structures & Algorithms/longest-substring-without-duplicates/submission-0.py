class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxv = 0
        for i in range (len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j]in seen:
                    break
                seen.add(s[j])

                maxv = max(maxv, j - i + 1) 
        return maxv
        

        # maxv = 0
        # for i in range (len(s)):
        #     seen = []
        #     for j in range(i, len(s)):
        #         if s[j]in seen:
        #             break
        #         seen.append(s[j])

        #     maxv = max(maxv, len(seen)) 
        # return maxv