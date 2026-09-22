class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0

        ones = 0
        while n != 1:
            if n%2 != 0:
                ones += 1
            n = n // 2
        
        return ones + 1
        

        