class Solution:
    def climbStairs(self, n: int) -> int:
        meme = [1, 2]
        
        for i in range(2, n):
            meme.append(meme[i-1]+ meme[i-2])

        return meme[n-1]

        