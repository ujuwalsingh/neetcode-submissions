class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for ch in s:
            if ch in "[":
                arr.append("]")
            elif ch in "(":
                arr.append(")")
            elif ch in "{":
                arr.append("}")
            else:
                if len(arr) == 0:
                    return False
                if ch == arr[-1]:
                    arr.pop()
                else:
                    return False
        return len(arr) == 0