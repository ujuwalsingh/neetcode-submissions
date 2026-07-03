class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = []
        for i in range (len(temperatures)):
            counter = False
            for j in range (i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    arr.append(j-i)
                    counter = True
                    break
            if not counter:
                    arr.append(0)
        return arr