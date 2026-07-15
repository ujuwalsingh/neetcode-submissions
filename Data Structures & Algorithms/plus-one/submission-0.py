class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strs = ""
        for i in digits:
            strs += str(i)
        dig = int(strs) + 1
        arr = []
        string = str(dig)
        for i in string:
            arr.append(int(i))
        return arr