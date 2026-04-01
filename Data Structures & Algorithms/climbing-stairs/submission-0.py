class Solution:
    def climbStairs(self, n: int) -> int:
        
        one = 0
        two = 1

        for step in range(n+1):

            new_val = one + two
            two = one
            one = new_val
    
        return one