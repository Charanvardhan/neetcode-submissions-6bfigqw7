class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {
            '2':'abc', '3':'def', '4':'ghi', '5':'jkl',
            '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'
        }
        res = []
        cur = []

        def letterComb(cur,i):
            if i == len(digits):
                if len(cur) > 0:         # ✅ base case: used every digit
                    res.append(''.join(cur))
                return
            
            for k in mappings[digits[i]]: # ✅ only loop over letters for digit[i]
                cur.append(k)
                letterComb(cur, i+1)           # ✅ always move to next digit
                cur.pop()


        letterComb(cur, 0)

        return res

