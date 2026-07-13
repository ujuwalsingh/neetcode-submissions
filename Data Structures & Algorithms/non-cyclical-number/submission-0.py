class Solution:
    def sq_of_digits(self, num):
        sums = 0
        while num > 0:
            i = num % 10
            sums = sums + i**2
            num = num // 10
        return sums
    
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sq_of_digits(n)
        return n==1


    