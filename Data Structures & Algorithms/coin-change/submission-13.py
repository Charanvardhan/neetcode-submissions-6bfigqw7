class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        mem= {}
        
        def traversal(temp, depth, mem, target):
            nonlocal op
            if target - temp in mem:
                return depth + mem[target - temp]
            if temp > target:
                return False
            if temp == target:
                op = min(op, depth)
                return depth
            
            for i in coins:
                cur = traversal(temp+i, depth + 1, mem, target)
                if cur is not False:
                    op = min(op, cur)
                
            
        for i in range(amount+1):   
            op = 2**32 -1 
            traversal(0, 0, mem, i)
            mem[i] = op

        if mem[amount] == 4294967295:
            return -1
        return mem[amount]