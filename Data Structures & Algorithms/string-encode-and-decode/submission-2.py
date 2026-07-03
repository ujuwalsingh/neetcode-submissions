class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += i
            s += "ø"
        return s

    def decode(self, s: str) -> List[str]:
        word = ""
        arr = []
        for ch in s:
            if ch == "ø":
                arr.append(word)
                word = ""
                continue
            word += ch
        return arr 