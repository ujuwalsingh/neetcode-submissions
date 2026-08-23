import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        a = {
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz"
        }
        if digits == "":
            return []
        b = []
        for i in str(digits):
            b.append(a[int(i)])
        return ["".join(p) for p in itertools.product(*b)]