class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strs = ""
        for i in digits:
            strs += str(i)
        string = str(int(strs) + 1)
        arr = []
        for i in string:
            arr.append(int(i))
        return arr