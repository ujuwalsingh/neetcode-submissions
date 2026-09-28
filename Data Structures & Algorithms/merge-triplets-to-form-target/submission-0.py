class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        valid_indices = set()
        
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for i in range(3):
                if t[i] == target[i]:
                    valid_indices.add(i)
                    
        return len(valid_indices) == 3