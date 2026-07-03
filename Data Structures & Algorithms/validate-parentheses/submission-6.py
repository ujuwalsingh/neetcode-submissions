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

        # b = {
        #     ")" : "(",
        #     "}" : "{",
        #     "]" : "["
        # }
        # arr = []
        # for ch in s:
        #     if ch in "({[":
        #         arr.append(ch)
        #     else:
        #         if not arr:
        #             return False
        #         c = arr.pop()
        #         if c != b[ch]:
        #             return False
        # return len(arr) == 0