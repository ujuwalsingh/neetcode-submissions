class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            speed = (left + right) // 2

            hours = 0
            for bananas in piles:
                hours += (bananas + speed - 1) // speed

            if hours <= h:
                right = speed
            else:
                left = speed + 1

        return left