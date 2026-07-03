class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for i in strs:
            key = ''.join(sorted(i))
            a[key].append(i)
        return list(a.values())