class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i in range (len(position)):
            position[i] = target - position[i]
        for i in range (len(position)):
            position[i] = [position[i], speed[i]]
        position.sort(key=lambda x: x[0])
        for i in range(len(speed)):
            position[i] = position[i][0] / position[i][1]
        
        i = 1 
        while i < len(position):
            if position[i] <= position[i-1]:
                position.pop(i)
            else:
                i+= 1
        return len(position)